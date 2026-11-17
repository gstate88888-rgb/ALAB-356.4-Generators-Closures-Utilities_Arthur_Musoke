# fibonacci_generator.py

def gen_fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        yield a
        a, b = b, a + b


# Test Code
count = int(input("How many Fibonacci numbers would you like to generate? "))

print("\nFibonacci Sequence:")

for num in gen_fibonacci(count):
    print(num)
