def my_min(numbers):
    min_num = float('inf')
    for num in numbers:
        if num < min_num:
            min_num = num
    return "Min: " + str(min_num)

def my_max(numbers):
    max_num = float('-inf')
    for num in numbers:
        if num > max_num:
            max_num = num
    
    return "Max: " + str(max_num)

def main():
    try:
        numbers = list(map(float, input().split()))
        if not numbers:
            raise ValueError
        print(my_min(numbers), my_max(numbers), sep=", ")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()