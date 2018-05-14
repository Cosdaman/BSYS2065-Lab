import cImage as image
img = image.Image("testimage.gif")

newimg = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin()

for col in range(img.getWidth()):
    for row in range(img.getHeight()):
        p = img.getPixel(col, row)

        red = int(p.getRed()/3)
        green = int(p.getGreen()/3)
        blue = int(p.getBlue()/3)

        newpixel = image.Pixel(red, green, blue)

        newimg.setPixel(col, row, newpixel)

newimg.draw(win)
win.exitonclick()
