#importing pillow to the code
import os
import PIL as Pillow
from PIL import Image, ImageFilter, ImageDraw, ImageFont

#Collecting user input
text = input('Enter what the text you want on the photo: ')

im = Image.open('puppy.jpg')
width, height = im.size 

#words on picture
draw = ImageDraw.Draw(im)
font = ImageFont.truetype('arial.ttf', 36)
textwidth, textheight = draw.textsize(text, font)

#calculating x,y coordinates
margin = 10
x = width - textwidth - margin
y = height - textwidth - margin

#drawing words on picture and appying filter
draw.text((x,y), text, font=font)

#showing the image
im.show()

