# Problem 1: Find Largest Number in a list

def find_largest(numbers):
    if not numbers:
        return none 

    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest
# numbers = [2, 41, 56, 21, 76, 9]            
numbers = [1, 4, 6, 9, 2]
# numbers = []
print(find_largest(numbers))