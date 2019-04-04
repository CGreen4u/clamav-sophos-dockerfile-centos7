#configuration.py


#destinations
def destination():
	#source location of files - needs to be a string
	dest1 = '//home//cgreen//Decryption//Encrypted'
	#decrypted files - needs to be a string
	dest2 = '//home//cgreen//Decryption//decrypted'
	#shared_drive - needs to be a string
	dest3 = '//home//cgreen//Decryption//Json//shared-drive1'
	#quarantine - needs to be a string
	dest4 = '//home//cgreen//Decryption//Json//virus'
	return dest1, dest2, dest3, dest4

def destination2():
	#sophos directories cannot have forward slashes before the first directory
	#location to scan for virus - same as dest1
       dest5 = 'home//cgreen//Decryption//Encrypted'
	#quarantine
	dest6 = 'home//cgreen//Decryption//Json//virus'
	return dest5, dest6

def location():
	#Final Location of files
	#shared directory location 
	file_location1  = 'No malware found. files ziped and sent to shared directory'
	#Quarantine location
	file_location2 = 'Malware found. Some of your files have been Quarantined'
	return file_location1, file_location2
