import os
import random
files = []
for root, mydir, fileiter in os.walk(".", topdown=True):
   for name in fileiter:
      print((os.path.join(root, name)))
      files.append(os.path.join(root, name))
extension = input("Which file extension would you like to shuffle?")
files = [file for file in files if file.endswith(extension)]
filesOld = files.copy()
random.shuffle(files)
print(filesOld)
print(files)
for i in range(len(files)):
    os.rename(filesOld[i],files[i]+"-pytemp");
for i in range(len(files)):
    os.rename(files[i]+"-pytemp",files[i]);

        
