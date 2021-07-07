num=int(input("Enter the number of terms: "))
n1=0
n2=1
count=0
if num<=0:
    print("Enter a positive number")
elif num==1:
    print("Fibonacci Series")
    print(n1)
else:
    print("Fibonacci Series")
    while count<num:
        print(n1)
        sum=n1+n2
        n1=n2
        n2=sum
        count=count+1