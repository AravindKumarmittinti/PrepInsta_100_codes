# Finding the given number is even number or odd number
num = int(input("enter the number :"))
#model 1 using brute force 
if num >= 0:
    if num == 0:
        print("Zero")
    elif num%2 == 0:
        print("Even")
    else:
        print("odd")
else:
    print("the number is a intger") 
    
    
#model 2 using terinary operator
if num >= 0:    
    out = 'Zero' if num ==0 else 'Even' if num%2 == 0 else 'odd'
    print(out)
else:
    print("Integer")
    
# model 3 using bitwise operator
