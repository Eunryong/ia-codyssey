def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def parse_factor(tokens):
    token = tokens.pop(0)
    if token == '(':
        number = parse_expression(tokens)
        tokens.pop(0)
        return number
    else:
        return float(token)

def parse_term(tokens):
    number = parse_factor(tokens)
    while tokens and tokens[0] in ('*', '/'):
        operator = tokens.pop(0)
        next_number = parse_factor(tokens)
        if operator == '*':
            number *= next_number
        else:
            number /= next_number
    return number

def parse_expression(tokens):
    number = parse_term(tokens)
    while tokens and tokens[0] in ('+', '-'):
        op = tokens.pop(0)
        next_number = parse_term(tokens)
        if op == '+':
            number += next_number
        else:
            number -= next_number
    return number

def is_number(token):
    try:
        float(token)
        return True
    except ValueError:
        return False

def validate_tokens(tokens):
    allowed = set('0123456789.+-*/()')
    prev_type = None  # 'number', 'operator', 'open_paren', 'close_paren'
    for token in tokens:
        # 문자 검사
        if not (is_number(token) or token in ('+', '-', '*', '/', '(', ')')):
            raise ValueError(f"허용되지 않는 토큰: '{token}'")
        # 연속 숫자 검사
        curr_type = 'number' if is_number(token) else (
            'open_paren' if token == '(' else
            'close_paren' if token == ')' else
            'operator'
        )
        if prev_type == 'number' and curr_type == 'number':
            raise ValueError("숫자가 연속해서 나올 수 없습니다.")
        if prev_type == 'operator' and curr_type == 'operator':
            raise ValueError("연산자가 연속해서 나올 수 없습니다.")
        prev_type = curr_type

def calculator(args):
    validate_tokens(args)
    return parse_expression(args)

def main():
    try:
        args = input().split()
        print("Result:", calculator(args))

    except ValueError:
        print("Invalid input")
    
    except ZeroDivisionError:
        print("Error: Division by zero.")
    
if __name__ == "__main__":
    main()