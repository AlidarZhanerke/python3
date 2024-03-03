import os

for i in os.listdir(r'C:\Users\z_ali\Desktop\labs_pp2\lab6'):
    if os.path.isdir(r'C:\Users\z_ali\Desktop\labs_pp2\lab6'):
         print(i, end = ' ')

for i in os.listdir(r'C:\Users\z_ali\Desktop\labs_pp2\lab6'):
     if os.path.isfile(r'C:\Users\z_ali\Desktop\labs_pp2\lab6'):
      print(i, end = ' ')
for i in os.listdir(r'C:\Users\z_ali\Desktop\labs_pp2\lab6'):
     print(i)
