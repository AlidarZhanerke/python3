def ischeck(s):
    rev = s[::-1]
    if rev == s:
        return True
    else:
        return False
    
t = input()
print(ischeck(t))

    