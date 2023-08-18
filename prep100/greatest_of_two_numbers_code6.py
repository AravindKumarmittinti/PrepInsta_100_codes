# Find greatest num

#model 1 using if else 
num1 = int(input("enter the 1st number :"))
num2 = int(input("enter the 2nd number :"))

if num1>num2:
    print("{0} is big".format(num1))
elif num1 == num2:
    print("both are Equal")
else:
    print("{0} is big ".format(num2))
    
#model 2 using terinary operator

print('{0} is big'.format(num1)) if num1>num2 else print("Equal") if num1 == num2 else print('{0} is big'.format(num2))


# model 3 usingg max function

print(max(num1,num2))
