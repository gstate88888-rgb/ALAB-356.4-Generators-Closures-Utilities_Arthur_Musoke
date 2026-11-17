# multiplier_closure.py

def make_multiplier(factor):

    def multiply(x):
        return x * factor

    return multiply


# Create multipliers
times3 = make_multiplier(3)
times10 = make_multiplier(10)

# Test them
print("times3(7) =", times3(7))
print("times10(7) =", times10(7))
