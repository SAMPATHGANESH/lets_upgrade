#DAY 2 	QUEOSTION 1 
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
#####DAY 2 QUEOSTION 2 
Try 5 Different functions of the List object in Python
vowels = ['a','e','i','o','u']
numbers = [11,21,31,45,55,65,17]
print("vowels = " , vowels)
print("numbers = " , numbers)
#len of list tells how many items are in list 
print("1.length of list ")
print(len(vowels))
print(len(numbers))
print(len(vowels)*len(numbers))
#type is a function used for  the finding type of a function 
print('2.type finding ')
print(type(numbers))
print(type(numbers[2]))
print(type(vowels))
#insert is used for  creating a new variable in list
print("3.new variable")
vowels.insert(2,"sampath")
print( vowels)
#reverse is used for the reversing of the list 
print("4.reversing")
numbers.reverse()
print(numbers)
#sort is used for the keeping the elements in ascending order 
print("5.sort in list ")
numbers.sort()
print(numbers)
#pop is a function in alist used to remove a element in list
print("6.pop in list")
vowels.pop(2)
print(vowels)
####DAY 2 QUEOSTION 3
#Experiment with at least 5 default functions of Dictionary
details = {'name': "sampath","branch":"mechatronics","roll.no":3211 }
print(details)
print(type(details))
#values is a default function in dictionary prints values 
print("1.values")
x = details.values()
print(x)
#copy is a default function in dictionary copies characters 
print("2.copying")
y = details.copy()
print(y)
#we can change the value of a character in string using this 
print("3.updating ")
details['roll.no'] = 3000 + 200 +10 + 2
print(details)
#or we can use update value 
details.update({"name":"sampath ganesh kandregula" ,"roll.no":3211})
print(details)
#we can remove the last element using pop  
print("4.removing elements")
details.popitem()
print(details)
#we can get the key values using key function
z  = details.keys()
print(z)



