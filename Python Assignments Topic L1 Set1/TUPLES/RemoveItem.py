# Write a Python program to remove an item from a tuple


t=(1,2,3,4,4,3,5,6,8,77,9,0,1,0,3,2,6,1)
print("The Given Tuple:",t)

ls=list(t)

ls.remove(77)

t_new=tuple(ls)

print("Tuple after removing 77 :",t_new)