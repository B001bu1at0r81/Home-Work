###################################
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
#!!!_______Orest Danysh________!!!#
#!!!________Home-work_4________!!!#
#!!!___________Task_3__________!!!#
#!!!_____Fibonacci_number______!!!#
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
###################################
quantity_of_numbers = int(input("Input number of members : "))
fibonacci = [0, 1]
temp = 0
i = 2 #оскільки пеших два числа Фібоначчі у нас вже є, то починаємо з третього
while i < quantity_of_numbers:
    temp = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.insert(i, temp)
    i += 1

for item in fibonacci:
    print(item)