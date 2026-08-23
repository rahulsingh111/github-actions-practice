def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    print("Simple Calculator")
    print("=================")

    a = 20
    b = 5

    print(f"Addition:       {add(a, b)}")
    print(f"Subtraction:    {subtract(a, b)}")
    print(f"Multiplication: {multiply(a, b)}")
    print(f"Division:       {divide(a, b)}")


if __name__ == "__main__":
    main()
#test
