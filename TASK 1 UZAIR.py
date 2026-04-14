def greet(name):
    print(f"Hello {name}")


greet("haseeb")
def my_function():
    x = 10
    print(x)

my_function()

y = 20

def access_global():
    print(y)

access_global()
def modify_global():
     global y
     y = 30

modify_global()
print(y)