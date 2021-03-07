Pillow is used to edit images. This is the tutorial I used to learn how to navigate Pillow: https://www.tutorialspoint.com/python_pillow/python_pillow_quick_guide.htm
I used a picture of a puppy to test pillow. 

INSTALLING PILLOW:
First, I made sure that python had an environment variable path on my machine (does not work otherwise). 
Then, I went into the command prompt and typed in the following commands (pip is already installed with new python versions):
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow

Importing Pillow within the code:

#Here I imported Pillow itself, the image, and filters I will be using.#
import PIL as Pillow
from PIL import Image, ImageFilter
from PIL.ImageFilter import (CONTOUR)

#I uploaded the image here in its original state. It is in the same directory as my python file, so I did not need to include a specific path#
beforeImage = Image.open('puppy.jpg')
beforeImage.show()

Example1) Blurring a Photo
blurredImage = beforeImage.filter(ImageFilter.BoxBlur(5))
blurredImage.show()

Example2) Rotating a Photo
rotatedImage = beforeImage.rotate(90)
rotatedImage.show()

Example3) Adding a filter to the photo (contour)
contouredImage = beforeImage.filter(CONTOUR)
contouredImage.show()
