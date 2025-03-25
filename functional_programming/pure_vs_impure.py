def multiply_by_two(numbers):
    new_numbers = []
    for num in numbers:
        new_numbers.append(num * 2)
    return new_numbers

def multiply_by_two_impure(numbers):
    new_numbers = []
    for num in numbers:
        new_numbers.append(num * 2)
        print(num)
    return new_numbers
    
    
# use the pure function
# 1. It does not have side effects 
# 2. It does not modify outside data
# 3. The output is always the same for same input

nums = [10, 20, 30, 40]
new_nums = multiply_by_two(nums)
print(new_nums)
print(nums)

new_nums_two = multiply_by_two_impure(nums)
print(new_nums_two)



    
        