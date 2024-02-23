def gen(n):
    idx=0
    while idx<=n:
        yield idx
        idx +=1

def divis(l):
    for i in l:
        if i %3==0:
            if i%4 ==0:
                yield i

a = gen(int(input()))
b= divis(a)
for i in b:
    print(i)


