import sys

class printProperty:
	''' Class to print property information to the console '''

	def __init__(self, propertyInfo):
		''' Set class attribute to given property info '''
		self.__propertyInfo = propertyInfo
	
	def printName(self):
		''' Print formatted name of property '''
		print('Property Name: \t\t' + self.__propertyInfo.name)

	def printPropertyType(self):
		''' Print formatted property type '''
		print ('Property Type: \t\t' + self.__propertyInfo.propertyType)

	def printBedrooms(self):
		''' Print formatted bedroom information for property '''
		print ('No. of bedrooms: \t' + self.__propertyInfo.bedroomLabel)

	def printBathrooms(self):
		''' Print formatted bathroom information for property '''
		print ('No. of bathrooms: \t' + self.__propertyInfo.bathroomLabel)

	def printAmenities(self):
		''' Print formatted list of amenities for property '''
		print ('Amenities:')

		for amenity in self.__propertyInfo.amenities:
			print ('\t' + amenity["name"])

	def printAll(self):
		''' Print all formatted info for property '''
		self.printName()
		self.printPropertyType()
		self.printBedrooms()
		self.printBathrooms()
		self.printAmenities()

	__propertyInfo = ''


class writeProperty:
	''' Class to write property information to a file '''
	def __init__(self, propertyInfo, folder):
		''' Set class attribute to given property info '''
		filepath = folder + '/' + propertyInfo.name.rstrip('.') + '.txt'
		self.__propertyInfo = propertyInfo
		
		try:
			self.file = open(filepath, 'w')
		except IOError:
			print('Could not create file at \'' + filepath + '\'')
			sys.exit(20)
		
	def writeName(self):
		''' Print formatted name of property '''
		self.file.write('Property Name: \t\t' + self.__propertyInfo.name + '\n')

	def writePropertyType(self):
		''' Print formatted property type '''
		self.file.write('Propert Type: \t\t' + self.__propertyInfo.propertyType + '\n')

	def writeBedrooms(self):
		''' Print formatted bedroom information for property '''
		self.file.write('No. of bedrooms: \t' + self.__propertyInfo.bedroomLabel + '\n')

	def writeBathrooms(self):
		''' Print formatted bathroom information for property '''
		self.file.write('No. of bathrooms: \t' + self.__propertyInfo.bathroomLabel + '\n')

	def writeAmenities(self):
		''' Print formatted list of amenities for property '''
		self.file.write('Amenities:' + '\n')

		for amenity in self.__propertyInfo.amenities:
			self.file.write('\t' + amenity["name"] + '\n')

	def writeAll(self):
		''' Print all formatted info for property '''
		self.writeName()
		self.writePropertyType()
		self.writeBedrooms()
		self.writeBathrooms()
		self.writeAmenities()

		# Print message to inform user of progress
		print('Finished writing data to ' + self.file.name)

		# Define private 
		__propertyInfo = ''
		__file = ''