from PIL import Image
import os

maps = [183]
zooms = xrange(10,14)
xs = xrange(0,50)
ys = xrange(0,50)

size =257

for m in maps :
	for z in zooms:
		stitch = "%s/%s.jpg" % (m,z)
		for x in xs:
			for y in ys:
				filename = "%s/%s/%s_%s.jpg" % (m,z,x,y)
				if os.path.exists(filename):	
					mx, my = x+1,y+1
					i = Image.open(filename)
					w,h = i.size
		sizex = (mx-1)*size+w
		sizey = (my-1)*size+h
		canvas = Image.new("RGB", (sizex, sizey), (255,255,255))
		
		for x in range(mx):
			for y in range(my):
				i = Image.open("%s/%s/%s_%s.jpg" % (m,z,x,y))
				if i.mode == "RGBA":
					canvas.paste(i, (x*size, y*size), i)
				else:
					canvas.paste(i, (x*size, y*size))		
		canvas.save(stitch, "jpeg")				
