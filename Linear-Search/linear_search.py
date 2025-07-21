# Linear Search Algorithm:
# Linear search is simple and easy but not efficient algorithm for large lists
# Linear search algorithms is used to find a number in the list

# We check each and every number in the list
# If it is equal to target we return the index of list at which number is
# else we return -1

# Time Complexity: O(n)


def main() -> None:
    def linear_search(arr: list[int], target: int) -> int:
        for index in range(len(arr)):
            if arr[index] == target:
                return index
        return -1

    nums: list[int] = [5, 4, 3, 6, 9, 1]
    result: int = linear_search(nums, 3)

    if result != -1:
        print(f"Found at index {result}")
    else:
        print("Not found")


if __name__ == "__main__":
    main()
