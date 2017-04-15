---
layout: page
show_meta: false
subheadline: "Explore and Download"
title: "OI Apps"
permalink: "/download/"
---
<ul style="list-style: none;">
    {% for app in site.apps %}
		{% if app.github %}
		{% assign github = {{app.github}} %}
		{% else %}
		{% assign github = {{app.ref}} %}
		{% endif %}
		<li><img src="https://raw.githubusercontent.com/openintents/{{ github }}/master/promotion/icons/ic_launcher_{{github}}_512.png" width="50" alt="{{ page.title | escape_once }}"/>
		<a href="{{ site.url }}/{{ app.ref}}">{{ app.title }}</a></li>
    {% endfor %}
</ul>
