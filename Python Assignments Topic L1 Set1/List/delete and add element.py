lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input("Enter element: "))
    lst.append(ele)
print("The list before removal:", str(lst))

a = int(input("Enter the element to remove: "))
b = int(input("Enter the element to add: "))

lst.remove(a)
lst.append(b)

print("The list after change:", str(lst))
