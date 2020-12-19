###################################
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
#!!!_______Orest Danysh________!!!#
#!!!________Home-work_5________!!!#
#!!!___________Task_1__________!!!#
#!!!_______Rage division_______!!!#
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
###################################

#Task1. In the range from 1 to 10 determine 
#even numbers that are divisible by 2,
#odd numbers, which are divisible by 3,
#numbers that are not divisible by 2 and 3.
my_list = [item for item in range(1,11)]
even_num = []
odd_num = []
other_num = []
for item in range(len(my_list)):
    if my_list[item] % 2 == 0:
        even_num.append(my_list[item])
    elif my_list[item] % 3 == 0:
        odd_num.append(my_list[item])
    else:
        other_num.append(my_list[item])
print(even_num)
print(odd_num)
print(other_num)