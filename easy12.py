#easy12
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main()
    n = 5
    result = factorial(n)
    print(f"The factorial of {n} is {result}")

main()
