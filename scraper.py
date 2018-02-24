#Import libraries
import json
import urllib2
from bs4 import BeautifulSoup

#specify the URL
urls = ['https://www.airbnb.co.uk/rooms/19278160?s=51','https://www.airbnb.co.uk/rooms/14531512?s=51','https://www.airbnb.co.uk/rooms/19292873?s=51']

#set headers so that the website thinks it is being accessed from a browser
hdr = headers={'User-Agent': 'Mozilla/5.0'}

#loop through urls
for url in urls:
	#request the site
	req = urllib2.Request(url, headers=hdr)

	#grab page content from url
	page = urllib2.urlopen(req) 

	#parse html
	pageContents = BeautifulSoup(page, 'html.parser')

	#get all scripts containing json
	JSONTexts = pageContents.findAll("script", type="application/json")

	#loop through scripts
	for JSONText in JSONTexts:
		#filter out json we are interested in
		if JSONText.get('data-hypernova-key') == "spaspabundlejs":
			#remove leading and trailing tags
			propInfoJSON = JSONText.next.replace('<!--','').replace('-->','')

	#parse text as json
	data = json.loads(propInfoJSON)

	#grab object we are interested in
	listingData = data["bootstrapData"]["reduxData"]["marketplacePdp"]["listingInfo"]["listing"]

	#print data
	print 'Property Name: \t\t' + listingData["name"]
	print 'Propert Type: \t\t' + listingData["room_and_property_type"]
	print 'No. of bedrooms: \t' + listingData["bedroom_label"]	
	print 'No. of bathrooms: \t' + listingData["bathroom_label"]
	print 'Amenities:'
	for amenity in listingData["listing_amenities"]:
		print "\t" + amenity["name"]

	if urls.index(url) != len(urls)-1:
		print '\n\n --------------------- \n\n'

