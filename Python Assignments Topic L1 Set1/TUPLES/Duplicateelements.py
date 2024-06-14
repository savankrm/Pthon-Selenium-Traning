# Write a Python program to find repeated items in a tuple

t=(1,2,3,4,4,3,5,6,8,77,9,0,1,0,3,2,6,1)
print("The Given Tuple:",t)

ls=list(t)
rep=[]

for item in ls:
    if ls.count(item) > 1:
        if item not in rep:
            rep.append(item)

repated_element=tuple(rep)

print("the repeated elememts in tuple are:",repated_element)