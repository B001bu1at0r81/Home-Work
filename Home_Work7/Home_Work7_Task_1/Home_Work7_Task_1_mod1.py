###################################
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
#!!!_______Orest Danysh________!!!#
#!!!________Home-work_7________!!!#
#!!!__________Task_1___________!!!#
#!!!_______Area_modul_1________!!!#
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
###################################

from math import pow, pi
def the_square():
    """ 
    The square area.
    """
    f_height = 0
    f_width = 0
    while True:
        height = input("\nPlease, enter the HEIGHT of the square: ")
        if str.isdigit(height) == True:
            f_height = float(height)
            break
        else:
            print("You entered a bad value, try again!")
    while True:
        width = input("Please, enter the WIDTH of the square: ")
        if str.isdigit(width) == True:
            f_width = float(width)
            break
        else:
            print("You entered a bad value, try again!")

    return f_height * f_width

def triangle_square():
    """ The triangle area.
    """
    f_side_one = 0
    f_height = 0
    while True:
        side_one = input("\nPlease, enter the LENGHT of the BASE of the triangle: ")
        if str.isdigit(side_one) == True:
            f_side_one = float(side_one)
            break
        else:
            print("You entered a bad value, try again!")
    while True:
        height = input("Please, enter the HEIGHT of the triangle: ")
        if str.isdigit(height) == True:
            f_height = float(height)
            break
        else:
            print("You entered a bad value, try again!")
    return (f_side_one * f_height) / 2

def circle_square():
    """ The circle area.
    Variables: radius
    """
    f_radius = 0
    while True:
        radius = input("\nPlease, enter the RADIUS of circle: ")
        if str.isdigit(radius) == True:
            f_radius = float(radius)
            break
        else:
            print("You entered a bad value, try again!")
    return round(pi * pow(f_radius, 2), 2)