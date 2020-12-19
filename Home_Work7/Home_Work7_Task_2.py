###################################
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
#!!!_______Orest Danysh________!!!#
#!!!________Home-work_7________!!!#
#!!!___________Task_2__________!!!#
#!!!___________RegEx___________!!!#
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
###################################

import re
def f_validator(user_pass):
    """
    Password validator
    Parematers: user_pass
    """
    valid = False
    
    if re.search(" ", user_pass) != None:
        print("Your password contain spaces.")
        return False
    elif len(user_pass) < 6 or len(user_pass) > 16:
        print("Your password must contain at least 6 characters but no more than 16 characters.")
        return False

    l_items = ["[A-Z]", "[a-z]", "[0-9]"]
    for item in l_items:
        if re.search(item, user_pass) == None:
            print("Your password must contain at least: \n1 letter between [a-z].\n1 letter between [A-Z]. \n1 number between [0-9].")
            return False
    l_items = ["$", "#", "@"]
    for item in l_items:
        if re.search(item, user_pass) != None:
            print("Your password is valid!")
            return True
        else:
             print("Your password must contain at least: 1 character from [$#@].")
             return False    


    #result = re. match(r"", user_pass)
    #if re.match(r" ",) and 


print("Password validaotor.")
validator = False
while True:
    user_pass = str(input("Enter password: "))
    if user_pass:
        validator = f_validator(user_pass)
    if validator == True:
        break
    else:
        print("Try again.")
    
#[0-9A-Fa-f]
