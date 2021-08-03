from functions import add 
from functions import subtract
from functions import multiply
from functions import divide
from error_handling import handle_division
from error_handling import handle_addition
from error_handling import handle_multiplication
from error_handling import handle_subtraction


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

def main():
    choice = input("Enter choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':

            if num2 == 0:
                handle_division(num2)

            else:
                print(num1, "/", num2, "=", divide(num1, num2))

    else:
        print("Please enter 1, 2, 3, or 4")

if __name__ == "__main__":
    # execute only if run as a script
    main()
print("Would you like to make another calculation?")
while True:
    choice2 = input("Enter choice (yes,no): ")
    if choice2 in ('yes', 'no'):
        if choice2 == 'yes':
            main()
        else:
            print("Bye")
            break
    else:
        print("Please enter yes or no")