# write a python program to check whether the given item is present in the set or not.

set1 = {'Savan', 'Wipro', 2023, 11}
print("The given set:", set1)

n = input()
print("The input to be searched in set:", n)

try:

    value = int(n)
except ValueError:
    value = n

if value in set1:
    print("The element is present")
else:
    print("Element not found")
