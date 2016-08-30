from PIL import Image
from operator import itemgetter
import hashlib
import time
import sys

def main():
    args = sys.argv[1:]

    if not args:
        print "Dude atleast give me the image";
        sys.exit(1)

    for filename in args:
        im = Image.open(filename)
        bg = Image.new("RGB",im.size,(255,255,255))
        bg.paste(im,im)
        bg.save("lol.jpg")
        im = Image.open("lol.jpg")
        im = im.convert("P") #256 pallette convert
        show_histogram(im)
        im2 = create_image_to_parse(im)
        segment_coordinates(im2)

def show_histogram(im):
    his = im.histogram()

    values = {}

    for i in range(256):
      values[i] = his[i]

    for j,k in sorted(values.items(), key=itemgetter(1), reverse=True)[:10]:
      print "Color is %d Frequency is %d"%(j,k)



def create_image_to_parse(im):
    im2 = Image.new("P",im.size,255)
    im = im.convert("P")
    temp = {}

    for x in range(im.size[1]):
      for y in range(im.size[0]):
        pix = im.getpixel((y,x))
        temp[pix] = pix
        if pix == 0 or pix == 96:
          im2.putpixel((y,x),0)
    return im2

def segment_coordinates(im2):
    inletter = False
    foundletter=False
    start = 0
    end = 0

    letters = []
    print "Width is %d"%im2.size[0]
    print "Height is %d"%im2.size[1]

    for y in range(im2.size[0]):
      for x in range(im2.size[1]):
        pix = im2.getpixel((y,x))
        if pix != 255:
          inletter = True

      if foundletter == False and inletter == True:
        foundletter = True
        start = y

      if foundletter == True and inletter == False:
        foundletter = False
        end = y
        letters.append((start,end))

      inletter=False
    print letters

    count = 0
    for letter in letters:
      m = hashlib.md5()
      im3 = im2.crop(( letter[0] , 0, letter[1],im2.size[1] ))
      m.update("%s%s"%(time.time(),count))
      im3.save("./CUTS/%s.gif"%(m.hexdigest()))
      count += 1

if __name__ == '__main__':
  main()
