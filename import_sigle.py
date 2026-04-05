#!/usr/bin/env python3
"""
Import blog posts from Sigle (via Internet Archive) into Jekyll _posts.

Usage:
    python3 import_sigle.py

This script:
1. Fetches the listing page from the Internet Archive to get all post metadata
2. Fetches each individual post page to get full HTML content
3. Downloads images locally
4. Converts HTML content to Markdown
5. Creates Jekyll-compatible post files in _posts/
"""

import json
import os
import re
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path

REPO_ROOT = Path(__file__).parent
POSTS_DIR = REPO_ROOT / "_posts"
IMAGES_DIR = REPO_ROOT / "images"

LISTING_URL = "https://web.archive.org/web/20250418224235id_/https://app.sigle.io/friedger.id.stx"

# CDX entries: slug -> timestamp (from Wayback CDX API)
CDX_URL = "http://web.archive.org/cdx/search/cdx?url=app.sigle.io/friedger.id.stx/*&output=text&fl=original,timestamp,statuscode&filter=statuscode:200&collapse=urlkey"

# Cache for CDX lookups of image URLs
_image_cdx_cache = {}


def fetch_url(url, retries=3, delay=2):
    """Fetch URL content with retries."""
    # URL-encode spaces and other unsafe chars in path
    url = url.replace(" ", "%20")
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.read()
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, ValueError) as e:
            print(f"  Attempt {attempt+1} failed for {url}: {e}")
            if attempt < retries - 1:
                time.sleep(delay * (attempt + 1))
    return None


def extract_next_data(html_bytes):
    """Extract __NEXT_DATA__ JSON from HTML page."""
    html = html_bytes.decode("utf-8", errors="replace")
    marker = '__NEXT_DATA__" type="application/json">'
    idx = html.find(marker)
    if idx < 0:
        # Try alternate format
        marker = "__NEXT_DATA__' type='application/json'>"
        idx = html.find(marker)
    if idx < 0:
        return None
    start = html.find(">", idx) + 1
    end = html.find("</script>", start)
    if end < 0:
        return None
    try:
        return json.loads(html[start:end])
    except json.JSONDecodeError:
        return None


def get_existing_titles():
    """Get set of existing post titles (lowercased)."""
    titles = set()
    for f in POSTS_DIR.glob("*.md"):
        with open(f) as fh:
            for line in fh:
                if line.startswith("title:"):
                    titles.add(line.split(":", 1)[1].strip().lower())
                    break
    return titles


def get_cdx_timestamps():
    """Fetch CDX timestamps for all individual post pages."""
    print("Fetching CDX index...")
    data = fetch_url(CDX_URL)
    if not data:
        return {}
    timestamps = {}
    for line in data.decode().strip().split("\n"):
        parts = line.split()
        if len(parts) >= 3:
            url, ts, status = parts[0], parts[1], parts[2]
            # Extract slug from URL
            match = re.search(r"friedger\.id\.stx/(.+)$", url)
            if match:
                slug = match.group(1)
                # Keep the first (oldest) capture
                if slug not in timestamps:
                    timestamps[slug] = ts
    return timestamps


def get_wayback_timestamp(url):
    """Look up the Wayback Machine CDX for the best timestamp for a URL."""
    if url in _image_cdx_cache:
        return _image_cdx_cache[url]

    encoded_url = url.replace(" ", "%20")
    cdx_query = f"http://web.archive.org/cdx/search/cdx?url={encoded_url}&output=text&fl=timestamp,statuscode&filter=statuscode:200&limit=1"
    try:
        data = fetch_url(cdx_query, retries=2, delay=1)
        if data:
            line = data.decode().strip()
            if line:
                ts = line.split()[0]
                _image_cdx_cache[url] = ts
                return ts
    except Exception:
        pass
    _image_cdx_cache[url] = None
    return None


def slugify(title):
    """Convert title to URL-friendly slug."""
    slug = title.lower()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"[\s]+", "-", slug.strip())
    slug = re.sub(r"-+", "-", slug)
    return slug


def html_to_markdown(html_content):
    """Convert HTML content to Markdown."""
    if not html_content:
        return ""

    text = html_content

    # Handle code blocks first (before other transformations)
    # <pre><code class="language-xxx">...</code></pre>
    def replace_code_block(m):
        lang = ""
        lang_match = re.search(r'class="language-(\w+)"', m.group(0))
        if lang_match:
            lang = lang_match.group(1)
        code = m.group(1)
        # Decode HTML entities in code
        code = code.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&").replace("&quot;", '"')
        return f"\n\n```{lang}\n{code}\n```\n\n"

    text = re.sub(r"<pre[^>]*><code[^>]*>(.*?)</code></pre>", replace_code_block, text, flags=re.DOTALL)
    text = re.sub(r"<pre[^>]*>(.*?)</pre>", replace_code_block, text, flags=re.DOTALL)

    # Inline code
    text = re.sub(r"<code[^>]*>(.*?)</code>", r"`\1`", text)

    # Headings
    for i in range(6, 0, -1):
        text = re.sub(rf"<h{i}[^>]*>(.*?)</h{i}>", "\n\n" + "#" * i + r" \1\n\n", text, flags=re.DOTALL)

    # Bold and italic
    text = re.sub(r"<strong>(.*?)</strong>", r"**\1**", text, flags=re.DOTALL)
    text = re.sub(r"<b>(.*?)</b>", r"**\1**", text, flags=re.DOTALL)
    text = re.sub(r"<em>(.*?)</em>", r"*\1*", text, flags=re.DOTALL)
    text = re.sub(r"<i>(.*?)</i>", r"*\1*", text, flags=re.DOTALL)

    # Images - extract src and alt
    def replace_img(m):
        tag = m.group(0)
        src_match = re.search(r'src="([^"]*)"', tag)
        alt_match = re.search(r'alt="([^"]*)"', tag)
        src = src_match.group(1) if src_match else ""
        alt = alt_match.group(1) if alt_match else ""
        return f"\n\n![{alt}]({src})\n\n"

    text = re.sub(r"<img[^>]*/>", replace_img, text)
    text = re.sub(r"<img[^>]*>", replace_img, text)

    # Links
    def replace_link(m):
        href = m.group(1)
        link_text = m.group(2)
        # Strip any remaining HTML from link text
        link_text = re.sub(r"<[^>]+>", "", link_text)
        if not link_text.strip():
            link_text = href
        return f"[{link_text}]({href})"

    text = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', replace_link, text, flags=re.DOTALL)

    # Lists
    text = re.sub(r"<ul[^>]*>", "\n", text)
    text = re.sub(r"</ul>", "\n", text)
    text = re.sub(r"<ol[^>]*>", "\n", text)
    text = re.sub(r"</ol>", "\n", text)
    text = re.sub(r"<li[^>]*>(.*?)</li>", r"- \1\n", text, flags=re.DOTALL)

    # Blockquotes
    text = re.sub(r"<blockquote[^>]*>(.*?)</blockquote>", lambda m: "\n" + "\n".join("> " + line for line in m.group(1).strip().split("\n")) + "\n", text, flags=re.DOTALL)

    # Horizontal rules
    text = re.sub(r"<hr[^>]*/?>", "\n\n---\n\n", text)

    # Line breaks
    text = re.sub(r"<br[^>]*/?>", "\n", text)

    # Paragraphs
    text = re.sub(r"<p[^>]*>", "\n\n", text)
    text = re.sub(r"</p>", "\n\n", text)

    # Divs and spans
    text = re.sub(r"<div[^>]*>", "\n", text)
    text = re.sub(r"</div>", "\n", text)
    text = re.sub(r"<span[^>]*>", "", text)
    text = re.sub(r"</span>", "", text)

    # Remove remaining HTML tags
    text = re.sub(r"<[^>]+>", "", text)

    # Decode HTML entities
    text = text.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
    text = text.replace("&quot;", '"').replace("&apos;", "'").replace("&nbsp;", " ")

    # Clean up whitespace
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = text.strip()

    return text


def download_image(url, post_slug):
    """Download an image and return the local path relative to repo root."""
    # Clean wayback URLs
    clean_url = re.sub(r"https?://web\.archive\.org/web/\d+/", "", url)
    if not clean_url.startswith("http"):
        clean_url = url

    # Determine filename from URL
    filename = clean_url.split("/")[-1]
    # Clean up filename
    filename = re.sub(r"[?#].*$", "", filename)
    if not filename or len(filename) > 100:
        filename = f"{post_slug}-image.jpg"

    # Prefix with post slug to avoid collisions
    local_filename = f"{post_slug}-{filename}"
    local_path = IMAGES_DIR / local_filename

    if local_path.exists():
        print(f"    Image already exists: {local_filename}")
        return f"/images/{local_filename}"

    # First try CDX lookup for exact Wayback timestamp
    for base_url in [clean_url] + ([clean_url.replace("gaia.blockstack.org", "gaia.hiro.so")] if "gaia.blockstack.org" in clean_url else []):
        ts = get_wayback_timestamp(base_url)
        if ts:
            wb_url = f"https://web.archive.org/web/{ts}id_/{base_url}"
            data = fetch_url(wb_url, retries=2, delay=1)
            if data and len(data) > 100:
                local_path.write_bytes(data)
                print(f"    Downloaded (wayback): {local_filename} ({len(data)} bytes)")
                return f"/images/{local_filename}"

    # Fallback: try original URLs directly
    urls_to_try = [clean_url]
    if "gaia.blockstack.org" in clean_url:
        urls_to_try.append(clean_url.replace("gaia.blockstack.org", "gaia.hiro.so"))

    for try_url in urls_to_try:
        data = fetch_url(try_url, retries=1, delay=1)
        if data and len(data) > 100:
            local_path.write_bytes(data)
            print(f"    Downloaded: {local_filename} ({len(data)} bytes)")
            return f"/images/{local_filename}"

    print(f"    FAILED to download: {clean_url}")
    return clean_url  # Return original URL as fallback


def process_images_in_content(content, post_slug):
    """Find all image URLs in markdown content and download them."""

    def replace_image(m):
        alt = m.group(1)
        url = m.group(2)
        if url.startswith("/images/") or url.startswith("images/"):
            return m.group(0)  # Already local
        local_path = download_image(url, post_slug)
        return f"![{alt}]({local_path})"

    return re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", replace_image, content)


def download_cover_image(url, post_slug):
    """Download cover image, return local filename (without path)."""
    if not url:
        return None

    clean_url = re.sub(r"https?://web\.archive\.org/web/\d+/", "", url)
    ext = os.path.splitext(clean_url.split("?")[0])[-1] or ".jpg"
    filename = f"{post_slug}{ext}"
    local_path = IMAGES_DIR / filename

    if local_path.exists():
        print(f"    Cover already exists: {filename}")
        return filename

    # First try CDX lookup for exact Wayback timestamp
    for base_url in [clean_url] + ([clean_url.replace("gaia.blockstack.org", "gaia.hiro.so")] if "gaia.blockstack.org" in clean_url else []):
        ts = get_wayback_timestamp(base_url)
        if ts:
            wb_url = f"https://web.archive.org/web/{ts}id_/{base_url}"
            data = fetch_url(wb_url, retries=2, delay=1)
            if data and len(data) > 100:
                local_path.write_bytes(data)
                print(f"    Cover downloaded (wayback): {filename} ({len(data)} bytes)")
                return filename

    # Fallback: try original URLs directly
    for try_url in [clean_url] + ([clean_url.replace("gaia.blockstack.org", "gaia.hiro.so")] if "gaia.blockstack.org" in clean_url else []):
        data = fetch_url(try_url, retries=1, delay=1)
        if data and len(data) > 100:
            local_path.write_bytes(data)
            print(f"    Cover downloaded: {filename} ({len(data)} bytes)")
            return filename

    print(f"    FAILED to download cover: {clean_url}")
    return None


def create_post(title, date, content_md, cover_image_filename):
    """Create a Jekyll post file."""
    slug = slugify(title)
    date_str = date.strftime("%Y-%m-%d")
    filename = f"{date_str}-{slug}.md"
    filepath = POSTS_DIR / filename

    image_line = ""
    if cover_image_filename:
        image_line = f"\n  title: {cover_image_filename}"

    frontmatter = f"""---
title: "{title}"
categories: blockstack
image:{image_line}
---
"""

    with open(filepath, "w") as f:
        f.write(frontmatter)
        f.write("\n")
        f.write(content_md)
        f.write("\n")

    print(f"  Created: {filename}")
    return filepath


def main():
    print("=" * 60)
    print("Sigle Blog Post Importer")
    print("=" * 60)

    # Step 1: Get CDX timestamps for individual posts
    cdx_timestamps = get_cdx_timestamps()
    print(f"Found {len(cdx_timestamps)} captured post pages in Wayback")

    # Step 2: Fetch listing page to get all post metadata
    print("\nFetching listing page...")
    listing_html = fetch_url(LISTING_URL)
    if not listing_html:
        print("ERROR: Could not fetch listing page")
        sys.exit(1)

    data = extract_next_data(listing_html)
    if not data:
        print("ERROR: Could not extract __NEXT_DATA__ from listing page")
        sys.exit(1)

    stories = data["props"]["pageProps"]["file"]["stories"]
    print(f"Found {len(stories)} stories in listing")

    # Step 3: Get existing post titles
    existing_titles = get_existing_titles()

    # Step 4: Process each new post
    new_stories = [s for s in stories if s["title"].lower() not in existing_titles]
    print(f"\n{len(new_stories)} new posts to import (skipping {len(stories) - len(new_stories)} existing)")

    created = 0
    failed = 0

    for i, story in enumerate(new_stories):
        title = story["title"]
        story_id = story["id"]
        date = datetime.fromtimestamp(story["createdAt"] / 1000)
        cover_url = story.get("coverImage", "")
        slug = slugify(title)

        print(f"\n[{i+1}/{len(new_stories)}] {title} ({date.strftime('%Y-%m-%d')})")

        # Fetch full content from individual post page
        ts = cdx_timestamps.get(story_id)
        html_content = None

        if ts:
            post_url = f"https://web.archive.org/web/{ts}id_/https://app.sigle.io/friedger.id.stx/{story_id}"
            print(f"  Fetching content...")
            post_html = fetch_url(post_url)
            if post_html:
                post_data = extract_next_data(post_html)
                if post_data:
                    file_data = post_data["props"]["pageProps"].get("file", {})
                    html_content = file_data.get("content", "")

        if not html_content:
            # Fall back to excerpt from listing page
            excerpt = story.get("content", "")
            if excerpt:
                print(f"  WARNING: Using excerpt only (no full capture available)")
                html_content = f"<p>{excerpt}</p>"
            else:
                print(f"  ERROR: No content available at all, skipping")
                failed += 1
                continue

        if not html_content:
            print(f"  WARNING: Empty content")
            failed += 1
            continue

        # Convert HTML to Markdown
        content_md = html_to_markdown(html_content)

        # Download cover image
        cover_filename = download_cover_image(cover_url, slug)

        # Download and localize inline images
        content_md = process_images_in_content(content_md, slug)

        # Create the post
        create_post(title, date, content_md, cover_filename)
        created += 1

        # Be nice to the Wayback Machine
        time.sleep(1)

    print(f"\n{'=' * 60}")
    print(f"Done! Created {created} posts, {failed} failed")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
