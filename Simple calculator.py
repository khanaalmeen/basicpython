
#***** Simple Calculator in Python *****#

# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division

print("Select an operation to perform:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while(True):
 operation= int(input("Enter an operation :"))
 num1= float(input("Enter First number : "))
 num2= float(input("Enter Second number : "))


 if operation == 1:
   print("{} + {} = " . format(num1,num2), num1 + num2)
 elif operation == 2:
   print("{} - {} = ".format(num1,num2),num1 - num2)
 elif operation == 3:
   print("{} * {} = ".format(num1,num2), num1*num2)
 elif operation == 4:
   print("{} / {} = 4".format(num1,num2), num1/num2)
 else:
   print("Invalid Entry")










