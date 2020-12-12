###################################
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
#!!!_______Orest Danysh________!!!#
#!!!________Home-work_5________!!!#
#!!!___________Task_2__________!!!#
#!!!______Check_the_login______!!!#
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
###################################

#Task2. Write a script that checks the login that the user enters. 
#If the login is "First", then greet the users. If the login is different, send an error message. 
#(need to use loop while)
while True:
    login = input("Input your login: ")
    if login == "First":
        print("Greetings First and wellcom!")
        break
    else:
        print("Error! You entered wrong login!")
