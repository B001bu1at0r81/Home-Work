###################################
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
#!!!_______Orest Danysh________!!!#
#!!!________Home-work_3________!!!#
#!!!___________Task_1__________!!!#
#!!!____"The_Zen_of_Python"____!!!#
#!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!#
###################################



# Home work
# 1. Записати в стрічку філософію пайтона
# 2. Порахувати кількість слів (better, never, is) 
# 3. Вивести текст у верхньому регістрі 
# 4. Замінити всі "і" на "&" 

# 1. Записати в стрічку філософію пайтона
zen_of_python = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
print(zen_of_python)

# 2. Порахувати кількість слів (better, never, is)
uper_zen = zen_of_python.upper()
list_of_up_zen = uper_zen.split()
num_better = list_of_up_zen.count("BETTER") + list_of_up_zen.count("BETTER.")
num_never = list_of_up_zen.count("NEVER") + list_of_up_zen.count("NEVER.")
num_is = list_of_up_zen.count("IS") + list_of_up_zen.count("IS.")
# Я помітив, що метод спліт вважає "NEVER." одним словом, 
# тому доводиться перевіряти і "NEVER" і "NEVER.".

print(f'The quantity of "better" is: {num_better}')
print(f'The quantity of "never" is: {num_never}')
print(f'The quantity of "is" is: {num_is}')
# 3. Вивести текст у верхньому регістрі
print(uper_zen)
# 4. Замінити всі "і" на "&" .replace("i","&")
#Великі букви теж міняти?
#replace_i = zen_of_python.replace("I","&")
#print(replace_i.replace("i","&"))
print(zen_of_python.replace("i","&"))