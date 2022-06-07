#Calculator

from art import logo
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
    print(logo)
    
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
      print(symbol)
    
    is_continue = True
    
    while is_continue:
        operation_symbol = input("Pick an operation: ") 
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        wanna_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ")
        
        if wanna_continue == "y":
            num1 = answer
        else:
            is_continue = False
            calculator()

calculator()