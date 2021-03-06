# -*- coding: utf-8 -*-
"""image-to-ascii.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1feQ4WEdl8RLfmPLZOHZDhB27IZLjF4j7

modified from https://github.com/kiteco/python-youtube-code/blob/master/ascii/ascii_convert.py

This uses amount of 'ink' in each letter for light value.
"""

import PIL.Image

name = 'name'
size = 500

# get array with letter brightness organization
name = [char for char in name]
letter_value = {' ': 0, 'a': 0.461, 'b': 0.463, 'c': 0.400, 'd': 0.541, 'e': 0.481, 'f': 0.462, 'g': 0.592, 'h': 0.491, 'i': 0.336, 'j': 0.445, 'k': 0.518, 'l': 0.354, 'm': 0.590, 'n': 0.436, 'o': 0.420, 'p': 0.572, 'q': 0.545, 'r': 0.372, 's': 0.467, 't': 0.354, 'u': 0.468, 'v': 0.360, 'w': 0.492, 'x': 0.469, 'y': 0.432, 'z': 0.461}

rname = []
for i in name:
  if i not in rname and i != " ":
    rname.append(i.lower())
name = rname

n = len(name)
for i in range(n):
  for j in range(0, n-i-1):
    if letter_value[name[j]] > letter_value[name[j + 1]]:
      name[j], name[j+1] = name[j+1], name[j]
print(name)

# resize
def resize_image(image, new_width=size):
  width, height = image.size
  ratio = height / width
  new_height = int(new_width * ratio)
  resized_image = image.resize((new_width, new_height))
  return(resized_image)

# gray
def gray(image):
  grayscale_image = image.convert("L")
  return(grayscale_image)

# subtract 1 from (len(name) incase this doesn't work. I have no idea why that fixes it. If you don't get all the letters, remove the subtraction
import math
def pixels_assciified(image):
  global name
  pixels = image.getdata()
  maxed = max(pixels)
  chars = ""
  try:
    chars = "".join([name[pixel // (maxed // (len(name)))] for pixel in pixels])
  except:
    # name.append(name[-1])
    chars = "".join([name[pixel // (maxed // (len(name) -1))] for pixel in pixels])
  return(chars)

path = "drive/MyDrive/imgs/IMG_3534.JPEG"
image = PIL.Image.open(path).convert('L')

new_image_data = pixels_assciified(gray(resize_image(image)))
pixel_count = len(new_image_data)
final_ascii = "\n".join(new_image_data[i:(i+size)] for i in range(0,pixel_count,size))
print(final_ascii)