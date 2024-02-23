def gen(n):
    idx = 0
    while idx <=n:
        yield idx
        idx +=1
def isEven(a):
    for i in a:

     if i%2 == 0 :
        yield i

b = gen(int(input()))
c = isEven(b)
for i in c:
    print(i)

        