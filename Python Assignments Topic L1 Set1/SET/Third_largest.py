#write a python program to find the third largest no from a given list
#use the python set data type.

def third_largest_number(numbers):
    unique_numbers = set(numbers)
    if len(unique_numbers) < 3:
        return None
    sorted_numbers = sorted(unique_numbers, reverse=True)
    return sorted_numbers[2]

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("The given list of numbers is:", numbers)

third_largest = third_largest_number(numbers)

if third_largest is None:
    print("There are less than 3 unique numbers in the list")
else:
    print("The third largest number in the list is:", third_largest)
