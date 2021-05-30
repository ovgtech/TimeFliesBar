
""" Timefliesbar date calculus. """

# MIT License

# Copyright (c) 2020 melancholicbot

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

#---------------------------------------------------------------------------#

# Contact.

# timefliesbar@protonmail.com

#---------------------------------------------------------------------------#

import datetime

#---------------------------------------------------------------------------#

# Obtain basic year information.

currentDate: str
currentYear: int
currentDay: str

currentDate = datetime.datetime.now()
currentYear = currentDate.year
currentDay = currentDate.strftime("%j")

# Test dates
# currentYear = 2022
# currentDay = 0

#---------------------------------------------------------------------------#

# Obtain year type.

stringCurrentYear: str
""" Int to string conversion needed. """

stringCurrentYear = str(currentYear)

secondLastDigitCurrentYear: str
lastDigitCurrentYear: str
leapYear: int

secondLastDigitCurrentYear = stringCurrentYear[2:3]
lastDigitCurrentYear = stringCurrentYear[3:4]

if currentYear%4 == 0:

	if secondLastDigitCurrentYear == 0 and lastDigitCurrentYear == 0:

		if currentYear%400 == 0:

			leapYear = 1

		elif currentYear%400 != 0:
			leapYear = 0

	else:
		pass

elif currentYear%4 != 0:
	leapYear = 0

#---------------------------------------------------------------------------#

# Obtain total days.

totalDays: int
""" Total days depending on year type. """

if leapYear == 1:
	totalDays = 366

elif leapYear == 0:
	totalDays = 365

#---------------------------------------------------------------------------#

# Obtain total minutes.

totalMinutes: int
""" Total minutes. Days + 60. """

totalMinutes = totalDays * 1440

#---------------------------------------------------------------------------#

# Obtain gone minutes.

peCurrentHour: str
""" PythonEverywhere current hour. """
peCurrentMinute: str
""" PythonEverywhere current minute. """

currentHour: int
""" Local current hour. """
currentMinute: int
""" Local current minute. """

minutesGone: int
""" Minutes elapsed untill current time. """

# PE date correction
peCurrentHour = currentDate.strftime("%H")  #PythonEverywhere environment has 1 hour less
peCurrentMinute = currentDate.strftime("%M")   #PythonEverywhere environment has 60 minutes less

currentHour = int(peCurrentHour) + 1    #Hour more correction to local hour
currentMinute = int(peCurrentMinute) + 60   #Hour more correction to local hour

# Test dates
# currentHour = int(12)   #Hour more correction to local hour
# currentMinute = int(00)   #Hour more correction to local hour

minutesGone = int(currentDay)*1440 + int(currentHour)*60 + int(currentMinute)

#---------------------------------------------------------------------------#

# Obtain remaining minutes.

minutesRemaining: int
""" Minutes remaining this year. """

minutesRemaining = int(totalMinutes) - int(minutesGone)