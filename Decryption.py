import gnupg
import os
import shutil
import configuration as cf

class Decryption:

    def __init__(self, filename, public_keyring, filepath, passphrase):
        self.filename = filename
        self.filepath = filepath
        self.public_keyring = public_keyring
        self.passphrase = passphrase
    def makeDir(self):
        dest1, dest2, dest3, dest4 = cf.destination()
        if os.path.exists(dest1):
            print("Decrypted directory already exists")
        else:
            os.mkdir(dest1)
            print("Created decrypted directory")

        #this is important if this is not correct the program will  run in the folder it is launched within
        os.chdir(dest1)
    def Decrypt(self, filename, public_key, filepath, passphrase):
        dest1, dest2, dest3, dest4 = cf.destination()
        #the location of the files and the keys pulled from postgres are here as well.  
        gpg = gnupg.GPG(gnupghome=(str(filepath)))
        #gpg = gnupg.GPG(homedir=(str(filepath), keyring= (str(public_keyring))))
                                        #secring= (str(secret_keyring)))

    
        #create list
        files_dir = []
        files_dir_clean = []

        #create seperate path for decryped files to be seperate from encryped files
        if os.path.exists(dest2):
            print("Decrypted directory already exists")
        else:
            os.mkdir(dest2)
            print("Created decrypted directory")
        
        #add files to list (list the uuid for the folder to pick) name of file from kafka
        files = [f for f in os.listdir(dest1) if os.path.isfile(f)]
        for f in files:
            files_dir.append(f)

        #remove the .gpg from the extention.  
        for x in files_dir:
            length = len(x)
            endLoc = length - 4
            clean_file = x[0:endLoc]
            files_dir_clean.append(clean_file)


        #Decrypion starts here.  Be sure the passphrase is properly named. and the files is converted into a string 
        for x in files_dir:
                with open(str(filepath) + "/" + str(filename), 'rb') as f:
                        status = gpg.decrypt_file(f, passphrase= str(passphrase), output=files_dir_clean[files_dir.index(x)])
                          #greenzone1
        #print( 'ok: ', status.ok)
        #print( 'status: ', status.status)
        #print( 'stderr: ', status.stderr)       
        #print("Decryption Complete")
    
    def cleanup(self):
        dest1, dest2, dest3, dest4 = cf.destination()
        #removing any files ending with the gpg extention. some new files have been created when decrypted. 
        files = [f for f in os.listdir(dest1) if os.path.isfile(f)]
        new_dest = dest2
        for f in files:
             if f.endswith('gpg'):
                 os.remove(f)
        files = [f for f in os.listdir(dest1) if os.path.isfile(f)]
        for f in files:
             shutil.move(f, new_dest)
           
