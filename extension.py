filename=input("Input the Filename: ")
ext=filename.split(".")
str1="py"
str2="python"
if ext[-1]==str1 :
    print("The extension of the file is: ",str2)
else:
    print("The extension of the file is: "+ext[-1])

