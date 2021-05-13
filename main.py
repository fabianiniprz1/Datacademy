import rock_paper_scissors as rps
import triangle_area as ta


def run():
	selectionX = int(input('What would you like to do?: \n 1.Calculate a triangle area \n 2.Play rock paper scissors: '))
	selection(selectionX)

def selection(i):
	if i == 1:
		ta.calculate_triangle_area()
	elif i ==2:
		rps.rock_paper_scissors_game()	


if __name__ == '__main__':
	run()