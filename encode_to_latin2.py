# -*- coding: iso-8859-2 -*-
base_file_name = "validated_words_jav"
extension = "txt"

inputFile = open(base_file_name+"."+extension, 'rb')
inputFileLines = inputFile.readlines()

outputFile = open(base_file_name+"_lat2."+extension, "wb")#, encoding="iso-8859-2")

for line in inputFileLines:
	converted_string = line.decode('utf8')
	try :
		convert_to_byte = converted_string.encode('iso-8859-2')
	except UnicodeEncodeError:
		print(converted_string)
	outputFile.write(convert_to_byte)
