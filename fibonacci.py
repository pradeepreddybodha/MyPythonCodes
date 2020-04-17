def func_fib(num):
    num2 = 1
    num1 = -1
    li = []
    fab_num = num1 + num2
    for i in range(0, num):
        fab_num = num1 + num2
        num1, num2 = num2, fab_num
        li.append(fab_num)
    return li
# num = int(input("Enter the number to find the fibonocci:"))
factorial = func_fib(10)
print(factorial)
