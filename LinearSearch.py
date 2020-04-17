from random import *


def linear_search(nums):
    for j in li:
        globals()['pos'] += 1
        if j == nums:
            return True
            break


nums = int(input("Enter the number to search in the list: "))
li = [29, 53, 94, 54, 48, 52, 88, 58, 7]
pos = 0
for i in range(1, 10):
    k = randint(1, 100)
    li.append(k)


if linear_search(nums):
    print("Number found at position", pos)
else:
    print("Number not found")
