def f1(func):
   def wrapper():
       print("Started")
       func()
       print("Ended")
    return wrapper

@f1
def f():
    f()
   print("Hello")

# def __init __(self,first,last,pay,prog_lang):
#    super().__init __(first,
#    Employee.__init __(self,ast,pay)
#         first,last,pay)
                                              X