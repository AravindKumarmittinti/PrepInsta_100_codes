# Sum of natural numbers in a range
# model 1 using for loop brute force method
start = int(input("Enter starting value :"))
end = int(input("Enter ending value :"))
sum = 0
for i in range(start,end +1):
    sum += i
print(sum)

# using formula 

total = (end * (end +1))/2
dif = ((start -1) * ((start-1) +1 ))/2
result = total - dif
print(int(result))

#using recurrsion

def recsum(start,end):
    if start and end == 0:
        return 0
    return start + recsum(start +1,end)
print(recsum(start,end))
