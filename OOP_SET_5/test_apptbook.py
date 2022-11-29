from appt import *
from mytime import *

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

    # Create Time Objects 
    T1_start = Time(10, 30, "AM")
    T1_end = Time(12, 0, "PM")


    App_1 = Appointment(T1_start, T1_end, 'Camden', 'Homework Help', 'Students needs help with studying')

    # Testing first appointment
    print(App_1)

