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
<a href="https://github.com/openintents/openintents.github.io/new/master/_intent_specs">Add a new intent protocol via Github.</a>
<ul>
    {% assign ordered_specs = site.intent_specs | where "type", "activity" | sort: "title" %}
    {% for spec in ordered_specs %}
    <li><a href="{{ site.url }}/action/{{ spec.action | slugify  }}">{{ spec.title }}</a></li>
    {% endfor %}
</ul>
