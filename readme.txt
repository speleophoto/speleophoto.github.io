Create YAML sequences (arrays) for your images in the post's front matter like this:

  image:
    - url: path/to/image
      caption: 'A photo from my trip to [the solar farm](http://example.com).'
      alt: 'alt text'
    - url: path/to/another-image
      caption: 'Another photo from my trip.' 
      alt: 'more alt text'



Make sure to have an image host specified in the _config.yml file. Example:

image_url: http://static.example.com/images

Assuming that all image URLs are all hosted from the same source, the image URL for the site leads the post's image file name like this: {{ site.image_url }}/{{ page.image[3].url }} 


The integer value that you pick determines which image (and alt and caption) will be picked from the YAML sequence. Starting at 0 and counting through the sequence, this index value refers to the front matter.
