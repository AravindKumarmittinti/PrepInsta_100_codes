# find given number is a prime or not
num = int(input("Enter a number  :"))
count = 0
if num == 1 or num <= 0 :
    print("not prime")
else:
    for i in range(2,num):
        if num%i == 0:
            count += 1
        else:
            continue
    if count == 0:
        print("then it is a prime number")
    else:
        print("the number is not a prime number")