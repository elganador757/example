
def menu_selection_error(a): 
    """if input is a non-empty string, throw an error"""
    if a < 1 or a > 5:
             print("'\033[91m'ERROR:'\033[92m'Invalid input! Please select from the menu")


def handle_division(a):
    """makes sure number is not zero"""
    if a == 0:
        print("'\033[91m'ERROR:'\033[92m'Cannot divide by zero!")
    
menu_selection_error(45)
menu_selection_error(4)

handle_division(0)