####################################
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
#!!!________Orest Danysh________!!!#
#!!!_________Home-work_7________!!!#
#!!!_______CodeWars_Task_1______!!!#
#!!!_____Count_of_positives_____!!!#
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
####################################

def count_positives_sum_negatives(arr):
    #your code here
    if len(arr) != 0:
        positive=0
        negative=0
        for item in arr:
            if item > 0:
                positive += 1
            elif item < 0:
                negative += item
        arr1 = [positive, negative]
    else:
        arr1 = arr
    return arr1

arr = [0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]
print(count_positives_sum_negatives(arr))

