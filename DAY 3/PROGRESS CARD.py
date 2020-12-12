##Use IF ELSE and ELIF to write a program in python for your Report Cards.
marks = int(input())
x = 50 - marks
y = str(x)
print(x)
if marks >=90 :
     print("Grade A ")
elif marks >=80:
	print("Grade B")
elif marks >= 70:
	print("Grade c")
elif marks>=60:
	print("Grade D")
elif marks >=50:
	print("Grade E")
else :
	print("you are failed in exam to qualify you need " +y, "marks to pass ")
print("THE ABOVE ONE IS USED TO FIND GRADES IN PROGRESS CARD 😅😅")