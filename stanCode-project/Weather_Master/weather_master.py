"""
File: weather_master.py
Name:
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

QUIT = -1


def main():
	"""
	input each day's temperature and output maximum, minimum, average and how many cold days
	"""
	print('stanCode \"Weather Master 4.0\"!')
	first_temperature = int(input('Next temperature: (or ' + str(QUIT) + ' to quit)? '))
	if first_temperature == QUIT:
		print('No temperatures were entered.')
	if first_temperature != QUIT:
		if first_temperature < 16:
			# if the temperature is lower than 16 (but don't equal 16 and str(QUIT) then cold_day +1.
			cold_day = 1
		else:
			cold_day = 0
		count = 1
		total = first_temperature
		maximum = first_temperature
		minimum = first_temperature
		while True:
			# compare the temperature with QUIT, maximum and minimum
			temperature = int(input('Next temperature: (or ' + str(QUIT) + ' to quit)? '))
			if temperature == QUIT:
				break
			if temperature != QUIT:
				if temperature < 16:
					cold_day += 1
				if temperature > maximum:
					maximum = temperature
				if temperature < minimum:
					minimum = temperature
				count += 1
				total += temperature
		print('Highest temperature = ' + str(maximum))
		print('Lowest temperature = ' + str(minimum))
		print('Average = ' + str(float(total/count)))
		print(str(cold_day) + ' cold day(s)')







###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
