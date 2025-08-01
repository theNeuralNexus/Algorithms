# Binary Search Algorithm
# Divide & Conquer Principle
# Very efficient for the sorted lists; but the key is sroted lists
# Time Complexity: O(log n))


def main() -> None:
    """Main part of the program"""
    nums1 = [1, 2, 3, 5, 6, 7, 8, 9, 10]
    # Cases in which the element is in the list
    print(binary_search(nums1, 5))
    print(binary_search(nums1, 1))
    print(binary_search(nums1, 10))

    # Cases in which the target is not in the list
    print(binary_search(nums1, 0))
    print(binary_search(nums1, 11))
    print(binary_search(nums1, 4))

    # Edge Cases
    print(binary_search([], 1))
    print(binary_search([1], 1))
    print(binary_search([10], 100))


def binary_search(numbers: list, target: int) -> int:
    """
    Binary Search Algorithm to find the target element from the list

    Args:
        numbers (list): List of all the numbers
        target (int): Number to find from the list

    Returns:
        int: Index at which element is present otherwise -1
    """
    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] == target:
            return mid 
        elif numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == "__main__":
    main()
