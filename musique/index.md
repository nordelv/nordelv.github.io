---
layout: default
title: Mes musiques
---

<ul class="posts">
    Articles publiés :
    {% for post in site.posts %}
       {% if post.tags contains "musique" %}
           <li><span>{{ post.date | date_to_string }}</span> &raquo; <a          href="{{ post.url }}">{{ post.title }}</a></li>
       {% endif %}
    {% endfor %}
</ul>
