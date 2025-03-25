# import the reduce from functools
from functools import reduce

numbers = [10, 20, 30, 40, 50]

def accumulator(x, y):
    return x + y
    
sum_result = reduce(accumulator, numbers)
print(sum_result)

sum_result_with_offset = reduce(accumulator, numbers, 100)
print(sum_result_with_offset)

nested_lists = [[1,2], [3,4], [5,6], [7,8], [9]]

# [1, 2] + [3, 4] = [1, 2, 3, 4]
def accumulate_lists(list1, list2):
    return list1 + list2 

flattened_list = reduce(accumulate_lists, nested_lists)
print(flattened_list)

