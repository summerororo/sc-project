"""
File: quadratic_solver.py
Name:
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	to calculate the value of Quadratic
	"""
	print('stanCode Quadratic Solver!')
	a = float(input('Enter a: '))
	b = float(input('Enter b: '))
	c = float(input('Enter c: '))
	if b**2 - 4*a*c > 0:
		x = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
		y = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
		print('The two roots are ' + str(x) + ' and ' + str(y))
	elif b**2-4*a*c == 0:
		x = -b/(2*a)
		print('The only root is ' + str(x))
	else:
		print('No real roots')






###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
