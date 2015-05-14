---
layout: page
show_meta: false
subheadline: "Intents Registry"
title: "See All Intents"
teaser: "These are all the possibilities to save your time and delegate to other apps."
header:
   image_fullwidth: "header_unsplash_5.jpg"
permalink: "/intentsregistry/"
---
<ul>
    {% for spec in site.intent_specs %}
    <li><a href="{{ site.url }}/action/{{ spec.action | slugify  }}">{{ spec.title }}</a></li>
    {% endfor %}
</ul>