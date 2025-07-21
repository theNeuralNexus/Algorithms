# Problem:
# You are given a list of student names and their corresponding scores.
# Your task is to write a Python function that, given a student's name, finds and
# returns their score. If the student is not found, it should return -1.

student_data: list = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]


def find_student_score(required_name: str, data: list) -> int:
    for name, score in data:
        if name == required_name:
            return score
    return -1


# Student in the list
print(find_student_score("Alice", student_data))
print(find_student_score("Charlie", student_data))

# Student not in the list
print(find_student_score("Jhon", student_data))

# Edge Cases
print(find_student_score("James", []))
