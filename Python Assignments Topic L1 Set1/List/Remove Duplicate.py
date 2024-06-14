# input

lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
print("The list before removal:",str(lst))

res = []
for i in lst:
    if i not in res:
        res.append(i)

print("The list after the removal of duplicates:",str(res))
