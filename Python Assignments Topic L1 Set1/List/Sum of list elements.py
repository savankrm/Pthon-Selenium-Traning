
def addition(lst):
    print("the sum of all list elements is",sum(lst))



lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
print(lst)
addition(lst)



