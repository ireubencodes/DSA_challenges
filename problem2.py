def find_smallest(numbers):
    if not numbers:
       return none

    smallest = numbers [0]
    for num in numbers:
        if num < smallest:
            smallest = numbers

    return smallest
# numbers = [2, 41, 56, 21, 76, 9]            
numbers = [1, 4, 6, 9, 2]
# numbers = []
print(find_smallest(numbers))