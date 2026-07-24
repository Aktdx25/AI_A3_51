def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def div(a, b):
    return a / b


while True:  # do-while equivalent in Python
    print("\nSelect the arithmetic operation you want to perform:")
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")

    ch = int(input("Enter Choice 1-5: "))

    if ch == 1:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = add(num1, num2)
        print(f"Sum = {result}")

    elif ch == 2:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = sub(num1, num2)
        print(f"Difference = {result}")

    elif ch == 3:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = multiply(num1, num2)
        print(f"Result = {result}")

    elif ch == 4:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if num2 != 0:
            result = div(num1, num2)
            print(f"Result = {result}")
        else:
            print("Cannot divide by zero!")

    elif ch == 5:
        print("Program closed")
        break  # exits the loop

    else:
        print("Invalid choice. Please select between 1-5.") 
	  
