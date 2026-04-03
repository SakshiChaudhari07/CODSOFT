def calculator():
    print("CALCULATOR")

    while True:

        print("\nChoose an operation:")
        print("1.Addition(+)")
        print("2.Subtraction(-)")
        print("3.Multiplication(*)")
        print("4.Division(/)")
        print("5.Exit")

        choice=input("Enter your choice:")

        if choice == "5":
            print("Exit...")
            break

        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))

        if choice=="1":
            result = num1+num2
            print(f"{num1}+{num2}={result}")

        elif choice=="2":
            result=num1-num2
            print(f"{num1}-{num2}={result}")

        elif choice=="3":
            result=num1*num2
            print(f"{num1}*{num2}={result}")

        elif choice=="4":
            if num2!=0:
                result=num1/num2
                print(f"{num1}/{num2}={result}")
            else:
                print("Cannot divide by zero!")

        else:
            print("Invalid Input.")

calculator()