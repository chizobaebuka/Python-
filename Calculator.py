#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What is the first number? "))
for symbol in operations:
  print(symbol)
should_continue = True

while should_continue:
    operations_symbol = input("Pick an operation symbol from the line above:")
    num2 = int(input("What is the next number? ")) 
    calculation_function = operations[operations_symbol]
    answer = calculation_function(num1, num2)
    
    print(f"{num1} {operations_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with the {answer}, or type 'n' to exit.: ") == "y":
        num1 = answer
    else:
        should_continue = False