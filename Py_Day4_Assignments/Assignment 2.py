# Write a Python program to concatenate all elements in a list into a string and return it


# creating an empty list
lst = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    ele = input()

    lst.append(ele)  # adding the element

print(lst)

# concatenating the list
def concatenate_list_data(ele):
    result= ''
    for element in ele:
        result += str(element)
    return result
