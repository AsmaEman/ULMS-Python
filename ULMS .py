List_of_codes=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
List_of_Names=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
List_of_creditHours=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
List_of_sem=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
List_of_users=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
List_of_passwords=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
global x
global j
global a
global b
global y
global S
print("**Welcome to University Learning Managment System**")
print("Dear User, current software is intended for authorised users only.")
print("Login the system to get access.")
def Load_User():
	import os
	filePath='user.txt'
	if os.path.exists('user.txt'): 
		#print("The file exist")
		file = open('user.txt')
		for lines in file:
			l=lines
		
	else:
		print("The file does not exist")
	with open('user.txt','r') as rf:
		n=str(input("Username:"))
		p=str(input("Password:"))
		l=lines
		if n==l and p==l :
			print("n")
			print("p")
			print("You have successfully logged into system.")
		else:
			print("DearUser, username/password is incorrect.")
			print("Enter username/passwordagain to get access to the system.")
	return()
Load_User()
		
def isValidCourseCode():
	global j
	j=str(input("enter code: "))
	index=y
	Uppercase_Characters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	Numeric_Characters=['0','1','2','3','4','5','6','7','8','9']
	def length_of_string(t):
		counter = 0
		for a in t:
			counter = counter + 1
		return counter
	if length_of_string(j)==5:
		if (j[0:1] in Uppercase_Characters) and (j[2:3:4] in Numeric_Characters) :
			List_of_codes[y]=j
		else:
			print("Invalid code")
	else:
		print("Invalid code")
	return True
def isValidName():
	global x
	#y is index
	List_of_lc=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
	x=str(input("subject to be selected: "))
	n=0
	Uppercase_Characters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	for letter in x:
		n+=1
	if (x[0:1:2] in List_of_lc) and (x[0] in  Uppercase_Characters) :
		List_of_Names[y]=x
	else:
		print("Invalid Name")
	return True
def isValidCreditHours():
	global a
	a=int(input("enter credit Hours"))
	Num=[1,2,3]
	if a in Num:
		List_of_creditHours[y]=a
	else:
		print("Invalid CreditHours")
	return True
def isValidsemesters():
	global b
	b=int(input("semester"))
	available_sem=[0,1,2,3,4,5,6,7,8]
	if b in available_sem:
		List_of_sem[y]=b
	else:
		print("Invalid Semester")
	return True
isValidCourseCode
isValidName
isValidCreditHours
isValidsemesters

def Add_Course():
	print("Enter course details:")
	isValidCourseCode()
	isValidName()
	isValidCreditHours()
	isValidsemesters()
	s=[j,x,a,b]
	print("your course details ",s)
	return(s)
def Update_Course():
	
	s=int(input("course to be changed: "))
	List_of_codes[s]=0
	List_of_Names[s]=0
	List_of_creditHours[s]=0
	List_of_sem[s]=0
	Uppercase_Characters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	Numeric_Characters=['0','1','2','3','4','5','6','7','8','9']
	n=str(input("enter code: "))
	if (n[0:1] in Uppercase_Characters) and (n[2:3:4] in Numeric_Characters):
		List_of_codes[s]=n
		f=str(input("enter name"))
		List_of_Names[s]=f
	else:
		while (n[0:1] in Uppercase_Characters) and (n[2:3:4] in Numeric_Characters):
			n=str(input("enter code: "))
		List_of_codes[s]=n
		f=str(input("enter name"))
		List_of_Names[s]=f
	Num=[1,2,3]
	v=int(input("enter credit hours"))
	if (v in Num):
		List_of_creditHours[s]=v
	else:
		while (v in Num):
			v=int(input("enter credit hours"))
		List_of_creditHours[s]=v
	available_sem=[0,1,2,3,4,5,6,7,8]
	c=int(input("enter semester"))
	if  (c in available_sem):
		List_of_sem[s]=c
	else:
		while (c in available_sem):
			c=int(input("enter semester"))
		List_of_sem[s]=c
	print("your course "+str(s)+" has been updated to : ",List_of_codes[s],List_of_Names[s],List_of_creditHours[s],List_of_sem[s])
		

				
def Delete_Course():
	s=int(input("course to be deleted: "))
	List_of_codes[s]=0
	List_of_Names[s]=0
	List_of_creditHours[s]=0
	List_of_sem[s]=0
	List_of_codes[s] = List_of_codes[0]
	List_of_Names[s]= List_of_Names[0]
	List_of_creditHours[s] = List_of_creditHours[0]
	List_of_sem[s] = List_of_sem[0]
	List_of_codes[0]=0
	List_of_Names[0]=0
	List_of_creditHours[0]=0
	List_of_sem[0]=0
def View_Courses():
	l=0
	print(         "COURSE_CODE  ","COURSE_NAME  ","CREDIT_HOURS  ","SEMESTER")
	while l<y:
		if  Add_Course:
			S=(           str(List_of_codes[l])+"          ",str(List_of_Names[l])+"       ",str(List_of_creditHours[l])+"           ",str(List_of_sem[l]))
			print(S)
		l+=1

def View_Courses_of_a_semester():
	n=int(input("choose semester: "))
	print("COURSE_CODE ","COURSE_NAME ","CREDIT_HOURS ")
	e=0
	n=0
	y=5
	while n<y:
		if n==List_of_sem[e]:
			print((List_of_codes[e])+"        "+(List_of_Names[e])+"             "+str(List_of_creditHours[e]))
		n+=1
		y-=4
def Exit_program():
	print("                                     END                                                      ")
	quit()
	return()

def Save_Courses():
	with open('courses.txt') as wf:
		l =0
		global y
		file='courses.txt'
		if l<y:
			S=(           str(List_of_codes[l])+"          ",str(List_of_Names[l])+"       ",str(List_of_creditHours[l])+"           ",str(List_of_sem[l]))
			file=open('courses.txt','w')
			file.write(str(S))
			if y>1:
				S1=(           str(List_of_codes[l+1])+"          ",str(List_of_Names[l+1])+"       ",str(List_of_creditHours[l+1])+"           ",str(List_of_sem[l+1]))
				file.write("\n")
				file.write(str(S1))
			if y>2:	
				S2=(           str(List_of_codes[l+1])+"          ",str(List_of_Names[l+1])+"       ",str(List_of_creditHours[l+1])+"           ",str(List_of_sem[l+1]))
				file.write("\n")
				file.write(str(S2))
		else:
			print('This file does not exist')
		y+=1

	return()
def Load_Courses():
	import os
	filePath='courses.txt'
	if os.path.exists('courses.txt'): 
		file = open('courses.txt','r')
		for lines in file:
			print(lines)
	else:
		print("The file does not exist")
	return()


y=0
g=0
l=0
Load_User()
while g<=6:
	print("1 ","add_course") 
	print("2 ","Update_Course") 
	print("3 ","Delete_course") 
	print("4 ","View_all_courses") 
	print("5 ","View_courses_of_semester")
	print("6 ","Logout the system")
	print("7 ","Exit_program")
	g = int(input("Choose the option: "))
	if g==1:
		Add_Course()
		y+=1
	if g==2:
		Update_Course()
	if g==3:
		Delete_Course()
	if g==4:
		View_Courses()
		Load_Courses()
		
	if g==5:
		View_Courses_of_a_semester()

	if g==6:
		print("Logout")
	if g==7:
		Save_Courses()
		Exit_program()
		