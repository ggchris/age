drive=input("drive?")
if drive!="yes" and drive!="no":
	print("yes or no")
	raise SystemExit
age=input("age?")
age=int(age)
if drive=="yes":
	if age >=18:
		print("ok")
	else:
		print("No")
elif drive=="no":
    if age>=18:
      	print("18 no")
    else:
    	print(">18 no")
else:
	print("yes or no")


