from appt import *
from mytime import *
from apptbook import *

"""
Author: Victer Phiathep
Object-Oriented Programming (50:198:113), Fall 2022

This module contains a Test Module Class implementation to be
used in Homework 5.
"""



if __name__ == "__main__":
    """
    TEST MODULE
    """

    
    print('-----------------------------------------------------------\n')
    print("Testing __str__ for Appointments\n")
    T1_start = Time(10, 30, "AM")
    T1_end = Time(12, 0, "PM")
    App_1 = Appointment(T1_start, T1_end, 'Camden', 'Homework Help', 'Students needs help with studying')
    print(App_1)
    print('\n')
    
    # Test for Exception Error
    # T2_start = Time(6, 0, "AM") # Test for Exception Error
    # T2_end = Time(11, 0, "PM")
    # App_2 = Appointment(T2_start, T2_end,'Camden', 'Homework')

    T3_start = Time(7,0,'AM')
    T3_end = Time(2,0,'PM')
    App_3 = Appointment(T3_start,T3_end,'Camden','Exam Review')
    print(App_3)

    T4_start = Time(7,59,'AM')
    T4_end = Time(8,1,"AM")
    App_4 = Appointment(T4_start,T4_end,'Zoom','Greetings')
    print(App_4)

    T5_start = Time(3,0,'PM')
    T5_end = Time(4,1,'PM')
    App_5 = Appointment(T5_start,T5_end,'Zoom','Meeting with Professor','Discussing Grade')
    print(App_5)

    print("-----------------------------------------------")
    print("TESTING START/END METHODS")
    print(f"App_1 Start Time: {App_1.start()} ----- Correct answer: 10:30AM")
    print(f"App_3 End Time: {App_3.end()}   ----- Correct answer: 9:00PM")

    print("-----------------------------------------------")
    print("TESTING LOCATION/DESCRIPTION/NOTES METHOD")
    print("--App 1--")
    print(App_1.location())
    print(App_1.description())
    print(App_1.notes())
    print("--App 3--")
    print(App_3.location())
    print(App_3.description())
    print(App_3.notes())
    
    print("-----------------------------------------------")
    print("TESTING DURATION")
    print("--App 1--")
    print(App_1.duration())
    print("--App 3--")
    print(App_3.duration()) 

    print("-----------------------------------------------")
    print("TESTING CONFLICTS")
    print("--App 1 and 4--")
    if App_1.conflicts(App_4) == False:
        print("No conflict... Correct Answer")
    else:
        print("Conflict... Incorrect Answer")
    print("--App 3 and 4--")
    if App_3.conflicts(App_4) == False:
        print("No conflict... Incorrect Answer")
    else:
        print("Conflict... Correct Answer")
    print("--App 1 and 3--")
    if App_1.conflicts(App_3) == False:
        print("No conflict... Correct Answer")
    else:
        print("Conflict... Incorrect Answer")

print("-----------------------------------------------")
print("TESTING APPOINTMENT BOOKS CLASS")

Apt_Book = AppointmentBook()

Apt_Book.insert(App_1)
Apt_Book.insert(App_3)
Apt_Book.insert(App_5)
Apt_Book.create_report()
print('\n')
print("TESTING SEARCH KEYWORD\n")
print(Apt_Book.searchkey("Exam"))
print("\n")
print(Apt_Book.searchloc("Camden"))

print("\nTesting Search Time\n")
T1 = Time(8,0,'AM')
T2 = Time(5,0,'PM')
print(Apt_Book.searchtime(T1,T2))

Apt_Book.delete(0)