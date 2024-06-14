# Write a Python program to add an item to a tuple

t = (2, 3, 4, 5, 6, 7)
print("Tuple before insertion:", t)

lst = list(t)
element = 4

lst.append(element)
t_updated = tuple(lst)

print("The tuple after addition:", t_updated)
