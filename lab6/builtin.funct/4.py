import math
import time 
def root(number, ms):

    result = math.sqrt(number)
    return result

number =int(input())
ms = int(input())


result = root(number, ms)


print(f"Square root of {number} after {ms} milliseconds is {result}")

