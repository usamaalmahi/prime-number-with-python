num = input("Enter a number\n")
mid=num/2
flag=0
for i in range(2,mid):
    if num%i == 0:
        flag=1
        break
    i=i+1
if flag==0:
    print("this is prime number")
else:
    print("this is not prime")
