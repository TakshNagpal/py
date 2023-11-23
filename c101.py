import os
import shutil

source = "/Users/takshnagpal/Downloads/ABC"
destination = "/Users/takshnagpal/Desktop"

files = os.listdir(source)
for i in files:
    name,ext = os.path.splitext(i)
    if ext == "":
        continue
    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        path1 = source + '/' + i
        path2 = destination + '/' + "Image_Files"
        path3 = destination + '/' + "Image_Files" + '/' + i

        if os.path.exists(path2):
            print("Moving")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Creating and moving")
            shutil.move(path1,path3)
        
    


