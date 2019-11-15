---
layout: page
show_meta: false
subheadline: "Explore and Download"
title: "OI Apps"
permalink: "/download/"
---
<ul style="list-style: none; line-height:1; margin-bottom:1em">
    {% for app in site.apps %}
		{% if app.githubicon %}
		{% assign ghicon = app.githubicon %}
		{% elsif app.github %}
		{% assign ghicon = app.github %}
		{% else %}
		{% assign ghicon = app.ref %}
		{% endif %}
		<li><img src="https://raw.githubusercontent.com/openintents/{{ ghicon }}/master/promotion/icons/ic_launcher_{{ghicon}}_512.png" width="50" alt="{{ page.title | escape_once }}"/>
		<a href="{{ site.url }}/{{ app.ref}}">{{ app.title }}</a><br/>
		<small>{{ app.teaser }}</small>
		{% if app.web_only %}
		<!--web only-->
		{% else %}
		<img src="https://raw.githubusercontent.com/openintents/openintents.github.io/master/images/android.png" height="10" alt="Android"/>
		{% endif %}
		{% if app.domain %}
		<img src="https://raw.githubusercontent.com/openintents/openintents.github.io/master/images/blockstack.png" height="10" alt="Blockstack"/>
		{% endif %}
		</li>
    {% endfor %}
</ul>
