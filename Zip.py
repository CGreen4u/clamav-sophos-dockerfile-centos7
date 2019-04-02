import os
import tarfile
import configuration as cf


class zipper:
    def __init__(self, filename):
        self.filename = filename

    def unzip(self):
        dest1, dest2, dest3, dest4 = cf.destination()
        current_wkd = os.getcwd()
        pointed_dir = dest2
        try:
            for dirpath, dir, files in os.walk(top=pointed_dir):
                for file in files:
                    tar = tarfile.open(os.path.join(dirpath, file))
                    tar.extractall(path=pointed_dir)
                    tar.close()
        except tarfile.ReadError:
            print("No files to untar, moving on.")

    def zipit(self, filename):
        dest1, dest2, dest3, dest4 = cf.destination()
        #ziping/taring files that are in the clean list. files are named the same way as they came in under zip/tar  
        base_path = dest2
        next_path = dest3
        try:
            for dirpath, dir, files in os.walk(top=base_path):
                for file in files:#, root, dirs:    
                    #tar = tarfile.open(os.path.join(dirpath, file))
                    tar = tarfile.open(next_path +"/"+ 'testfile' + ".tar.gz", "w:gz")
                    #tar = tarfile.open(next_path +"/"+ filename + ".tar.gz", "w:gz")
                    tar.add(base_path)
                    tar.close()
                    break
                    os.rmdir(dest2)
        except FileNotFoundError as u:
            print (u)               
