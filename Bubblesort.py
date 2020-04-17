def bubble_sort(li):
    for j in range(len(li)-1, 0, -1):
        for i in range(j):
           if li[i] > li[i + 1]:
                li[i], li[i + 1] = li[i + 1], li[i]
    return li


li = [23, 45, 56, 12, 3, 89]
li = bubble_sort(li)
print(li)