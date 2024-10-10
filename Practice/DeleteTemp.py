import os
import shutil
def delFiles(path): # path to Temp folder, in this case
    for file in os.listdir(path):
        filePath=path+"\\"+file
        print(filePath)
        try:
            if os.path.isdir(filePath):
                shutil.rmtree(filePath)
            else:
                os.remove(filePath)
        except: # when access denied
            continue

delFiles()