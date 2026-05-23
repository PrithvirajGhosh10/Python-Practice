# 6. Write a program to mine a log file and find out whether it contains 'python,
word="Python"
with open("log.txt","r") as a:
    find=a.read()
    if(word in find):
        print("yes python is present")
    else:
        print("No python is not present")