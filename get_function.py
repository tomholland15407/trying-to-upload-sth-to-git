def Integral(f, a, b):
    return (f(a) + f(b)) / 2 * (b - a)

# Example usage
if __name__ == "__main__":
    import math

    # User inputs
    func_str = input("Enter a function of x (e.g., 'math.sin(x)', 'x**2 + 3*x'): ")
    a = float(input("Enter the lower limit a: "))
    b = float(input("Enter the upper limit b: "))

    # Convert string to function
    def f(x):
        return eval(func_str)

    # Calculate and print the integral
    result = Integral(f, a, b)
    print(f"The approximate integral of f(x) from {a} to {b} is: {result}")