def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    tail = arr[1:]
    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

def main():
    try:
        numbers = list(map(float, input().split()))
        if not numbers:
            raise ValueError
        sorted_numbers = quick_sort(numbers)
        print("Sorted:", " ".join(map(str, sorted_numbers)))

    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    main()