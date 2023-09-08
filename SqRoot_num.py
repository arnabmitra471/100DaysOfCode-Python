# Solution 1
# num = int(input("Enter a number: "))
# sq_root = num ** (1/2)
# print("The square root of the number is",sq_root)

# Solution 2
import math
num = int(input("Enter a square number: "))
sq_root = math.sqrt(num)
print("The square root of {0} is {1}".format(num,sq_root))