import os

print("Enter Number of Seconds to Shutdown System: ")
sec = int(input())

strOne = "shutdown /s /t "
strTwo = str(sec)
str = strOne+strTwo

os.system(str)
