from functions import add
from functions import subtract
from functions import divide
from functions import multiply

total = 0
x = 0


def calculator():
    menu = True
    while menu:
        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5. Quit")
        choice = input("Enter choice: ")
        if choice in ('1', '2', '3', '4','5'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                x = print(num1, "+", num2, "=", add(num1, num2))

            elif choice == '2':
                x = print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == '3':
                x = print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == '4':
                x = print(num1, "/", num2, "=", divide(num1, num2))
            
            elif choice == '5':
                print(choice)
                menu = False
                print("dfjklafdjklj")
                break
            else:
                print(choice)
                print("else statement")
                menu = False
                break 
        elif choice =='5':
            print('bye')
            menu = False
            break
        else:
            break




calculator()
