"""
Author: Victer Phiathep
Object-Oriented Programming (50:198:113), Fall 2022

This module contains a Appointment Book class implementation to be
used in Homework 5.
"""

from appt import Appointment

# This class is a CONTAINER for other objects so that 
# searching and sorting becomes possible.
class AppointmentBook():
    """
    This class will store a collection of appointment instances that form the schedule
    of a single person throughout the day.
    """
    def __init__(self):
        self.__data = []

    def __insert__(self, item):
        """
        Inserts a new appointment into the appointment book if it does not conflict with existing ones.
        If it does conflict, the user will receive an indication of all available time slots.
        """

    def searchtime(self, t1 , t2):
        """
        This method takes in two Time objects and searched for appointments who start time lie between T1 and T2
        and returns all such appointments in a list.
        """

    def searchkey(self):
        """
        Searches for appointments by keyword in the description and/or notes; the appointments
        that will be returned in a list
        """

    def searchloc(self):
        """
        search for appointments by location, appointments that match should be returned in a list
        """

    def delete(self):
        """
        """
        pass


class AppointmentBookIterator():
    def __init__(self):
        pass

    def __next__(self):
        pass