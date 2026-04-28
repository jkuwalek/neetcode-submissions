from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    best_student: Tuple[str, int] = ("a", 0)
    for student, grade in scores:
        if grade > best_student[1]:
            best_student = (student, grade)
    return best_student[0]
        




# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
