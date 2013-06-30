import urllib2

import os


url = "http://badigit.comune.bologna.it/books/%s/big/%03d.jpg"
books = [
'dolfi',
'B4362',
'zanti',
]

pages = xrange(1, 1000)



for book in books:
	has_pages = True
	for page in pages:
		if has_pages:
			try: 
				uurl = url % (book, page)
				print uurl
				u = urllib2.urlopen(uurl)
				if not os.path.exists("%s" % book):
					os.makedirs("%s" % book)
				f = open("%s/%s.jpg" % (book, page), "w")
				f.write(u.read())
				f.close()
			except:
				has_pages = False
		else:
			continue
