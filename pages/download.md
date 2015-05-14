---
layout: page
show_meta: false
subheadline: "Explore and Download"
title: "OI Apps"
header:
   image_fullwidth: "header_unsplash_5.jpg"
permalink: "/download/"
---
<ul style="list-style: none;">
    {% for app in site.apps %}
    <li><img src="https://raw.githubusercontent.com/openintents/{{ app.ref }}/master/promotion/icons/ic_launcher_{{app.ref}}_512.png" width="50" alt="{{ page.title escape_once }}"/> <a href="{{ site.url }}/{{ app.ref}}">{{ app.title }}</a></li>
    {% endfor %}
</ul>