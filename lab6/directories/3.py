import os

path = r'C:\Users\z_ali\Desktop\labs_pp2\lab6\directories'
if os.path.exists(path):
   print("Yes")
   filename = os.path.split(path)
   print(filename)
   print(filename[0])
   print(filename[1])
else:
   print("path is not exist")