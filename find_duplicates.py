seen=[]
o_list=[]
dups=[]
N=int(input("Enter the number of elements you want to add: "))
i=1
while i<=N:
    K = int(input(f"Enter number {i}: "))
    o_list.append(K)
    i=i+1
for j in o_list:
    if j not in seen:
        seen.append(j)
    elif j not in dups:
        dups.append(j)
print("Original list is: ",o_list)
print("Duplicate list (list with repeated numbers) is: ",dups)