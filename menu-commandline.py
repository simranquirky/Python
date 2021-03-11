import os
import pyttsx3

print("\t-----SERVICES WE PROVIDE HERE:-----")
print("\t1. open text editor")
print("\t2. open webbrowser")
print("\t3. open media player")
print("\t4. perform arithmetic operation")
print("\t5. view date and time")
print("\t6. pronounce your inputted statement")
print("\t7. work with basic shapes and figures")
print("\t8. exit")
print("\t-----------------------------------")
print("\tHOW CAN WE HELP YOU..?\n\t(YOU CAN USE STATEMENTS OR WORDS IN ENGLISH AS PER YOUR OWN CONVENIENCE) \n\tCHAT WITH US\t",end='')

while True:
	print("\twhat would you like to work with ? ")
	p=input()
	p=p.lower()
	if (("menu" in p) or ("list" in p)) and ("again" in p):
		print("\t-----SERVICES WE PROVIDE HERE:-----")
		print("\t1. open text editor")
		print("\t2. open webbrowser")
		print("\t2. open webbrowser")
		print("\t3. open media player")
		print("\t4. perform arithmetic operation")
		print("\t5. view date and time")
		print("\t6. pronounce your inputted statement")
		print("\t7. work with basic shapes and figures")
		print("\t8. exit")
		print("\t-----------------------------------")

	elif ("text editor"in p) or ("notepad" in p) or ("document" in p) or ("text file" in p)or ("editor"in p): 
		os.system("notepad")


	elif ("browser" in p) or ("webbrowser" in p):

		print("   Available options for browsers")
		print("\t1.chrome")
		print("\t2.microsoft edge")
		print("\t3.firefox")

	elif "chrome" in p:
			os.system("chrome")

	elif ("edge" in p) or ("microsoft" in p):
			os.system("microsoftedge")

	elif("firefox" in p):
			os.system("firefox")
	elif("media player" in p):
			os.system("wmplayer")


	elif ("arithmetic" in p) or ("calculations" in p) or ("mathematical" in p) or ("operations" in p)or ("maths" in p):

		print("   types of calculation you can perform:")
		print("\t1.adittion")
		print("\t2.multiplication")
		print("\t3.division")
		print("\t4.substraction")
		print("\t5.print multiplication table")
		print("\t6.find factorial of a number")

	elif ("add" in p) or ("addition" in p):
		print("adiition of how many numbers(input in digit)?")
		n=int(input())
		i=1
		sum=0
		while i<=n:
			print("enter value of num",end='')
			print(i," ",end='')
			z=int(input())
			sum=sum+z
			i=i+1
		print("the summation is:",end='')
		print(sum)

	elif ("mul" in p) or ("multiply" in p) or ("multiplication" in p) or ("product" in p):
		print("multiplication of how many numbers(input in digit)?")
		n=int(input())
		i=1
		mul=1
		while i<=n:
			print("enter value of num",i," ",end='')
			z=int(input())
			mul=mul*z
			i=i+1
		print("the product is:",end='')
		print(mul)

	elif ("substract" in p) or ("sub" in p) or ("difference" in p) or ("diff" in p):
		print("enter the two numbers:")
		n1=int(input())
		n2=int(input())
		print("the difference is: ", end='')
		if(n1>n2):
			print(n1-n2)
		else:
			print(n2-n1)

	elif ("division" in p) or ("div" in p) or ("divide" in p) or ("quotient" in p):
		print("enter the two numbers:")
		n1=int(input())
		n2=int(input())
		print("the quotient is: ", end='')
		if(n1>n2):
			print(n1/n2)
		else:
			print(n2/n1)

	elif ("table" in p):
		print("print the multiplication table of which number? ")
		n=int(input())
		i=1
		mul=1
		while i<=10:
			mul=n*i
			print(n," X ",i,"= ",mul)
			i=i+1
	elif ("fact" in p) or ("factorial" in p):
		print("enter the number: ")
		x=int(input())
		z=x
		fact=1
		while x>=1:
			fact=fact*x
			x=x-1
		print("The factorial of ",z,"is ",fact)
#to run date and time commands

	elif ("date" in p) and ("time" in p):
		os.system("date")
		os.system("time")

	elif "date" in p:
		os.system("date")

	elif "time" in p:
		os.system("time")

	elif ("speak" in p) or ("voice" in p) or ("speech" in p) or ("pronounce" in p):
		print("enter your statement: ",end='')
		say=input()
		pyttsx3.speak(say)
	elif ("exit" in p) or ("quit" in p) or (("come" in p) and ("out" in p)):
		break
# the code below is written with a view that the product proves out to be useful while teaching a baby even while one is not connected  # to the internet (I simply wanted to have fun with my knowledge on patterns)
	elif ("shapes" in p) or ("shape" in p) or ("figure" in p):
		print(" the shapes you can work with: ")
		print("\t1.square")
		print("\t2.rectangle")
		print("\t3.triangle")
	elif ("square" in p):
		print("enter the size of the square :")
		x=int(input())
		i=1
		while i<=x:
			print("\t",'- '*x)
			i=i+1
	elif ("rectangle" in p):
		print("enter the length and breadth of the rectangle :")
		x=int(input())
		y=int(input())
		i=1
		while i<=x:
			print("\t",'- '*y)
			i=i+1
	elif ("triangle" in p):
		print("enter the size of the triangle :")
		x=int(input())
		i=1
		while i<=x:
			print("\t",'  '*(x-i),end='')
			print('- '*i)
			i=i+1
	else:
		print("WE DO NOT SUPPORT ANY SUCH SERVICES")
