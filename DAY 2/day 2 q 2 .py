#Try 5 Different functions of the List object in Python
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