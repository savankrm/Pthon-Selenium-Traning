lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
print(lst)

#Logice to exchange

temp=lst[0]
lst[0]=lst[-1]
lst[-1]=temp

print(lst)