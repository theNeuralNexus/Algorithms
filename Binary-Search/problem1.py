# Problem: Library Catalog Search

# You are helping manage a digital library catalog. This catalog contains information about books,
# and it is always sorted by Book ID in ascending order. Your task is to implement a binary search algorithm
# to efficiently find a specific book by its Book ID.

# If the book is found, you should return all its details (Book ID, Title, and Author).
# If the book is not found in the catalog, you should indicate that.


def main() -> None:
    """Main part of the program"""
    catalog: list = [
        [101, "The Great Gatsby", "F. Scott Fitzgerald"],
        [105, "To Kill a Mockingbird", "Harper Lee"],
        [110, "1984", "George Orwell"],
        [115, "Pride and Prejudice", "Jane Austen"],
        [120, "Moby Dick", "Herman Melville"],
    ]

    # Book Found
    print(find_book(catalog, 110))
    print(find_book(catalog, 111))
    print(find_book(catalog, 120))
    
    # Book not found
    print(find_book(catalog, 101))

    # Added a new book and found that
    catalog.append([125, "Atomic Habits", "James Clear"])
    print(find_book(catalog, 125))

    # Edge Cases
    print(find_book([], 1))
    print(find_book([[100, "Harry Potter", "J.K. Rowling"]], 100))


def find_book(catalog: list, book_id: int) -> str:
    """
    Find the book in the catalog by id using binary serach algorithm

    Args:
        catalog (list): list of all the books where each book is a list [book_id, book_name, author]
        book_id (int): ID of the book which we are going to find

    Return:
        str: Prints if the book is found with all of the respective information otherwise print not found
    """
    if not catalog:
        return "Catalog is empty. There is no book."

    low: int = 0
    high: int = len(catalog) - 1

    while low <= high:
        mid: int = (low + high) // 2
        mid_book_id: int = catalog[mid][0]
        print(mid_book_id)
        if mid_book_id == book_id:
            return (
                f"Book Found, ID: {mid_book_id}, Name: {catalog[mid][1]} and Authour: {catalog[mid][2]}"
            )
        elif mid_book_id < book_id:
            low = mid + 1
        else:
            high = mid - 1

    return f"Book not found with the ID {book_id}"


if __name__ == "__main__":
    main()
