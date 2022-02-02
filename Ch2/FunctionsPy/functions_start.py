# Exercise file for Python for the C# Developer LinkedIn Learning course by Joe Marini

# functions are defined using the def keyword, then
# the : character and whitespace define the function body
def myfunction():
    print("This is a line in my function")
    return 123

def myvoidfunction(a, b):
    print("This function returns nada")
    print(a+b)

retval = myfunction()
print(retval)

retval = myvoidfunction(1, 2)
print(retval)