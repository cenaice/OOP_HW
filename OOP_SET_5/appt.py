from mytime import *
"""
Author: Victer Phiathep
Object-Oriented Programming (50:198:113), Fall 2022

This module contains a Appointment class that allows us to store
and retrieve information about a specific apointment.
Homework Set 5
"""

class Appointment(Time):
    def __init__(self, start_time, end_time, location, description="", notes=""):
        """
        Constructor
        """
        # Must be specified/ No default parameters
        if start_time.hour() < 7 or start_time.hour() > 21:
            raise Exception("Time is not within appointment hours")

        self.__start_time = start_time # Time Instance should be passed in
        self.__end_time = end_time # Time instance should be passed in
        self.__location = location

        # Default Values if not specified
        self.__description = description
        self.__notes = notes


    def start(self):
        """
        Returns the starting time of the appointment
        """
        return self.__start_time
    
    def end(self):
        """
        Returns the ending time of the appointment
        """
        return self.__end_time

    def location(self):
        """
        Returns the location of the appointment
        """
        return self.location


    def description(self):
        """
        Returns a description of the appointment
        """
        return self.description

    def notes(self):
        """
        Returns any notes kept for the appointment
        """
        return self.notes

    def duration(self):
        """
        Returns the duration of the appointment in minutes as a string
        """
        duration = time_interval(self.__start_time, self.__end_time)
        
        # Convert hours to minutes and add together to get total time in minutes
        total_time = (duration[0]*60)+duration[1]
        
        return total_time

    def conflicts(self, other):
        """
        Returns True if there is a time conflict between two appointment objects,
        self and other should both be appointment objects
        """
        if self.__end_time > other.__start_time:
            return False
        elif other.__end_time > self.__start_time:
            return False
        else:
            return True

    def __str__(self):
        """
        Returns a printable representation of an appointment
        """
        message = f"Appointment Start: {self.__start_time}\nAppointment End: {self.__end_time}\nLocation: {self.__location}\nDescription: {self.__description}"
        return message

    def __repr__(self):
        """
        Returns a meaningful string representation of an appointment
        """
        return str(self)

