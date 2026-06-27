text=input("Enter a string: ")
flag=True     #we are assuming that entered word is a palindrome
for i in range(len(text)//2):
    if text[i].upper()!=text[len(text)-1-i].upper():
        flag=False
        break

if flag==True:
    print("It's a palindrome!!")
else:
    print("It's not a palindrome...")

