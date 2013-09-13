#!/usr/bin/env python
# This script is used for my WordClock project. It require an mcp23017 GPIO expander and wiringpi2.
# The script simply check the time and turn on the respective led. The clock is in italian, but you can easly adapt it.

# NOTICE: there are a lot of print output, these are not require, so you can comment them if you don't want a screen output.

# www.raspberrygaming.tk

import sys
import time
import wiringpi2 as wiringpi
from time import sleep

pin_base = 65       # lowest available starting number is 65  
i2c_addr = 0x20     # A0, A1, A2 pins all wired to GND  
  
wiringpi.wiringPiSetup()                    # initialise wiringpi  
wiringpi.mcp23017Setup(pin_base,i2c_addr)   # set up the pins and i2c address  
  

wiringpi.pinMode(1, 1)		#initialise all the required pin
wiringpi.pinMode(4, 1)
wiringpi.pinMode(5, 1)
wiringpi.pinMode(6, 1)
wiringpi.pinMode(15, 1)
wiringpi.pinMode(16, 1)
for count in range(65,80):
	wiringpi.pinMode(count, 1)


while True:

	ora = time.strftime("%I", time.localtime(time.time()));		#Takes the hour
	minuti = time.strftime("%M", time.localtime(time.time()));	#Takes the minutes

	#Convert values from String to Int
	minuti = int(minuti)
	ora = int(ora)

	#print ora
	#print minuti

	#Turn off all the led
	wiringpi.digitalWrite(1, 1)
	wiringpi.digitalWrite(4, 1)
	wiringpi.digitalWrite(5, 1)
	wiringpi.digitalWrite(6, 1)
	wiringpi.digitalWrite(15, 1)
	wiringpi.digitalWrite(16, 1)
	for count in range(65,80):
		wiringpi.digitalWrite(count, 1)
		
	#Turn on the required led

	if 0 <= minuti <= 2:
		print "niente"

	if 3 <= minuti <= 7:
		print "e cinque"
		wiringpi.digitalWrite(71, 0)	
		wiringpi.digitalWrite(73, 0)

	if 8 <= minuti <= 12:
		print "e dieci"
		wiringpi.digitalWrite(71, 0)
		wiringpi.digitalWrite(74, 0)

	if 13 <= minuti <= 17:
		print "e un quarto"
		wiringpi.digitalWrite(71, 0)
		wiringpi.digitalWrite(75, 0)

	if 18 <= minuti <= 22:
		print "e venti"
		wiringpi.digitalWrite(71, 0)
		wiringpi.digitalWrite(76, 0)

	if 23 <= minuti <= 27:
		print "e venticinque"
		wiringpi.digitalWrite(71, 0)
		wiringpi.digitalWrite(77, 0)

	if 28 <= minuti <= 32:
		print "e mezza"
		wiringpi.digitalWrite(71, 0)
		wiringpi.digitalWrite(78, 0)

	if 33 <= minuti <= 37:
		print "e trentacinque"
		wiringpi.digitalWrite(71, 0)
		wiringpi.digitalWrite(79, 0)

	if 38 <= minuti <= 42:
		print "meno venti"
		wiringpi.digitalWrite(72, 0)
		wiringpi.digitalWrite(76, 0)
		ora = ora + 1

	if 43 <= minuti <= 47:
		print "meno un quarto"
		wiringpi.digitalWrite(72, 0)
		wiringpi.digitalWrite(75, 0)
		ora = ora + 1

	if 48 <= minuti <= 52:
		print "meno dieci"
		ora = ora + 1
		wiringpi.digitalWrite(72, 0)
		wiringpi.digitalWrite(74, 0)

	if 53 <= minuti <= 57:
		print "meno cinque"
		ora = ora + 1
		wiringpi.digitalWrite(72, 0)
		wiringpi.digitalWrite(73, 0)

	if minuti >= 58:
		print "niente"
		ora = ora + 1

	#print ora

	if ora == 12:
		print "dodici"
		wiringpi.digitalWrite(70, 0)

	if ora == 1 or ora == 13:
		print "una"
		wiringpi.digitalWrite(6, 0)

	if ora == 2:
		print "due"
		wiringpi.digitalWrite(5, 0)

	if ora == 3:
		print "tre"
		wiringpi.digitalWrite(4, 0)

	if ora == 4:
		print "quattro"
		wiringpi.digitalWrite(1, 0)

	if ora == 5:
		print "cinque"
		wiringpi.digitalWrite(16, 0)

	if ora == 6:
		print "sei"
		wiringpi.digitalWrite(15, 0)

	if ora == 7:
		print "sette"
		wiringpi.digitalWrite(65, 0)

	if ora == 8:
		print "otto"
		wiringpi.digitalWrite(66, 0)

	if ora == 9:
		print "nove"
		wiringpi.digitalWrite(67, 0)

	if ora == 10:
		print "dieci"
		wiringpi.digitalWrite(68, 0)

	if ora == 11:
		print "undici"
		wiringpi.digitalWrite(69, 0)

	sleep (60)	#The clock have a 5 minute precision, so a 60 seconds loop will be good.
