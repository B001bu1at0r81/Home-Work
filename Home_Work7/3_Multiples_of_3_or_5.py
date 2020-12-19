####################################
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
#!!!________Orest Danysh________!!!#
#!!!_________Home-work_7________!!!#
#!!!_______CodeWars_Task_3______!!!#
#!!!_____Multiples_of_3_or_5____!!!#
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
####################################

def solution(number):
    div_items = 0
    for item in range(number):
        if item % 3 == 0 or item % 5 == 0:
            div_items += item

    return div_items

l = 10
print(solution(l))