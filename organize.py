import os
import shutil

from_dir="C:/Users/User/Downloads"
to_dir="c:/WhiteHatJr/downloadedimages"
list_of_files=os.listdir(from_dir)
#print(lis_off_files)

#move all image foler to another folder
for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)
    print(name)
    print(extension)

if extension == '':
    continue
if extension in ['.gif','.png','.jpeg','.jpg','.webp','.jfif']:
    path1=from_dir+'/'+ file_name
    path2=to_dir+'/'+"Image_Files"  
    path3=to_dir+'/'+ "Image_Files"+'/'+file_name