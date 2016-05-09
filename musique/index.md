---
layout: default
title: Mes musiques
---

Cette page est vide pour l'instant...

liste des musiques :

{{ site.page }}

{% for post in site.pages %}
  {% if post.tags == ['musique'] %}
   {{ post.date | date_to_string }} &raquo;[{{ post.title }}]({{ post.url }})
  {% endif %}
{% endfor %}

