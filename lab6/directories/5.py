file = open(r'C:\Users\z_ali\Desktop\labs_pp2\lab6\directories\zhaner.txtt', 'w')
mylist =['i am zhanerke', 'i get fullka from midterm proofReal Madrid the best team in history','115','18']
for i in mylist:
    file.write(str(i) + '\n')
file.close()
f = open(r'C:\Users\z_ali\Desktop\labs_pp2\lab6\directories\zhaner.txtt', 'r')
print(f.read())