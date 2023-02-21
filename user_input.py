
print("Calculator Menu")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True: 
    selection= input("Please enter your selection based on the numeric values above: ")
    try: 
        selection= int(selection)
    except: 
        print("Please choose one of the numeric values above")
        continue

    if selection < 1: 
        print("Please enter a number that is greater than 0")
        continue
    break

if selection == 1:
    print("this is the option to add two numbers")
    num1= int(input("Enter the first number: "))
    num2= int(input("Enter the second number: "))
    #total= num1+ num2
    print("The total for those numbers is " + str(num1 +num2))
elif selection == 2:
    pass
elif selection == 3: 
    pass
elif selection == 4:
    pass
else:
    print("Please make a valid selection")