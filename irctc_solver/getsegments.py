from PIL import Image
import hashlib
import time
import sys

args = sys.argv[1:]
if not args:
    print "Dude atleast give me the image";
    sys.exit(1)

for filename in args:
    im = Image.open(filename)
    if filename.endswith('.png'):
        print "It is a PNG File"
        bg = Image.new("RGB",im.size,(255,255,255))
        bg.paste(im,im)
        bg.save("lol.jpg")
        im = Image.open("lol.jpg")
    im2 = Image.new("P",im.size,255)
    im = im.convert("P")

    temp = {}


    for x in range(im.size[1]):
      for y in range(im.size[0]):
        pix = im.getpixel((y,x))
        temp[pix] = pix
        if pix == 0 or pix < 200: # these are the numbers to get
          im2.putpixel((y,x),0)

    count = 0
    for i in im.histogram():
      print count,i
      count += 1
    im2.save("output.gif")


    inletter = False
    foundletter=False
    start = 0
    end = 0

    letters = []


    for y in range(im2.size[0]): # slice across
      for x in range(im2.size[1]): # slice down
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

    count = 0
    for letter in letters:
      m = hashlib.md5()
      im3 = im2.crop(( letter[0] , 0, letter[1],im2.size[1] ))
      m.update("%s%s"%(time.time(),count))
      im3.save("./SEGMENTS/%s.gif"%(m.hexdigest()))
      count += 1
