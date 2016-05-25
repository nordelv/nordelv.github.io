#! /usr/bin/env python

import sys
import os


name = sys.argv[1]
#name of the post which will contain the pics, without extension
#same name as the blog post (if blog post)
#with the date
#finale name will be name + '-photos'
dirPics = os.listdir('.')
if name not in dirPics:
    raise NameError(name+'/ directory doesn\'t exist')

pics = os.listdir(name+'/')
pics.sort()

page = open(name+'-photos.md', 'a')

header ='<section class="row">\n'
footer = '</section>'
imgInsert = '<div class="col-xs-4 col-sm-3 col-md-2 ">\n  <a href="#" class="thumbnail">\n    <img src="/photos/{}/{}" class="img-rounded">\n  </a>\n</div>\n'


page.write(header)
for photoName in pics:
    page.write(imgInsert.format(name, photoName))
page.write(footer)
page.close()
