###################################
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
#!!!_______Orest Danysh________!!!#
#!!!________Home-work_7________!!!#
#!!!__________Task_1___________!!!#
#!!!_______Area_modul_2________!!!#
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
###################################

import Home_Work7_task1_mod1 as f

print("The program that calculates area of ​​a rectangle, a triangle and a circle.")
while True:
    users_choice = str(input("\nEnter:\n\t1 - if you want to calculate a square area.\n\
        2 - if you want to calculate a squire of triangle.\n\
        3 - if you want to calculate a square of circle.\n\
        4 - for exit.\n\
    Please, make your choice: "))
    if users_choice == "1":
        print(f"\nThe square area is {f.the_square()}")
    elif users_choice == "2":
        print(f"\nThe triangle area is {f.triangle_square()}")
    elif users_choice == "3":
        print(f"\nThe circle area is {f.circle_square()}")
    elif users_choice == "4":
        break
    else:
        print("You enter wrong symbol! Please, try again.")