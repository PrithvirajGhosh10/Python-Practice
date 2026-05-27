#4. Write a program to filter a list of numbers which are divisible by 5.
l=[1,33,15,51,45,40,10,84,621,84]
def divisible(n):
    if(n%5==0):
        return True
    return False
a=filter(divisible,l)
print("NO. Divisible by 5: ",list(a))
