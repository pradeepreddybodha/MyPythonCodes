from functools import *
li = range(1, 25)

print("Even Numbers:", list(filter(lambda n:n%2 == 0, li)))
print("Odd Numbers:", list(filter(lambda n:n%2 != 0, li)))
print("Sqr:", list(map(lambda n: n*n, li)))
print("Mean:", reduce(lambda a, b: a+b/2, li))