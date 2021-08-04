from functions import add
from functions import subtract
from functions import divide
from functions import multiply

total = 0

def calculator():
    menu = True
    x = 0
    while menu:
        float(x)
        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5. Quit")
        choice = input("Enter choice: ")
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter a number: "))

            if choice == '1':
                x = add(x, num1)
                print('=', x)

            elif choice == '2':
                x = subtract(x, num1)
                print('=', x)

            elif choice == '3':
                x = multiply(x, num1)
                print('=', x)

            elif choice == '4':
                x = divide(x, num1)
                print('=', x)
            
            
        elif choice =='5':
            print("Your total is: ", x)
            menu = False
            break
        else:
            break




calculator()
