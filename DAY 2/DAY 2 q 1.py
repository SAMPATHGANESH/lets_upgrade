#DAY 2 
# 5 Different functions of the String in Python.
# + is used for adding of strings 
print("1.concatenation")
name = "sampath ganesh kandregula"
address = " lives in vizag andhrapradesh"
print(name + address)
#split is used for divison of functions
print("2.split function")
splitfunction = name.split()
print(splitfunction)
#indexing is used for recognizing a position of a character 
print("3.indexing")
print(name[1])
print(name[0])
print(name[-1])#we can also use negative indexing from backward too 
print(name[-11])#in python space is also considered as a character we can access by using that too "negative indexing"
#we can find length of string  by using len()
print("4.length function ")
print(len(name))
print(len(address))
print(len(address)- len(name))
print(len(address)+len(name))#we can do any type of arthimetic functions using strings 
#capitalize the first letter of a name
print("5.capitalize function")
b = name.capitalize()
print(b)
#count function is used for no of times does a single character is repeated
print("6.count function ") 
x = name.count("a")
print(x)




