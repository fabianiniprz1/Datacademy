import rock_paper_scissors as rps
import triangle_area as ta
import miles_to_kilometers as mtk


def welcome(message):
	print("=================================================================================")
	print("=================================================================================")
	print(message)
	print("=================================================================================")
	print("=================================================================================")

def run():
	welcome("					๐งฎ ๐ ๐ WELCOME TO LITTLE THINGS SOFTWARE ๐งฎ ๐ ๐")
	selectionX = int(input('What would you like to do?: \n 1.Calculate a triangle area \n 2.Play rock paper scissors\n 3.Convert a measure: '))
	selection(selectionX)
	
def selection(i):
	if i == 1:
		welcome("๐บ WELCOME LET'S CALCULATE AREAS ๐ป")
		ta.calculate_triangle_area()
	elif i ==2:
		welcome("โ ๐งป ๐ WELCOME TO THE ROCK PAPER SCISSORS โ ๐งป ๐")
		rps.rock_paper_scissors_game()
	elif i == 3:
		welcome("๐ง ๐ WELCOME TO THE MILES/KILOMETERS CONVERTER ๐ง ๐")
		mtk.make_convert()

if __name__ == "__main__":
	run()
