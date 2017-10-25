---
layout: post
title: summer 2007
date: 2007-06-01 10:00:00
categories: photogallery
year: 2007
author: Pablo Bo.
images:
  - filename: r001-017p.jpg
    author: Pablo Bo.
    license: CC-BY-NC-ND
    title: Holodnaya entrance
    description: Holodnaya entrance
    date: 2007-06-10
    camera: FED-5V
    lens: Industar 61 L/D
    ISO: Kodak profoto 100
    fnumber: f/4
    exposure: 1/60
    focal_length: 55mm
  - filename: r001-025p.jpg
    author: Pablo Bo.
    license: CC-BY-NC-ND
    title: Obvalnaya cave 1
    description: 
    date: 2007-06-10
    camera: FED-5V
    lens: Industar 61 L/D
    ISO: Kodak profoto 100
    fnumber: f/8
    exposure: 40sec
    focal_length: 55mm
  - filename: r001-026p.jpg
    author: Pablo Bo.
    license: CC-BY-NC-ND
    title: Obvalnaya cave 2
    description: 
    date: 2007-06-10
    camera: FED-5V
    lens: Industar 61 L/D
    ISO: Kodak profoto 100
    fnumber: f/8
    exposure: 50sec
    focal_length: 55mm
---

{% for image in page.images %}
[![{{ image.title }}]({{ site.url }}/images/gallery/{{ page.year }}/{{ page.title }}/thumb/thumb_{{ image.filename }}  "{{ image.title }}" )]({{ site.url }}/photo_{{image.filename}}){:class="img-responsive"}{% endfor %}
<!--more-->  
