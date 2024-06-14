#Assign 2 numbers to the variables a and b. Write a program to print ”the sum of 2 no is” with the value a+b using 4 ways
#(",","+","f","format")

a = int(input("First number:"))
b = int(input("Second number:"))
sum=a+b

print("The sum of 2 no is",sum)

print("The sum of 2 no is " + str(sum))

print(f"The sum of 2 no is {sum}")

print("The sum of 2 no is =",format(sum,"d"))
