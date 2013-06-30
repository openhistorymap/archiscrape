import urllib2
import os

maps = xrange(1,280)
#maps = [183]
zoom = xrange(10,15)
xs = xrange(0,50)
ys = xrange(0,50)

url = "http://badigit.comune.bologna.it/mappe/%s/GeneratedImages/dzc_output_files/%s/%s_%s.jpg"
y_exit = False
x_exit = False
for m in maps:
	print "getting map",m
	for z in zoom:
		print 'getting zoom', z
		x_exit = False
		for x in xs:
			y_exit = False
			if not x_exit:
				for y in ys:
					if not y_exit:
						try:
							local = url % (m,z,x,y)
							u = urllib2.urlopen(local)
							if not os.path.exists("%s" % m):
								os.makedirs("%s" % m)
							if not os.path.exists("%s/%s" %(m,z)):
								os.makedirs("%s/%s" % (m,z))
							saver = open("%s/%s/%s_%s.jpg" % (m,z, x,y), 'w')
							saver.write(u.read())
							saver.close()
							print "got", x,y
							print "done"
							x_fail = 0
						except:	
							print "not available"
							y_exit = True
							x_fail = x_fail + 1 
							if x_fail > 3:
								x_exit = True
					if x_exit:
						continue
						
