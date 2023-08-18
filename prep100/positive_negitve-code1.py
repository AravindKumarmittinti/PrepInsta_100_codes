# finding a number is a positive or negitive number
#model 1 using nested if
num = int(input(" Enter a number you want to check :"))
if num>=0:
    if num == 0:
        print("you enterd number is Zero") 
    else:
        print(" The number you enterd is Positive")
else:
    print("The number you enterd is Negitive")
    
    
#model 2 using terinary operator

out = "Positive" if num>0  else "Negitive" if num<0 else 'Zero'
print(out)

#model3 using brute force method

if num>0:
    print("Postive")
elif num == 0:
    print('Zero')
else:
    print('Negative')
