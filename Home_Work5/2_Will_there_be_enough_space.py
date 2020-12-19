####################################
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
#!!!________Orest Danysh________!!!#
#!!!_________Home-work_5________!!!#
#!!!_______CodeWars_Task_2______!!!#
#!!!_Will_there_be_enough_space?!!!#
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
####################################

def enough(cap, on, wait):
    # Your code here
    num = wait - (cap - on)
    if num <= 0:
        return 0
    else:
        return num
    