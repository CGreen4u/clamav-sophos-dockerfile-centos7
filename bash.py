import subprocess
import os
import configuration as cf

class malware_process:
    def __init__(self):
        self.clamscan_virus_dir = None
        self.sophos_virus_dir = None
        self.clean_files = None
        self.changes = None
        self.files_b4_cleaning = None
    def getBash(self):
        binfo = [self.clamscan_virus_dir, self.sophos_virus_dir, self.clean_files, self.changes, self.files_b4_cleaning]
        return binfo
    def setBash(self, clamscan_virus_dir, sophos_virus_dir, clean_files, changes, files_b4_cleaning):
        self.clamscan_virus_dir = clamscan_virus_dir
        self.sophos_virus_dir = sophos_virus_dir
        self.clean_files = clean_files
        self.changes = changes
        self.files_b4_cleaning = files_b4_cleaning
    def malware_location(self):  
        dest1, dest2, dest3, dest4 = cf.destination()  
        #create seperate path for files to be placed into this is important becasue it creates the folders if they are not made.
        if os.path.exists(dest4):
            pass
        else:
            os.mkdir(dest4)
        if os.path.exists(dest3):
            pass
        else:
            os.mkdir(dest3)  
          
         
        #files_b4_cleaning = [(dest2)]
        #return files_b4_cleaning

    def malware_bash(self):
        dest1, dest2, dest3, dest4 = cf.destination()
        dest5, dest6 = cf.destination2()
        files_b4_cleaning = [(dest2)]
        clamscan_virus_dir = []
        sophos_virus_dir = []
        clean_files = []
        changes = []
        #Run command on command line to start the first malware scanner ClamAV. list of files scanned and cleared are saved to list
        bashCommand = "clamscan -r --move="+ dest4 + " "+ dest2 +""
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        for root, dirs, files in os.walk(dest4):
              for file in files:
                clamscan_virus_dir.append(file)
                ##return clamscan_virus_dir
        #Running second bash command for the Sophos malware scanner
        #bashCommand2 ="sweep "+ dest2 +" ""--quarantine="+ dest4 +"" 
        bashCommand2 ="sweep"" " + dest5 + "-move="+ dest6 + "" 
        process = subprocess.Popen(bashCommand2.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        for root, dirs, files in os.walk(dest4):
            for file in files:       
                changes.append(file)
        ##        return changes
        sophos_virus_dir.append(list(set(changes) - set(clamscan_virus_dir)))
        clean_files = os.listdir(dest2)
        self.setBash(self.clamscan_virus_dir, self.sophos_virus_dir, self.clean_files, self.changes, self.files_b4_cleaning)
        return malware_process.getBash(self)
