x=5
y=6
print(x)
print(y)

#String variables can be declared either by using single or double quotes
#Python allows you to assign values to multiple variables in one line:

x,y,z='blue','white','red'
print(x)
print(y)
print(z)

x=y=z='pink'
print(x)
print(y)
print(z)

"""
Output Variables,the Python print statement is often used to output variables.
To combine both text and a variable, Python uses the + character
"""

x="lit"
print("python is " + x)

#You can also use the + character to add a variable to another variable:
x='python is '
y='lob'
z=x + y
print(z)


#If you try to combine a string and a number, Python will give you an error:

#Global Variables

x="love"

def myfunc():
    print('python is ' +x)
    myfun()

x='lit'
def myfunc():
     x='awesome'
     print("python is" +x)
myfunc()

print("python is " +x)


#using global veriable

def myfunc():
    global x
    x="noice"
    myfun()
print('python is' +x)


#To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x="noice"
def myfunc():
    global x
    x="pok"

myfunc()

print("python is " +x)
