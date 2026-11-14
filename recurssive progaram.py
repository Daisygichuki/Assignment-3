def total(n):                       # (a) sum of first n natural numbers
    if n == 0:                      # base case
        return 0
    return n + total(n - 1)         # recursive case

def factorial(n):                   # (b) factorial
    if n <= 1:                      # base case
        return 1
    return n * factorial(n - 1)

def fib(n):                         # (c) nth Fibonacci term
    if n < 2:                       # base cases: fib(0)=0, fib(1)=1
        return n
    return fib(n - 1) + fib(n - 2)

def fib_series(n, a=0, b=1):        # (d) N terms, purely recursive
    if n == 0:
        return
    print(a, end=" ")
    fib_series(n - 1, b, a + b)

n = int(input("Enter n: "))
print("Sum of first", n, "numbers =", total(n))     # n=4 -> 10
print("Factorial of", n, "=", factorial(n))         # n=4 -> 24
print("Fibonacci term", n, "=", fib(n))             # n=5 -> 5
print("Fibonacci series:", end=" ")
fib_series(n)                                       # n=8 -> 0 1 1 2 3 5 8 13s