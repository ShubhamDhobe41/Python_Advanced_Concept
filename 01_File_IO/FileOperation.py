""" Reading a file """

# f = open("demo.txt", "r")
## read entire file
# data = f.read()#welcome
# print(data)
# print(type(data))
# f.close()

# f = open("demo.txt", "r+")
# data = f.read(5)#welco
# print(data)
# print(type(data))
# f.close()

# f = open("demo.txt", "r+")
# line1 = f.readline() # read line by line
# print(line1)
# line2 = f.readline()
# print(line2)
# line3 = f.readline()
# print(line3)
# f.close()



"""  writing a file """

# f = open("demo.txt", "w")
# data = f.write("this is a new line ")
# print(data)
# f.close() # overwrite entire file

# f = open("demo.txt", "a")
# data = f.write("\n this is a new line ")
# print(data)  # add to the file
# f.close()

# create a new file
# f = open("sample.txt", "a")
# f.close()


# new syntax for create , write and read
# with open("demo.txt", "w") as f:
#     data =f.write("this is a new data ")
#     print(data)


# deleting a file use os module
# import  os
# os.remove("demo.txt")

"""create a new file "practice.txt" using python . add the data 
hi everyone 
we are learning file i/o 
using python 
i like python programming"""
# with open("practice.txt","a") as f :
#     f.write(" \n hi everyone \n we are learning file i/o  using python  \n i like python programming")
