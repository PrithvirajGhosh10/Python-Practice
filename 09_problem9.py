#9. Write a program to find out whether a file is identical & matches the content of another file.
with open("this.txt")as f:
    a=f.read()
with open("this_copy.txt") as f:
    b=f.read()
if(a==b):
    print("Yes file is identical & matches the content")
else:
    print("No file is not identical & matches the content")