#importing pillow to the code
import os
import PIL as Pillow
from PIL import Image, ImageFilter
#importing specific filters
from PIL.ImageFilter import (CONTOUR)

#showing the original image before the filter is applied
beforeImage = Image.open('puppy.jpg')
beforeImage.show()

#the image after the blur filter is applied
blurredImage = beforeImage.filter(ImageFilter.BoxBlur(5))
blurredImage.show()

#image after it is rotated
rotatedImage = beforeImage.rotate(90)
rotatedImage.show()

#image contour filter applied
contouredImage = beforeImage.filter(CONTOUR)
contouredImage.show()