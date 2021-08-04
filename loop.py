from functions import add
from functions import subtract
from functions import divide
from functions import multiply
from error_handling import handle_division

total = 0

def calculator():
    menu = True
    x = 0
    while menu:
        float(x)
        # Make menu text a single varible in variable file
        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5. Quit")
        choice = input("Enter choice: ")
        if choice in ('1', '2', '3', '4'): # use list [] in variables

            # define list of functions 
            num1 = float(input("Enter a number: "))
            #functions = [add, subtract, multiply, divide]
            #x = functions[int(choice)](x, num1)
            if choice == '1':
                print(x, "+", num1, "=", add(x, num1))
                x = add(x, num1)

            elif choice == '2':
                print(x, "-", num1, "=", subtract(x, num1))
                x = subtract(x, num1)

            elif choice == '3':
                print(x, "*", num1, "=", multiply(x, num1))
                x = multiply(x, num1)

            elif choice == '4':
                if num1 != 0:
                    print(x, "/", num1, "=", divide(x, num1))
                    x = divide(x, num1)
                elif num1 == 0:
                    handle_division(num1)
            
            
        elif choice =='5':
            print("Your total is: ", x)
            menu = False
            break
        else:
            break




calculator()
