nums=[]
N=int(input("Enter the number of elements you want to add: "))
for i in range(N):
    p=int(input("Enter number"))
    nums.append(p)

print(nums)
print(max(nums))