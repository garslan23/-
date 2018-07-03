# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 11:10:07 2018

@author: Lenovo
"""

import random

from PIL import Image




renk1=[[0,255,0,255],[255,0,255,0],[255,255,0,0],[0,0,255,255]]
renk2=[[255,0,255,0],[0,255,0,255],[0,0,255,255],[255,255,0,0]]
resim=Image.open("yazi.png")
resim=resim.convert("1")
alan1=Image.new("1",[boyut*2 for boyut in resim.size])
alan2=Image.new("1",[boyut*2 for boyut in resim.size])
for i in range(resim.size[0]):
    for j in range(resim.size[1]):
        pixel=resim.getpixel((i,j))
        sayi=round(random.random()*3)
        sayi=int(sayi)
        if pixel==255:
            alan1.putpixel((i*2,j*2),renk1[sayi][3])
            alan1.putpixel((i*2,j*2+1),renk1[sayi][2])
            alan1.putpixel((i*2+1,j*2),renk1[sayi][1])
            alan1.putpixel((i*2+1,j*2+1),renk1[sayi][0])
        
            alan2.putpixel((i*2,j*2),renk2[sayi][0])
            alan2.putpixel((i*2,j*2+1),renk2[sayi][1])
            alan2.putpixel((i*2+1,j*2),renk2[sayi][2])
            alan2.putpixel((i*2+1,j*2+1),renk2[sayi][3])
        else:
            alan1.putpixel((i*2,j*2),renk1[sayi][0])
            alan1.putpixel((i*2,j*2+1),renk1[sayi][1])
            alan1.putpixel((i*2+1,j*2),renk1[sayi][2])
            alan1.putpixel((i*2+1,j*2+1),renk1[sayi][3])
        
            alan2.putpixel((i*2,j*2),renk2[sayi][0])
            alan2.putpixel((i*2,j*2+1),renk2[sayi][1])
            alan2.putpixel((i*2+1,j*2),renk2[sayi][2])
            alan2.putpixel((i*2+1,j*2+1),renk2[sayi][3])
            
alan1.save('pay1.png')
alan2.save('pay2.png')
alan1.show()
alan2.show()

