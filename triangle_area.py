#Area of a triangle

def triangle_area(base,height):
	area = (base*height)/2
	print('The triangle area is '+str(area))

def trigle_type(base, height):
    h = (base**2 * height**2)**0.5
    if base == height == h:
        print('Your triangle is equilateral.')
    elif base == height:
        print('Your triangle is isosceles.')
    else:
        print('Your triangle is scalene.')

def calculate_triangle_area():	
	base = float(input('What is the triangle base?: '))
	height = float(input('What is the triangle height?: ' ))
	triangle_area(base,height)
	trigle_type(base,height)
