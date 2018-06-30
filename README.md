# gymclassbot
This bot
1) logs on to the True Fitness website;
2) attempts to find and register the desired class around the time reservation opens;
3) sends out an email on the status (Class Booked) at completion;
4) and logs out of the website. 

Specs:
1) Windows OS (I use Windows 10)
2) Python 3.6.4 IDLE (or later versions)
3) Google Chrome browser (latest version)
4) Python pip install: Selenium with Python
5) Download and locate: chromedriver.exe
6) Python Imports: smtplib, re 
7) For email notifications, you need to get your App Password (I use Gmail in this program)
8) TrueFitness class booking website userid and password
9) Details of your target class: Gym Location, Studio Type, Class Name, Instructor Name, Class Timeslot
10) Access to Task Scheduler

Steps:
1) Update the <ENTER YOUR...> fields in the Python file with your info.
2) Do a test run to ensure you are able to use Selenium's Webdriver to log in to the website.
(If you were unsure of the class details, check against View Source when the program logs you into the website.)
3) After ensuring the program is functional, create a batch file with the same name as your Python file (put this in the same directory where your Python file is located) to run your Python file. You might need to add Python to the PATH Environmental Variable and set exclusive rights to Python in your anti-virus / firewall software.
4) Set up a task in Task Scheduler to run the batch file and specify it to do so on at 10pm 2 nights before your class.
e.g. The class is on 9am Thursday. Set up task to coincide with the timing when booking reservations are allowed -- which is, 48 hours before the day or precisely, on Monday at 10pm.
For this task, you will want to ensure it runs with:
  highest privileges, only when user is logged in, whether on laptop power or not, and ends after an hour of running.

This is my first Python program and in using Selenium too. 
Please let me know if it works for you!
