# AirbnbScraper

Program to return information about Airbnb properties

Program has been designed to refer to URLs stored in a properties file at:

	properties/propertyURLs.properties

All AirBNB property URLs must be stored in this file

## Run program

Once properties file has been setup run
	
	scraper.py

Program is set up to return all property information for all URLs to files found in:

	properties/<property name>.txt

### Print to console

If you wish to print the property information to the console please use the printProperty class in AirBNBOutput. You can either print the property name, type, number of bedroom, number of bathrooms or list of amenities, or all attributes

### Write to file

If you wish to write the property information to a file please use the writeProperty class in AirBNBOutput. A text file will be created with the same name as the property. You can either write the property name, type, number of bedroom, number of bathrooms or list of amenities, or all attributes to the file.
