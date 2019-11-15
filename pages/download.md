---
layout: page
show_meta: false
subheadline: "Explore and Download"
title: "OI Apps"
permalink: "/download/"
---
<ul style="list-style: none;">
    {% for app in site.apps %}
		<!-- 1:{{app.githubicon}} 2:app.github 3:app.ref -->
		{% if app.githubicon %}
		{% assign ghicon = app.githubicon %}
		{% elsif app.github %}
		{% assign ghicon = app.github %}
		{% else %}
		{% assign ghicon = app.ref %}
		{% endif %}
		<li><img src="https://raw.githubusercontent.com/openintents/{{ ghicon }}/master/promotion/icons/ic_launcher_{{ghicon}}_512.png" width="50" alt="{{ page.title | escape_once }}"/>
		<a href="{{ site.url }}/{{ app.ref}}">{{ app.title }}</a></li>
    {% endfor %}
</ul>
