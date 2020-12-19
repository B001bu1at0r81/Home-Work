####################################
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
#!!!________Orest Danysh________!!!#
#!!!_________Home-work_6________!!!#
#!!!_______CodeWars_Task_2______!!!#
#!!!_________No_yelling!________!!!#
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
####################################

def filter_words(st):
    # Your code here.
    x = st.lower()
    st = x.replace("'","")
    x = st.capitalize()
    st = x.split()
    x = " ".join(st)
    return x