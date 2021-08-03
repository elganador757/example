from functions import add 
from functions import subtract
from functions import multiply
from functions import divide
from error_handling import handle_division
from error_handling import handle_addition
from error_handling import handle_multiplication
from error_handling import handle_subtraction

def main():
    print (add(2,3))
    print (subtract(3,2))
    print(multiply(2,3))
    print(divide(4,3))

if __name__ == "__main__":
    # execute only if run as a script
    main()
