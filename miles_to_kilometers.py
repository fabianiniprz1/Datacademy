#conversor kilometers to miles

def converter(selection,amount):
	if selection == 1:
		result = amount/1.609344
		print (str(amount)+" kilometers are equal to " + str(result) + " miles" )
	elif selection ==2:
		result = amount*1.609344
		print (str(amount)+" miles are equal to " + str(result) + " kilometers" )

def make_convert():
	selection = int(input("What would you like to do? \n1.Kilometers to miles \n2.Miles to kilometers"))

	if selection == 1:
		amount = float(input("How many kilometers do you want to convert?: "))
	if selection == 2:
		amount = float(input("How many miles do you want to convert?: "))

	converter(selection,amount)

	selection = int(input("Would you like to convert another measure? \n1.Yes \n2.No: "))
	
	if selection == 1:
		make_convert()
	if selection == 2:
		print("See you later")
		
		

	