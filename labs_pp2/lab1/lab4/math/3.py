from math import pi, tan
n = int(input())
side = int(input())
area = n * (side ** 2) / (4 * tan(pi / n))
print(area)