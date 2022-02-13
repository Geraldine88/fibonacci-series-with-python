import math

"""
A utility function that will return true if the number is a perfect square, else it will return false
A given number is Fibonacci iff 5n^2 +4 or 5n^2 -4 is a perfect square
"""
def isSquare(num):
    #finding the square root of num
    s = int(math.sqrt(num))
    return s*s == num

def isFibonacciNumber(n):
    #return true if the number is fibonacci otherwise return false
    return isSquare(5*n*n+4) or isSquare(5*n*n - 4)

n = int(input("Enter the number you want to check : "))
if(isFibonacciNumber(n) == True):
    print("The given number is fibonacci number")
else:
    print(n, "is not a fibonacci number")
