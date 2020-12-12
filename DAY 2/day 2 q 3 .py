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


