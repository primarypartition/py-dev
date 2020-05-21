x = 50
y = 200

def func():
    global x
    y = 250
    print('This function is now using the global x!')
    print('Because of global x is: ', x)
    print('y is: ', y)    
    x = 150
    print('Ran func(), changed global x to', x)

print('Before calling func(), x is: ', x)
func()
print('Value of x (outside of func()) is: ', x)

print('Value of y (outside of func()) is: ', y)
