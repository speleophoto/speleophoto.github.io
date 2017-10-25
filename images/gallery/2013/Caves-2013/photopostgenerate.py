import yaml
import os

body_photopost='''
<figure style="">
<div id="photo" style="text-align: center;">
<img class="" src="{{ site.url }}/images/gallery/{{page.year}}/{{page.gallerytitle}}/{{page.filename}}" alt="{{page.description}}">
</div>
{% if page.title %}
<figcaption><p>{{page.title}}</p>{% if page.description!="None" %}{{page.description}}{% endif %}</figcaption>
{% endif %}
</figure>
'''


output_dir = './/photopost'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    
with open('images.yaml') as f:
    # use safe_load instead load
    dataMap = yaml.safe_load(f)
    images = dataMap['images']
    print images
    print '----------------'
    for i, img in enumerate(images):
        photopostfilename = '0000-01-01-photo_{0}.md'.format(img['filename']) 
        new_path = os.path.join(output_dir, photopostfilename)
        photopost_file = open(new_path,'w')
        photopost_file.write('---\n')
        photopost_file.write('layout: photopost\n')
        photopost_file.write('categories: photo\n')
        for key in img:
            photopost_file.write("{}: {}\n".format(key, img[key]))
        photopost_file.write('permalink: /:title/ # this is title from filename like photo_xxxxx.jpg\n') 
        if i>0:   
            photopost_file.write('prev_filename: {}\n'.format(images[i-1]['filename']))
        else:
            photopost_file.write('prev_filename: \n')
        try:
            photopost_file.write('next_filename: {}\n'.format(images[i+1]['filename']))
        except:
            photopost_file.write('next_filename: \n')
        photopost_file.write('---\n')
        #body

        photopost_file.write(body_photopost)
        photopost_file.close()
        print img
