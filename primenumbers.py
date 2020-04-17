list_prime = [1, 2]
for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:
            break
        elif i - 1 == j:
            list_prime.append(i)
print(list_prime)
