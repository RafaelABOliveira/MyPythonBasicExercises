number = int(input("Enter any number: "))

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "not prime")
            break
    else:
        print(number, "is prime")

else:
    print(number, "not prime")