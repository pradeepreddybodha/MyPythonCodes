def selection_sort(li):
    for j in range(len(li)-1):
        for i in range(j, len(li) - 1):
            if li[j] > li[i + 1]:
                li[j], li[i + 1] = li[i + 1], li[j]
    return li


li = [23, 45, 56, 12, 3, 89]
li = selection_sort(li)
print("Sorted List:", li)