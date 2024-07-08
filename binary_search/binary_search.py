def binary_search(arr, target):
    """
    Perform binary search to find the target in arr.

    Parameters:
    arr (list): Sorted list.
    target (int): Value to search for.

    Returns:
    int: Index of the target in arr if found, otherwise -1.
    """
    left, right = 0, len(arr)-1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def main():
    arr = list(map(int, input("Enter a list of numbers (separated by spaces): ").split()))
    arr.sort()
    target = int(input("Enter the value to search for: "))

    result = binary_search(arr, target)

    if result != -1:
        print(f"The value {target} was found at index {result}.")
    else:
        print(f"The value {target} is not in the list.")


if __name__ == "__main__":
    main()
