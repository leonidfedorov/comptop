import math
from PIL import Image

imgx = 800
imgy = 600
image = Image.new("RGB", (imgx, imgy))

metric = lambda x, y: math.sqrt(x**2 + y**2) 

def Voronoi(nx, ny, nr, ng, nb):
  for y in range(imgy):
      for x in range(imgx):
          dmin = metric(imgx - 1, imgy - 1)
          j = -1
          for i in range(n):
              d = metric(nx[i]-x, ny[i]-y)
              if d < dmin:
                  dmin = d
                  j = i
          
          image.putpixel((x, y), (nr[j], ng[j], nb[j]))

for i in range(n):
    image.putpixel((nx[i], ny[i]),(255 - nr[i], 255 - ng[i], 255 - nb[i]))

image.save("Voronoi.png", "PNG")
