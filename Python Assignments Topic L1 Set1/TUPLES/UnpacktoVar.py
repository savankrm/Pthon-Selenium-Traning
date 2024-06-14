# Write a Python program to unpack a tuple into several variables.

t=('savan',2023,True,11)

name,year,val,exp= t


print("My name is:",name)
print("The current year is: ",year)
print("The third variable type is :",type(val))
print("The last unpacked variable is:",exp)