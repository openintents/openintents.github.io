---
layout: page
show_meta: false
subheadline: "Explore and Download"
title: "OI Apps"
permalink: "/download/"
---
<ul style="list-style: none;">
    {% for app in site.apps %}
		{% if app.githubicon %}
		{% assign githubicon = app.githubicon %}
		{% elsif app.github %}
		{% assign github = app.github %}
		{% else }
		{% assign githubicon = app.ref %}
		{% endif %}
		<li><img src="https://raw.githubusercontent.com/openintents/{{ githubicon }}/master/promotion/icons/ic_launcher_{{githubicon}}_512.png" width="50" alt="{{ page.title | escape_once }}"/>
		<a href="{{ site.url }}/{{ app.ref}}">{{ app.title }}</a></li>
    {% endfor %}
</ul>
