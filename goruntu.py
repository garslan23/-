# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 16:51:24 2018

@author: Lenovo
"""

from PIL import Image


resim1=Image.open('a.png')
resim2=Image.open('b.png')

ol_resim=Image.new('1',resim1.size)

for x in range(resim1.size[0]):
    for y in range(resim1.size[1]):
        ol_resim.putpixel((x,y),min(resim1.getpixel((x,y)),resim2.getpixel((x,y))))
ol_resim.save("ab.png")
ol_resim.show()
