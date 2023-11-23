# иф элста барлық шарт орындалуы Тиысты емес 
# линейный деген циклда ифта болмаса жорлдар кайталанып орындалып шығады
# if шарт орындалмаса элс орындалады
# elif иф пен элстың ортасында тұрады 
# иф та елиф та орындалмаған кезде элс орындалады
# бірнеше элиф болуға болады

# Nasted codition 
#  == - тең болса тру, екі санның тең екенін тексереді тең болса тру тең емес болса фолс
# = 1 шт тең болса сан

# if condition and Logical Operators
# and - көр шарттарды бірден бір жолға жазамыз барлық шарттар орындалу керек, көбейту 
# or - тоже көп шарттар жазамыз бірақ + 
#  
# true 


# CLASS WORK
# age = int(input("Enter your age"))
# if age >= 18  and  age > 0:
#     print("You are old enought to learn to drive")
# elif age < 18 and age > 0:
#     print("You are old enought to learn to drive")
# else:
#     print("the digits must be more than zero")
#     if age < 0:
#         print("the digits must be more than zero")
# else: 
#     age < 18
#     d = 18 - age 
#     print(f"You need {d} more yers to learn to drive")
# 2
# my_age = 17
# age = int(input("Enter your age"))
# if my_age > age and  age < 0 and:
#     d = my_age - age
#     print(f"me {d} y.o than you")
#     if age < 0:
#         print("the digits must be more than zero")
# else:
#     my_age < age
#     z = age - my_age
#     print(f"you are {z} y.o than me")

# age = int(input("Enter your age"))
# my_age = 17
# if my_age > age and age > 0:
#     d = my_age - age
#     print(f"me {d} y.o than you")
# elif age > my_age and my_age > 0:
#     z = age - my_age
#     print(f"you are {z} y.o than me")
# else:
#     ("mistake")

# 3
one = int(input("number input"))
two = int(input("number input"))
if one > two:
    print(f"{one} is greater than {two}")
elif two > one:
    print(f"{two}is greater than{one}")
else:
    print(f"{one} is qually than {two}")