num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is not a prime number.")
else:
    flag = True

    for i in range(2, num):
        if num % i == 0:
            flag = False
            break

    if flag:
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")