# 7. Write a program to find out the line number where python is present from ques 6.
with open("log.txt","r") as a:
    lines=a.readlines()

lineno =1
for line in lines:
    if("Python" in line):
        print(f"yes python is present. line no.:{lineno}")
        break
    lineno +=1

else:
        print("No python is not present")