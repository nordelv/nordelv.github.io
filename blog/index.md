---
layout: default
title: Blog
---

<ul class="posts">
    Mes articles de blog :
    {% for post in site.posts %}
       {% if post.tags contains "blog" %}
           <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ post.url }}">{{ post.title }}</a></li>
       {% endif %}
    {% endfor %}
</ul>
