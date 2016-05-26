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

header ='\n<section class="row">\n'
footer = '</section>'
imgInsert = '<div class="thumbnails col-xs-6 col-sm-4 col-md-4" id="{}" onclick="showBig(\'#\'+id)>\n  <img src="/photos/{}/{}" class="img-rounded">\n</div>\n'


page.write(header)
for photoName in pics:
    page.write(imgInsert.format(photoName,name, photoName))
page.write(footer)
page.close()

'''
# Adding a link to the pics in the blog post, if this post exists
filesBlog = os.listdir('../_posts')
if (name+'.md') in filesBlog or (name+'.html') in filesBlog:
    page = open('../_posts/'+name+'.md','a')
    page.write('\n<hr>\n<p>Cliquez sur une photo pour acc\xc3\xa9der \xc3\xa0 toutes les photos</p>')
    page.write(header)
    i = 0
    while i<3 and i<len(pics):
        #insert 3 pics
        page.write(imgInsert.format('/photos/'+name+'-photos.html', \
                                    name, pics[i]))
        i+=1
    page.write(footer)
    page.close()
'''
