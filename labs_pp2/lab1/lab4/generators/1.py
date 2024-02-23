def gen(n):
    idx =0
    while idx <= n:
        yield idx
        idx+=1
def square(a):
    for i in a:
        yield i**2

b = gen (int(input()))
c = square(b)
for i in c:
    print(i)



