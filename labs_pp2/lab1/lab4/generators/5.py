def numbers(n):
        i=0
        while n>=0:
             yield n
             n-=1
numb = numbers(n= int(input()))
for i in numb:
    print(i)

