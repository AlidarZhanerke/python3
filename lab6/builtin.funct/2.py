def upperlower(s):
    upperletters=0
    lowerletters=0
    for i in s:
        if i.isupper():
            upperletters+=1
        if i.islower():
            lowerletters+=1
    return upperletters,lowerletters
s= input()

print(upperlower(s))


