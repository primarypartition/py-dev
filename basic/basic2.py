######################################
### compare
######################################


# print(1 > 2)
# print(1 < 2)
# print(1 >= 1)
# print(1 <= 4)
# print(1 == 1)
# print(1 == "1")
# print(1 != 2)

# print((1 > 2) and (2 < 3))
# print((1 > 2) or (2 < 3))

# if 1 > 2:
  # print('Vivamus!')
# elif 3 > 4:
    # print('Aliquam')
# else:
  # print('Pellentesque!')


######################################
### loops
######################################


# seq = [1, 2, 3, 4, 5]

# for item in seq:
    # print(item)
    
# ages = {"Sam":3,"Frank":4,"Dan":29}

# for key in ages:
    # print("This is the key", key)
    # print("This is the value", ages[key])
       
# mypairs = [(1,10),(3,30),(5,50)]

# for tup in mypairs:
    # print(tup)

# for (item1, item2) in mypairs:
    # print(item1, item2)
    
# i = 1
# while i < 5:
    # print('i is: {}'.format(i))
    # i = i+1    
    
# start = 0
# end = 10
# step = 2

# for i in range(start, end, step):
    # print(i)

# x = [1,2,3,4]

# [item**2 for item in x]


######################################
### Functions
######################################


# def func1():
    # '''
      # What function does
    # '''
    # print("Sed vel ipsum at nisl pulvinar finibus.")
    
# func1()

# def func2():
    # return ("Sed vel ipsum at nisl pulvinar finibus.")

# print(func2())

# def func3(name):
    # return ("Sed vel ipsum at nisl pulvinar finibus." + name)

# print(func3("joe"))

# def func3(name="not"):
    # return ("Sed vel ipsum at nisl pulvinar finibus." + name)

# print(func3())


######################################
### lambda
######################################


# my_list = [1,2,3,4,5,6,7,8,9,10]

# def evenBool(num):
    # return num%2 == 0

# print(evenBool(2))

# evens = filter(evenBool, my_list)

# print(list(evens))

# lambda input: output = input

# evens = filter(lambda num: num%2==0, my_list)
# print(list(evens))
