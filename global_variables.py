# Write your code here :-)
a = 10 # global variable
b = 5  # global variable
c = 0
def add():
    global c
    a = 1 # local variable
    b = 2 # local variable
    print(a)
    print(b)
    c = a + b # global variable used
    print(c)

add()
print(a)
print(b)
print(c)
