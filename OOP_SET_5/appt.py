from mytime import Time

"""
Author: Victer Phiathep
Object-Oriented Programming (50:198:113), Fall 2022

This module contains a Appointment class that allows us to store
and retrieve information about a specific apointment.
Homework Set 5
"""

class Appointment(Time):
    def __init__(self, location, description, notes):
        start_time = Time.__init__(self, 7, 0, "AM")
        end_time = Time.__init__(self, 9, 0, "PM")
        self.location = location
        self.description = description
        self.notes = notes


    def start(self):
        """
        Returns the starting time of the appointment
        """
    
    def end(self):
        """
        Returns the ending time of the appointment
        """

    def location(self):
        """
        Returns the location of the appointment
        """

    def description(self):
        """
        Returns a description of the appointment
        """

    def notes(self):
        """
        Returns any notes kept for the appointment
        """

    def duration(self):
        """
        Returns the duration of the appointment
        """

    def conflicts(self, other):
        """
        Returns True if there is a time conflict between self and other
        """

    def __str__(self):
        """
        Returns a printable representation of an appointment
        """

    def __repr__(self):
        """
        Returns a meaningful string representation of an appointment
        """

