import json
import requests
from bs4 import BeautifulSoup

class propertyInfo:

	def __init__(self, url):
		''' extract JSON from given URL and set class attributes '''
		propJSON = self.__getJSONfromURL(url)

		self.name = propJSON["name"]
		self.propertyType = propJSON["room_and_property_type"]
		self.bedroomLabel = propJSON["bedroom_label"]
		self.bathroomLabel = propJSON["bathroom_label"]
		self.amenities = propJSON["listing_amenities"]

    
	def __getJSONfromURL(self, url):
		''' Return a JSON object of useful property details from the given url. '''
		#grab page content from url
		page = requests.get(url)

		#parse html
		pageContents = BeautifulSoup(page.content, 'html.parser')

		#get all scripts containing json
		JSONTexts = pageContents.findAll("script", type="application/json")

		#loop through scripts
		for JSONText in JSONTexts:
			#filter out json we are interested in
			if JSONText.get('data-hypernova-key') == "spaspabundlejs":
				#remove leading and trailing tags and troublesome unicode characters
				propInfoJSON = JSONText.next.replace('<!--','').replace('-->','').replace( u'\u2018', u"'").replace( u'\u2019', u"'")

		#parse text as json
		data = json.loads(propInfoJSON)

		#grab object we are interested in
		return data["bootstrapData"]["reduxData"]["marketplacePdp"]["listingInfo"]["listing"]
