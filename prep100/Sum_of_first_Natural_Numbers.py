# Sum of Natural Numbers 
# model 1 using for loop brute force
num = int(input(" Enter the number:"))
sum = 0
for i in range(num+1):
    sum += i
print(sum)

# model 2 using  formula

out = (num * (num +1))/2
print(int(out))

# model using recurssion method

def sum(num):
    if num == 1:
        return 1
    return num + sum(num-1)
print(sum(num))