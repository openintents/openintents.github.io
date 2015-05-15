---
layout: page
show_meta: false
subheadline: "Intents Registry"
title: "See All Intents"
teaser: "These are all the possibilities to save your time and delegate to other apps."
permalink: "/intentsregistry/"
---
<a href="https://github.com/openintents/openintents.github.io/blob/master/README.md#intent-specification-for-writers">Add a new intent protocol via Github.</a>
<ul>
    {% assign ordered_specs = site.intent_specs | where: "component", "activity" | sort: "title" %}
    {% for spec in ordered_specs %}
    <li><a href="{{ site.url }}/action/{{ spec.action | slugify  }}">{{ spec.title }}</a> <br/><small>({{spec.action}})</small></li>
    {% endfor %}
</ul>
<a href="https://developer.android.com/guide/components/intents-common.html">Read also Google's documentation about commen intents.</a>

