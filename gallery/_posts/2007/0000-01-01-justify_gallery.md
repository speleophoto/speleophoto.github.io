---
layout: post
title: Chatyr-Dag
date: 2007-03-15
categories: photogallery
year: 2007
author: Pablo Bo.
excerpt_separator: <!--more-->
images:
  - filename: r001-017p.jpg
    author: Pablo Bo.
    license: CC-BY-NC-ND
    title: Holodnaya entrance
    gallerytitle: Chatyr-Dag
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
    gallerytitle: Chatyr-Dag
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
    gallerytitle: Chatyr-Dag
    description: Obvalnaya cave 2
    date: 2007-03-15
    year: 2007
    camera: FED-5V
    lens: Industar 61 L/D
    ISO: Kodak profoto 100
    fnumber: f/8
    exposure: 50sec
    focal_length: 55mm
---
<div id="gallery" >
{% for image in page.images %}
<a class="img-responsive" href="{{ site.url }}/photo_{{image.filename}}">
<img class="img-responsive" src="{{ site.url }}/images/gallery/{{ page.year }}/{{ page.title }}/thumb/thumb_{{ image.filename }}" alt="{{ image.description}}">
</a>

{% endfor %}
</div>
<!-- bower:js -->
<script src="{{ site.url }}/dist_jg/js/jquery.js"></script>
<script src="{{ site.url }}/dist_jg/js/jquery.justifiedGallery.js"></script>
<!-- endbower -->
<script>
$("#gallery").justifiedGallery({rowHeight: 220, lastRow: 'nojustify', margins: 2});
</script>
<!--more-->
