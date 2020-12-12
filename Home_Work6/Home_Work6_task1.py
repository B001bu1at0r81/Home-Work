###################################
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
#!!!_______Orest Danysh________!!!#
#!!!________Home-work_6________!!!#
#!!!___________Task_1__________!!!#
#!!!____The_largest_number_____!!!#
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
###################################

def largest_number(number_one, number_two):
    """
        The function that returns
        largest of two numbers.
    """
    if number_one > number_two:
        return number_one
    else:
        return number_two

one = int(input("Enter number one: "))
two = int(input("Enter number two: "))

print(f"The number {largest_number(one, two)} is largest or they`re both the same!")