def square (a,b):
    for i in range(a,b):
        yield i**2

square1 = square(a = int(input()) , b = int(input()))
for i in square1:
    print(i)
    
