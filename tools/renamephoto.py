import PIL
import PIL.ExifTags
from PIL import Image
import exifread  
import os
import os.path
import shutil
import time
import datetime

srcDir = "/Users/apple/Documents/photos"
dstDir = "/Users/apple/Documents/photos1"
for root, dirs, files in os.walk(srcDir):
    for file in files:
        ext = file.split(".")[-1]
        path = os.path.join(root, file)
        fd = open(path, 'rb')  
        tags = exifread.process_file(fd)
        fd.close()
        if tags.has_key("Image DateTime"):
            t = tags['Image DateTime']
            newName = "IMG" + str(t).replace(":", "").replace(" ", "") + "." + ext
            print newName
            shutil.move(os.path.join(root, file), os.path.join(dstDir, newName))
        else:
            t = os.path.getmtime(os.path.join(root, file))
            timeStruct = time.localtime(t)
            newName = "IMG" + time.strftime('%Y%m%d%H%M%S',timeStruct) + "." + ext
            print newName
            shutil.move(os.path.join(root, file), os.path.join(dstDir, newName))