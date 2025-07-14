
def power(number, exponent):
    value = 1

    if (exponent >= 0):
        for _ in range(exponent):
            value *= number
    else:
        for _ in range(exponent * -1):
            value /= number

    return value

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        print("Invalid exponent input")
        return False

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        print("Invalid number input")
        return False

def main():
    input_number= input("Enter number: ")
    input_exponent = input("Enter exponent: ")
    if (is_float(input_number) and is_int(input_exponent)):
        number = float(input_number)
        exponent = int(input_exponent)
        
        answer = power(number, exponent)

        if (answer == int(answer)):
            print(int(answer))
        else:
            print(answer)


if __name__ == '__main__':
    main()