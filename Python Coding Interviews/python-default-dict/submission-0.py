from collections import defaultdict
from typing import List, Dict


def count_chars(s: str) -> Dict[str, int]:
    cl = [c for c in s]
    freq = defaultdict(int)

    for char in cl:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1
    
    return freq




def nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]:
    
    output = defaultdict(list)

    for element in nums:
        header = element[0]
        body = element[1:]

        if header in output:
            output[header] += body
        else:
            output[header] = body
    
    return output



# do not modify below this line
print(count_chars("hello"))
print(count_chars("helloworld"))
print(count_chars("areallylongstringwhyareyoureadingthishahalol"))

print(nested_list_to_dict([[1, 2, 3], [4, 5, 6], [1, 4]]))
print(nested_list_to_dict([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6]]))
print(nested_list_to_dict([[5, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]))
print(nested_list_to_dict([[3, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8]]))
