This code is reminder system

There are 3 main files:
1.recorder.py
2.remind.csv
3.reminder.py

###########################################
1.recorder.py
INPUT (y) to record > user needs to input letter "y" to start recording
WHAT to remind > the lengtth of content must be less than 35
WHEN to remind > user has 2 options:
			1.input "next" follow by an integer and end with "second" or "minute" or "day"
			2.input "tomorrow" : this will remind the user at this time on the next day
The content is export and store in csv file ("remind.csv")
######################################################################################
2.remind.csv
This file contains 3 columns:
			1.content: store content to be remind
			2.start: store the time that the content was recorded
			3.remind: store the time that the content need to be remind
			4.complete: is 0 if completed, is 1 is completed
######################################################################################
3.reminder.py
The text "REMINDER ALERT !!!!!!" will be pop up.
Also, the model will generate the voice that read the content to be remind to the user
using  "from win32com.client import Dispatch" 

Then "Snooze / Mark as complete :" will be pop up > user has 2 options:
			1.input "next/remind/snooze" follow by an integer and end with "second" or "minute" or "day"
			2.input "mark/complete" to mark the content as complete
######################################################################################
