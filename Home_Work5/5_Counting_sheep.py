####################################
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
#!!!________Orest Danysh________!!!#
#!!!_________Home-work_5________!!!#
#!!!_______CodeWars_Task_5______!!!#
#!!!_______Counting_sheep_______!!!#
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
####################################

def count_sheeps(sheep):
  # TODO May the force be with you
    real_sheep_counter = 0
    for item in range(len(sheep)):
        if sheep[item] == True:
            real_sheep_counter += 1
    
    return real_sheep_counter
    