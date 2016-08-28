from PIL import Image


im = Image.open("0.png")
bg = Image.new("RGB",im.size,(255,255,255))
bg.paste(im,im)
bg.save("loltest.jpg")
im = Image.open("loltest.jpg")
im = im.convert("P") #256 pallette may convert

im2 = Image.new("P",im.size,255)
im = im.convert("P")


temp = {}

for x in range(im.size[1]):
  for y in range(im.size[0]):
    pix = im.getpixel((y,x))
    temp[pix] = pix
    if pix > 100 or pix == 227: # these are the numbers to get
      im2.putpixel((y,x),0)


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

print letters

