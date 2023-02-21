import pyinputplus as pyip

print("Calculator Menu")
#print("1. Add")
#print("2. Subtract")
#print("3. Multiply")
#print("4. Divide")


while True: 
    menu= pyip.inputMenu(['Add', 'Subtract', 'Multiply', 'Divide', 'Exit'], numbered=True)


#selection= pyip.inputInt("Choose a numeric selection from above: ", min=1)

    if menu == "Add":
        print("this is the option to add two numbers")
        num1= int(input("Enter the first number: "))
        num2= int(input("Enter the second number: "))
    #total= num1+ num2
        print("The total for those numbers is " + str(num1 +num2))
    elif menu == "Subtract":
        pass
    elif menu == "Multiply": 
        pass
    elif menu == "Divide":
        pass
    elif menu == "Exit":
        break
    else:
        print("Please make a valid selection")



