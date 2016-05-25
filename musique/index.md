---
layout: default
title: Mes musiques
---

Articles publiés :

{% for post in site.posts %}
    {% if site.posts.categories contains "musique" %}
        *{{ post.date | date_to_string }} &raquo; [{{ post.title }}]({{ post.url }})
    {% endif %}
{% endfor %}

---------

{% for post in site.posts %}
    {{ site.posts.categories }}
{% endfor %}
