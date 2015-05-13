---
layout: page
show_meta: false
subheadline: "Intents Table"
title: "See all intents"
teaser: "These are all the possibilities to save your time and delegate to other apps."
header:
   image_fullwidth: "header_unsplash_5.jpg"
permalink: "/intentstable/"
---
<ul>
    {% for spec in site.intent_specs %}
    <li><a href="{{ site.url }}/action/{{ spec.action }}">{{ spec.action }}</a></li>
    {% endfor %}
</ul>