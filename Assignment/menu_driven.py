num = int(input("Enter your number:"))
print("Check your entered number is:\n1.Even\n2.Odd");
choice = int(input("Enter your choice(in number):"))

if choice == 1:  
    if num%2 == 0 :
        print("Number is even.")
elif choice == 2:
    if num%2 != 2:
        print("Number is Odd")
elif choice != 1 and choice != 2:
    print("Invalid input")


    
