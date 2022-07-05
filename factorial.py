print("Factorial of a number")
num = int(input("Enter a number = "))
factorial = 1

if num < 0:
    print("Enter a positive number")
elif num < 2:
    print("Factorial of a number {}! = {}".format(num ,factorial))
else:
    for i in range(num,1,-1):
        factorial=factorial*i
    print(factorial)
