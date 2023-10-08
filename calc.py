
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b


print("Select operation.")
print("1.Addittion")
print("2.Subtraction")
print("3.Multiplication")
print("4.Divition")

while True:
    choice = input("Enter choice: ")

    if choice in ('1', '2', '3', '4'):
        try:
            n1 = float(input("Enter first number: "))
            n2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(n1, "+", n2, "=", add(n1, n2))

        elif choice == '2':
            print(n1, "-", n2, "=", sub(n1, n2))

        elif choice == '3':
            print(n1, "*", n2, "=", mul(n1, n2))

        elif choice == '4':
            try:
                print(n1, "/", n2, "=", div(n1, n2))
            except ZeroDivisionError:
                print("Can't divide something with zero")

        
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")