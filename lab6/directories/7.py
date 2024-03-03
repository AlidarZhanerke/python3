file1 = open(r'C:\Users\z_ali\Desktop\labs_pp2\lab6\directories\zhaner.txtt', 'r')
file2 = open('text.txt', 'w')

for i in file1:
    file2.write(str(i))
file1.close()
file2.close()

file2 = open('text.txt', 'r')
print(file2.read())