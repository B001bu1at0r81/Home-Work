###################################
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
#!!!_______Orest Danysh________!!!#
#!!!_______Home-work_10________!!!#
#!!!___________Task_2__________!!!#
#!!!______The_day_of_week______!!!#
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
###################################

def count_days(day):
    """
    docstring
    """
    try:
        if day <= 0 or day > 8:
            raise ValueError("ValueError")
    except ValueError as e:
        print("You entered negative value or number biger then 7, or zero!", e)
    else:
        days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        print(f"Your day is {days[day-1]}!")


try:
    day = int(input("Enter a number of day of week: "))
    count_days(day)
except ValueError as e:
    print("You entered not integer!", e)
except TypeError as e:
    print("You entered not integer!", e)