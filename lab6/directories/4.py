file = open(r'C:\Users\z_ali\Desktop\labs_pp2\lab6\directories\zhaner.txtt', 'r')
count = 0
for i in file:
    if i != '\n':
        count += 1
print(count)