def calculate(x,operator,y):
    if operator == "+":
        return x+y
    elif operator == "-":
        return x-y
    elif operator == "*":
        return x*y
    elif operator == "/":
        if y == 0:
            return "Cannot divide by zero"
        return x/y
    else:
        return("invalid operator")

print("Let's perform a simple mathematics operation")
while True:
    num = input("Enter the First number (or CLS to stop): ")
    if num.upper() == "CLS":
        break
    try:
        num_1 =float(num)
    except ValueError:
        print("Please enter a valid number")
        continue
    operator = input("Pick the operator you what use[+, - , * , / ]")
    
    num2 = (input("Enter the second number: "))
    try:
        num_2 =float(num2)
    except ValueError:
        print("Please enter a valid number")
        continue

    print(calculate(num_1,operator,num_2))

print("Calculator Cleared")