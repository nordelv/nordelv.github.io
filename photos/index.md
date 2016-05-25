---
layout: default
title: Photos
---

<ul class="posts">
    Mes photos :
    {% for page in site.pages %}
       {% if page.tags contains "photo" %}
           <li><span>{{ post.date | date_to_string }}</span> &raquo; <a          href="{{ post.url }}">{{ post.title }}</a></li>
       {% endif %}
    {% endfor %}
</ul>
