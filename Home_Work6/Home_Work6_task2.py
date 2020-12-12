###################################
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
#!!!_______Orest Danysh________!!!#
#!!!________Home-work_6________!!!#
#!!!__________Task_2___________!!!#
#!!!___________Area____________!!!#
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
###################################

def the_square():
    """ 
    The square area.
    """
    height = int(input("\nPlease, enter the HEIGHT of the square: "))
    width = int(input("Please, enter the WIDTH of the square: "))
    return height * width

def triangle_square():
    """ The triangle area.
    """
    side_one = int(input("\nPlease, enter the LENGHT of the BASE of the triangle: "))
    height = int(input("Please, enter the HEIGHT of the triangle: "))
    return (side_one * height) / 2

def circle_square():
    """ The circle area.
    Variables: radius
    """
    radius = int(input("\nPlease, enter the RADIUS of circle: "))
    return 3.14 * radius ** 2

print("The program that calculates area of ​​a rectangle, a triangle and a circle.")
while True:
    users_choice = str(input("\nInput:\n\t1 - if you want to calculate a square area.\n\
        2 - if you want to calculate a squire of triangle.\n\
        3 - if you want to calculate a square of circle.\n\
        4 - for exit.\n\
    Please, make your choice: "))
    if users_choice == "1":
        print(f"\nThe square area is {the_square()}")
    elif users_choice == "2":
        print(f"\nThe triangle area is {triangle_square()}")
    elif users_choice == "3":
        print(f"\nThe circle area is {circle_square()}")
    elif users_choice == "4":
        break
    else:
        print("You enter wrong symbol! Please, try again.")