def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError()
    
    return a / b

def main():
    try:
        a, operator, b = input("Enter expression: ").split()
        a, b = float(a), float(b)
        
        answer = 0
        if operator == '+':
            answer = add(a, b)
        elif operator == '-':
            answer = subtract(a, b)
        elif operator == '*':
            answer = multiply(a, b)
        elif operator == '/':
            answer = divide(a, b)
        else:
            print("Invalid operator.")
            return
        
        print("Result:", answer)

    except ValueError:
        print("Invalid number input")
    
    except ZeroDivisionError:
        print("Error: Division by zero.")
    
if __name__ == "__main__":
    main()