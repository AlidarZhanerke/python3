import os

path = r'C:\Users\z_ali\Desktop\labs_pp2\lab6\directories\zhaner.txtt'
if os.path.exists(path):
   os.remove(path)
   print('removed')
else:
   print('your file does not exists')