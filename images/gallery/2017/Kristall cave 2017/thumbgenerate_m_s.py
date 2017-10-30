import os
from PIL import Image
import exifread


gallerytitle = raw_input('Gallery name?:')
galleryyear = raw_input('Gallery year?:')


yaml_header = '''---
layout: post
title: {tit}
date:
categories: photogallery
year: {yea}
author: Pablo Bo.
---
'''.format(tit = gallerytitle, yea = galleryyear)
yaml_body = '''
<div id="{{ page.title | slugify }}" >
{% for image in page.images %}
<a class="img-responsive" href="{{ site.url }}/photo_{{image.filename}}">
<img class="img-responsive" src="{{ site.url }}/images/gallery/{{ page.year }}/{{ page.title }}/thumb/thumb_{{ image.filename }}" alt="{{ image.title}}">
</a>
{% endfor %}
</div>
<!-- bower:js -->
<script src="{{ site.url }}/dist_jg/js/jquery.js"></script>
<script src="{{ site.url }}/dist_jg/js/jquery.justifiedGallery.js"></script>
<!-- endbower -->
<script>
$("#{{ page.title | slugify }}").justifiedGallery({rowHeight: 220, lastRow: 'nojustify', margins: 2});
</script>
<!--more-->
'''
output_dir_m = './/thumb'
#output_dir_s = './/thumb_s'
thumbnail_size_m = (400,400)
#thumbnail_size_s = (400,400)

input_path = ".//"

yaml_gall_file = open('gall.yaml','w') 
yaml_img_file = open('images.yaml','w') 

yaml_gall_file.write(yaml_header)
yaml_gall_file.write(yaml_body)
yaml_img_file.write('images:\n')


if not os.path.exists(output_dir_m):
    os.makedirs(output_dir_m)

#if not os.path.exists(output_dir_s):
#    os.makedirs(output_dir_s)
    

    
    
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(input_path) if isfile(join(input_path, f))]
for f in onlyfiles:
	print f
	full_path = os.path.join(input_path, f)
	if f.endswith(".jpg") or f.endswith(".JPG"):
            filename = 'thumb_{0}'.format(f) 
            new_path = os.path.join(output_dir_m, filename)
            if os.path.exists(new_path):
                os.remove(new_path)
            im = Image.open(full_path)
            im.thumbnail(thumbnail_size_m)
            im.save(new_path, "JPEG")
            
            #filename = 'thumb_s_{0}'.format(f) 
            #new_path = os.path.join(output_dir_s, filename)
            #if os.path.exists(new_path):
                #os.remove(new_path)
            #im = Image.open(full_path)
            #im.thumbnail(thumbnail_size_s)
            #im.save(new_path, "JPEG")
            
            #read exif
            f_exif = open(full_path, 'rb')
            # Return Exif tags
            tags = exifread.process_file(f_exif)
            ex_camera = str(tags['Image Model'])
            ex_focal = str(tags['EXIF FocalLength'])+'mm'
            ex_ISO = str(tags['EXIF ISOSpeedRatings'])
            ex_exposure = str(tags['EXIF ExposureTime'])+'sec'
            #ex_Fnumb =tags['EXIF FNumber']
            fnum = tags['EXIF FNumber']
            ex_fnum = 'f/'+str(eval(str(fnum)+'.0'))
            
            
            yaml_img_file.write("  - filename: "+str(f)+'\n')
            yaml_img_file.write("    author: "+'Pablo Bo.\n')
            yaml_img_file.write("    license: "+'CC-BY-NC-ND\n')
            yaml_img_file.write("    title: "+'\n')
            yaml_img_file.write("    gallerytitle: "+gallerytitle+'\n')
            yaml_img_file.write("    description: "+'\n')
            yaml_img_file.write("    date: "+'\n')
            yaml_img_file.write("    year: "+galleryyear+'\n')
            yaml_img_file.write("    camera: "+ex_camera+'\n')
            yaml_img_file.write("    lens: "+'\n')
            yaml_img_file.write("    ISO: "+ex_ISO+'\n')
            yaml_img_file.write("    fnumber: "+ex_fnum+'\n')
            yaml_img_file.write("    exposure: "+ex_exposure+'\n')
            yaml_img_file.write("    focal_length: "+ex_focal+'\n')
            
yaml_gall_file.close()
yaml_img_file.close()
print '---------------'



