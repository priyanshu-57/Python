
#local scope

# def my_func():
#     my_var= 10 #locally scope to my_func
#     print(my_var)

# my_func()

# print(my_var) #its local scope ,NameError: name 'my_var' is not defined

#enclosing Scope

# def num():
#     n= 5  #enclosing scope
#     def odd():
#         if n % 2 ==0:
#             print("not odd")
#         else:
#             print("odd")
#     odd()
# num()

#example

# def outer_fn():
#     msg="Hello" #msg is in enclosing scope
#
#     def inner_fn():
#         print(msg)
#     inner_fn()
#
# outer_fn()

# #Global scope

# my_var= 1

# def show_var():
#     print(my_var)

# show_var()

# using "global keyword"

my_var_1= 2

def show_var():
    global my_var_2
    my_var_2= 6
    print(my_var_1)
    print(my_var_2)

show_var()
print(my_var_2)

