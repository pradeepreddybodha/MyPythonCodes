pos = 0
def binary_search(nums):
    l = 0
    u = len(li) - 1
    while l <= u:
        m = (l + u) // 2
        globals()['pos'] = m
        if li[m] == nums:
            return True
        else:
            if nums > li[m]:
                l = m
            else:
                u = m


# nums = int(input("Enter the number to search in the list: "))
li = [29, 53, 94, 54, 48, 52, 88, 58, 7]
li.sort()
nums = 88

if binary_search(nums):
    print("Number found at position", pos)
else:
    print("Number not found")
