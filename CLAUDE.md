# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

OpenIntents community website (openintents.github.io) — a Jekyll-based static site hosted on GitHub Pages. Primary content is Android Intent specifications, plus a blog and app showcase.

## Development Commands

```bash
# Install dependencies
bundle install

# Run local dev server (uses localhost:4000)
jekyll serve --config _config.yml,_config_dev.yml
```

Deployment is automatic via GitHub Pages on push to master.

## Architecture

**Jekyll collections** drive the site:
- `_intent_specs/` — Intent specification pages (output to `/action/{name}/`). Each is a Markdown file with YAML frontmatter defining action, uri, type, extras, implementations, etc. The `specification.html` layout auto-generates Java code snippets, intent filters, and implementation lists from this frontmatter.
- `_apps/` — App showcase pages (output to `/{name}/`)
- `_posts/` — Blog posts with date-based permalinks

**Layout hierarchy:** `compress.html` → `default.html` → content layouts (frontpage, specification, blog-post, app, page, etc.)

**Data files** in `_data/`: `navigation.yml` (site nav structure), `authors.yml`, `socialmedia.yml`, etc.

**Styling:** SCSS in `_sass/`, based on Foundation grid framework. Files are numbered `_01_` through `_12_` for load order.

**Custom plugin:** `_plugins/titleize.rb` — Liquid filter converting text to camelCase (used in specification code generation).

## Intent Specification Format

Each file in `_intent_specs/` uses this frontmatter structure:
- `title`, `action`, `constant`, `uri`, `type`, `component` — core spec metadata
- `extras` — array of `{name, type, description, sample_value}`
- `out` — return value spec (same structure as extras)
- `implementations` — array of `{name, link}` for apps implementing the spec
- `hide_use` / `hide_intent_filter` — flags to suppress auto-generated code sections
- `link` — reference URL (Android docs, etc.)

## Key Configuration

- `_config.yml` — main Jekyll config (collections, plugins, permalink structure)
- `_config_dev.yml` — local dev overrides (localhost URLs)
- Plugins: jekyll-redirect-from, jekyll-seo-tag, jekyll-paginate
