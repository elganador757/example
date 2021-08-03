
def type_error(a): 
    """if input is a non-empty string, throw an error"""
    if type(a) is str and a != "":
            raise TypeError("Invalid input. please enter a number and press enter")


def handle_division(a):
    """converts number into floating-point type for precision. checks input to make sure it's a number. makes sure number is not zero"""
    if type(a) == int:
        a = float(a)
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    type_error(a)

def handle_addition(a):
    """make sure input is a number"""
    type_error(a)

def handle_multiplication(a):
    """make sure input is a number"""
    type_error(a)

def handle_subtraction(a):
    """make sure input is a number"""
    type_error(a)

