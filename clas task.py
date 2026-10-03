# 1
# def welcome(func):
#     def inner(*args, **kwargs):
#         print(welcome("Welcome !"))
#         return func(*args, **kwargs)
#     return inner




# @welcome 
# def show_name(name)-> str:
#     return name

# print(show_name("Aziz"))






# 222222222222222222222222222222222

# def goodbye(func):
#     def inner(name):
#         print(func(name))
#         print(goodbye("Welcome !"))
#     return inner


# @goodbye
# def show_name(nam)-> str:
#     return nam

# print(show_name("Good bye !"))






# 3
# def repeat_three_times(repeat):
#     def inner1(func):
#         def inner(*args, **kwargs):
#             for i in range(repeat):
#                 func(*args, **kwargs)
#         return inner
#     return inner1

# @repeat_three_times(3)
# def hello():
#     print("Hello")


# hello()   



# def show_function_name(func):
#     def function_name(a,b):
#         return a+b


#     print(func("Function: add"))
#     print(function_name())



# def add(a,b):
#     print(a,b)
