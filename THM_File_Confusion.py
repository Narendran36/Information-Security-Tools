import zipfile
import os
import exiftool


with zipfile.ZipFile('final-final-compressed.zip','r') as zip_ref:
        zip_ref.extractall('zips')

zip_files = os.listdir('zips')

for f in zip_files:
        with zipfile.ZipFile('zips/'+f,'r') as zip_ref:
                zip_ref.extractall('filez')

ext_files = os.listdir('filez')
print(len(ext_files))
#print(os.getcwd())
os.chdir('filez')
#print(os.getcwd())

count = 0
with exiftool.ExifTool() as et:
        metadata = et.get_metadata_batch(ext_files)
        for d in metadata:
                if 1.1 in d.values():
                        count += 1
print(count)

for f in ext_files:
        with open(f) as F:
                L = F.readlines()
                for l in L:
                        if 'password' in l:
                                print(f)
                                break
