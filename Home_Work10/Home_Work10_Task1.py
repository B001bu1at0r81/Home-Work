def odd_or_even(age):
    try:
        if age < 0:
            raise ValueError("Valueerror")
    except ValueError as e:
        print("You entered negative value!", e)
    else:
        if age % 2 == 0:
            print("Your age is even!")
        elif age % 2 != 0:
            print("Your age is odd!")

try:
    age = int(input("Enter your age: "))
    odd_or_even(age)
except ValueError as e:
    print("You entered not integer!", e)
except TypeError as e:
    print("You entered not integer!", e)