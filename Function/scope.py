
#local scope

# def my_func():
#     my_var= 10 #locally scope to my_func
#     print(my_var)

# my_func()

# print(my_var) #its local scope

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

def outer_fn():
    msg="Hello" #msg is in enclosing scope
    def inner_fn():
        print(msg)
    inner_fn()
outer_fn()