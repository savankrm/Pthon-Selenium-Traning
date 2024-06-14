# Write a Python program to get the least common multiple (LCM) of two positive integers.
a=int(input())
b=int(input())


def lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b
    while(True):
        if((greater % a == 0) and (greater % b == 0)):
            lcm = greater
            break
        greater += 1
    return lcm;

print("the LCM for given number is:",lcm(a,b))