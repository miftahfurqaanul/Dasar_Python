memoization_dict = {}

def factorial_memoization(n):
    if n in memoization_dict:
        return memoization_dict[n]

    if n == 0 or n == 1:
        result = 1
    else:
        result = n * factorial_memoization(n - 1)

    memoization_dict[n] = result
    return result

# Examples
num1 = 5
num2 = 10
num3 = 20

result1 = factorial_memoization(num1)
result2 = factorial_memoization(num2)
result3 = factorial_memoization(num3)

print(f"Factorial of {num1} is: {result1}")
print(f"Factorial of {num2} is: {result2}")
print(f"Factorial of {num3} is: {result3}")

print("Memoization dictionary:", memoization_dict)