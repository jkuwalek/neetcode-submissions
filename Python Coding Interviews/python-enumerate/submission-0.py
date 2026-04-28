from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    i = -1

    for index, number in enumerate(nums):
        if number == 7:
            return index
    
    return i


def get_dist_between_sevens(nums: List[int]) -> int:
    seven_indexes = []

    for index, number in enumerate(nums):
        if number == 7:
            seven_indexes.append(index)
    
    return seven_indexes[1] - seven_indexes[0]


# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))
