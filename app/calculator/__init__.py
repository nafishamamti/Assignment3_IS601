from app.operations import Operations

def calculator():
    while True:
        userInput = input("Enter value1 operation (+,-,*,/) value2, or 'exit' to quit: ").strip()
        if userInput.lower() == 'exit':
            break
        try:  
            operand1, operator, operand2 = userInput.split()
            operand1 = float(operand1)
            operand2 = float(operand2)
            if operator == '+':
                result = Operations.addition(operand1, operand2)
            elif operator == '-':
                result = Operations.subtraction(operand1, operand2)
            elif operator == '*':   
                result = Operations.multiplication(operand1, operand2)
            elif operator == '/':
                result = Operations.division(operand1, operand2)
            else:
                print("Invalid operator. Please use +, -, *, or /.")
                continue
            print(f"Result: {result}")
        except ValueError:
            print("Invalid input format. Please enter in the format: value1 operator value2")
        except ZeroDivisionError as e:
            print(e)