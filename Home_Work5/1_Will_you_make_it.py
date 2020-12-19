####################################
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
#!!!________Orest Danysh________!!!#
#!!!_________Home-work_5________!!!#
#!!!_______CodeWars_Task_1______!!!#
#!!!______Will_you_make_it?_____!!!#
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
####################################

def zero_fuel(distance_to_pump, mpg, fuel_left):
    #Happy Coding! ;)
    if distance_to_pump == mpg * fuel_left or distance_to_pump <= mpg * fuel_left:
        return True
    else:
        return False