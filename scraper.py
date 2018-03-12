import sys
import AirBNBScraper
import AirBNBOutput

# Define folder, file and path for program to use
folder = 'properties'
file = 'propertyURLs.properties'
filepath = folder + '/' + file

try:
  	
  	# Open file and loop through urls
	with open(filepath) as urls:  
	    for url in urls:

	    	# Get property info from url
		    propertyInfo = AirBNBScraper.propertyInfo(url)

			# Write all property info to file
		    AirBNBOutput.writeProperty(propertyInfo, folder).writeAll()

except IOError:
	print('File at \'' + filepath + '\' could not be found')
	sys.exit(10)
