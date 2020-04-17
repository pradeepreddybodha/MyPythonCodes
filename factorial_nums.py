# from math import *
# def fact_orial(x):
#     z = 1
#     for i in range(0, x):
#         z = z * (x - i)
#     return z
#
#
# x = int(input("Enter the number to calculate the factorial:"))
# result = fact_orial(x)
# print("Facorial of", x, "is:", result)
# print("Using the in-built function:", factorial(x))

# Using recursive function

print("Using recursive function")

def fact_orial(a):
    if a == 1:
        return 1
    else:
        a = a * fact_orial(a-1)
        return a


a = int(input("Enter the number to calculate the factorial:"))
result = fact_orial(a)
print("Facorial of", a, "is:", result)
