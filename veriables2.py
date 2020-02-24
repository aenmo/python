


#To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x="noice"
def func():
    global x
    x="pok"

myfunc()

print("python is " +x)
