---
layout: post
title: summer 2007
date: 2007-01-01
categories: photogallery
year: 2007
author: Pablo Bo.
images:
  - filename: r001-017p.jpg
    author: Pablo Bo.
    license: CC-BY-NC-ND
    title: Holodnaya entrance
    gallerytitle: summer 2007
    description: Holodnaya entrance
    date: 2007-03-15
    year: 2007
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
    gallerytitle: summer 2007
    description: Obvalnaya cave 1
    date: 2007-03-15
    year: 2007
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
    gallerytitle: summer 2007
    description: Obvalnaya cave 2
    date: 2007-03-15
    year: 2007
    camera: FED-5V
    lens: Industar 61 L/D
    ISO: Kodak profoto 100
    fnumber: f/8
    exposure: 50sec
    focal_length: 55mm
  - filename: r001-017p.jpg
    author: Pablo Bo.
    license: CC-BY-NC-ND
    title: Holodnaya entrance
    gallerytitle: summer 2007
    description: Holodnaya entrance 2
    date: 2007-03-15
    year: 2007
    camera: FED-5V
    lens: Industar 61 L/D
    ISO: Kodak profoto 100
    fnumber: f/4
    exposure: 1/60
    focal_length: 55mm
---


<div style="vertical-align: middle">{% for image in page.images %}
    <a class="img-responsive" href="{{ site.url }}/photo_{{image.filename}}"><figure class="fig-responsive">
        <img class="img-responsive" src="{{ site.url }}/images/gallery/{{ page.year }}/{{ page.title }}/thumb/thumb_{{ image.filename }}" alt="dsds">
    {% if image.title %}
        <figcaption>{{image.title}}</figcaption>
    {% endif %}
        </figure></a>
    {% endfor %}</div>
