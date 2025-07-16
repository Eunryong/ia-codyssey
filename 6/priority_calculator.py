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
        if not tokens or tokens[0] != ')':
            raise ValueError
        tokens.pop(0)  # 닫는 괄호 제거
        return number
    else:
        return int(float(token))  # float 검증 후 int 변환

def parse_term(tokens):
    number = parse_factor(tokens)
    while tokens and tokens[0] in ('*', '/'):
        operator = tokens.pop(0)
        next_number = parse_factor(tokens)
        if operator == '*':
            number = multiply(number, next_number)
        else:
            number = divide(number, next_number)
    return number

def parse_expression(tokens):
    number = parse_term(tokens)
    while tokens and tokens[0] in ('+', '-'):
        op = tokens.pop(0)
        next_number = parse_term(tokens)
        if op == '+':
            number = add(number, next_number)
        else:
            number = subtract(number, next_number)
    return number

def is_number(token):
    try:
        float(token)
        return True
    except ValueError:
        return False

def validate_tokens(tokens):
    prev_type = None  # 'number', 'operator', 'open_paren', 'close_paren'
    paren_count = 0

    for token in tokens:
        if not (is_number(token) or token in ('+', '-', '*', '/', '(', ')')):
            raise ValueError

        curr_type = (
            'number' if is_number(token) else
            'open_paren' if token == '(' else
            'close_paren' if token == ')' else
            'operator'
        )

        # 연속성 체크
        if prev_type == 'number' and curr_type in ('number', 'open_paren'):
            raise ValueError
        if prev_type == 'operator' and curr_type == 'operator':
            raise ValueError
        if prev_type == 'open_paren' and curr_type == 'close_paren':
            raise ValueError
        if prev_type == 'close_paren' and curr_type in ('number', 'open_paren'):
            raise ValueError

        # 괄호 카운트
        if token == '(':
            paren_count += 1
        elif token == ')':
            paren_count -= 1
            if paren_count < 0:
                raise ValueError

        prev_type = curr_type

    if paren_count != 0:
        raise ValueError

    if prev_type == 'operator' or prev_type == 'open_paren':
        raise ValueError

def calculator(args):
    validate_tokens(args)
    return parse_expression(args)

def main():
    try:
        args = input().split()
        print("Result:", calculator(args))
    except ValueError:
        print("Invalid input.")
    except ZeroDivisionError:
        print("Error: Division by zero.")

if __name__ == "__main__":
    main()