---
layout: default
title: Photos
---

<ul class="posts">
    Mes photos :
    {% for page in site.pages %}
       {% if page.tags contains "photo" %}
           <li><a href="{{ page.url }}">{{ page.title }}</a></li>
       {% endif %}
    {% endfor %}
</ul>

![footer](/dl/photos/photoFooter.jpg)
