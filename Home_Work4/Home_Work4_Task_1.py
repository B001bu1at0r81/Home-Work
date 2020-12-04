###################################
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
#!!!_______Orest Danysh________!!!#
#!!!________Home-work_4________!!!#
#!!!___________Task_1__________!!!#
#!!!_________Factorial_________!!!#
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
###################################

entered_number = int(input("Enter integer, please : "))
if entered_number > 0 :
    factorial = 1
    i = 1
    while i <= entered_number:
        factorial *= i
        i+=1
    print(f"factorial of {entered_number} = {factorial}")
else:
    print(f"factorial of {entered_number} = 0")