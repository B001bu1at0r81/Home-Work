###################################
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
#!!!_______Orest Danysh________!!!#
#!!!________Home-work_3________!!!#
#!!!___________Task_2__________!!!#
#!!!__Sorting_numbers_in_list__!!!#
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
###################################

some_number = input("Input some four-digit integer : ")
str_number = str(some_number)
list_number = list(str_number)
# multiplication 
print(f"{str_number[0]} * {str_number[1]} * {str_number[2]} * {str_number[3]} = {int(str_number[0])*int(str_number[1])*int(str_number[2])*int(str_number[3])}")
# Revers
print(f"Revers of {str_number} : {str_number[::-1]}")
# gradation
sorted_list = sorted(list_number)
print(f"Gradation of mumber {some_number} : {sorted_list[0]}{sorted_list[1]}{sorted_list[2]}{sorted_list[3]}")