# def Factorial(n)->int:
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * Factorial(n-1)
    
# a = Factorial(5)
# print(a)

# def fib(n: int) -> int:
#         if n<=1:
#             return n
#         return fib(n-1) + fib(n-2)
# a = fib(10)
# print(a)

# def climbStairs( n: int) -> int:
#         if n<=3:
#             return n
#         return climbStairs (n-1) + climbStairs(n-2)
# n = 6
# a = climbStairs(n)
# print(a)

def sumOfDigits(n) -> int:
    #base state condition
    if n==0:
        return 0
    #Recursive function call
    return (n%10)+sumOfDigits(n//10)

a = sumOfDigits(1234)
print(a)