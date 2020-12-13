#filehandling
infinity = open("sampathfile.txt",'w')
infinity.write("I LOVE LETSUPGRADE")#WRITING
infinity.close()
#reading
infinity = open('sampathfile.txt','r')
content = infinity.read()
infinity.close()
print(content)
#Appending
infinity = open('sampathfile.txt','a')
infinity.write(" this is an amazing platform to learn coding but some the price is so high but loved your free courses")
infinity.close()
#reading
infinity = open('sampathfile.txt','r')
content = infinity.read()
infinity.close()
print(content)
