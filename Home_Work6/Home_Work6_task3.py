###################################
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
#!!!_______Orest Danysh________!!!#
#!!!________Home-work_6________!!!#
#!!!__________Task_3___________!!!#
#!!!___Charecters_calculate____!!!#
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
###################################

def string_calc(users_string):
    """ The function that calculates characters in the string.
    """
    number = 0
    for item in users_string:
        number += 1
    return number

print("The function that calculates characters in the string.")
users_string = input("Please, enter some text: ")
print(f"Your string has {string_calc(users_string)} characters.")