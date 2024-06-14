#Write a python program to print the odd numbers from 1 to 30 using continue statement.
n= int(input("Enter the maximum number: "))

a=1
while a<n+1:
    if a%2==0:
        a+=1
        continue
    print(a, end=' ')
    a+=1
