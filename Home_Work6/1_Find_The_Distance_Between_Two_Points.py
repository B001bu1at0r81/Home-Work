####################################
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
#!!!________Orest Danysh________!!!#
#!!!_________Home-work_6________!!!#
#!!!_______CodeWars_Task_1______!!!#
#!!!______Find_the_distance_____!!!#
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
####################################

from math import sqrt, exp
def distance(x1, y1, x2, y2):
    # Your code here
    x = x1 - x2
    y = y1 - y2
    length = sqrt(x**2 + y**2)
    return round(length, 2)