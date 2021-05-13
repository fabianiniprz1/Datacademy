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
	welcome("					🧮 📈 📊 WELCOME TO LITTLE THINGS SOFTWARE 🧮 📈 📊")
	selectionX = int(input('What would you like to do?: \n 1.Calculate a triangle area \n 2.Play rock paper scissors\n 3.Convert a measure: '))
	selection(selectionX)
	
def selection(i):
	if i == 1:
		welcome("🔺 WELCOME LET'S CALCULATE AREAS 🔻")
		ta.calculate_triangle_area()
	elif i ==2:
		welcome("✂ 🧻 💎 WELCOME TO THE ROCK PAPER SCISSORS ✂ 🧻 💎")
		rps.rock_paper_scissors_game()
	elif i == 3:
		welcome("🚧 🏁 WELCOME TO THE MILES/KILOMETERS CONVERTER 🚧 🏁")
		mtk.make_convert()

if __name__ == "__main__":
	run()
