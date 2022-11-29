"""
Author: Victer Phiathep
Object-Oriented Programming (50:198:113), Fall 2022

This module contains a Appointment class implementation to be
used in Homework 5.
"""

class Time:
    def __init__(self, init_hr = 12, init_min = 0, init_ampm = "AM"):
        if init_hr < 1 or init_hr > 12:
            raise Exception("Error: Invalid hour for Time object")
        if init_min < 0 or init_min > 59:
            raise Exception("Error: Invalid minute for Time object")
        init_ampm = init_ampm.upper()
        if init_ampm != "AM" and init_ampm != "PM":
            raise Exception("Error: Invalid am/pm flag for Time object")
        self.hr = init_hr
        self.min = init_min
        self.ampm = init_ampm

    def hour(self):
        return self.hr

    def minute(self):
        return self.min

    def am_pm(self):
        return self.ampm

    def total_minutes(self):
        if self.hour() == 12:
            answer_mins = self.minute()
        else:
            answer_mins =  self.hour() * 60 + self.minute()
        if self.am_pm() == "PM":
            answer_mins += 720
        return answer_mins
        
    def minute_ahead(self):
        if self.minute() == 59:
            if self.hour() == 11:
                if self.am_pm() == "AM":
                    return Time(12, 0, "PM")
                else:
                    return Time(12, 0, "AM")
            else:
                return Time((self.hour() + 1)%12, 0, self.am_pm()) # Using %12 ensures that the hour 13 is stored as 1
        else:
            return Time(self.hour(), self.minute() + 1, self.am_pm())

    def minute_back(self):
        if self.minute() == 0:
            if self.hour() == 12:
                if self.am_pm() == "AM":
                    return Time(11, 59, "PM")
                else:
                    return Time(11, 59, "AM")
            else:
                hr = self.hour() - 1
                if hr == 0:
                    hr = 12
                return Time(hr, 59, self.am_pm()) 
        else:
            return Time(self.hour(), self.minute() - 1, self.am_pm())

    def __str__(self):
        h = str(self.hour())
        if self.minute() < 10:
            m = "0" + str(self.minute())
        else:
            m = str(self.minute())
        return h + ":" + m + self.am_pm()

    def __repr__(self):
        return str(self)

    def __add__(self, mins):
        # If mins is greater than the number of minutes in 24 hours (24 * 60)
        # we only need to consider the remainder when mins is divided
        # by 24 * 60. This is because the time of day repeats every 24 hours.
        
        final_mins = mins % (24 * 60)

        # We initialize a Time object called sum_time to be the same
        # as self, and then move sum_time forward one minute at a time,
        # using the minute_ahead() method.

        sum_time = Time(self.hour(), self.minute(), self.am_pm())

        for i in range(final_mins):
            sum_time = sum_time.minute_ahead()
        return sum_time

    def __sub__(self, mins):
        # The logic in this function is the same as in the __add__ method,
        # but with the difference that we move the time backward one minute
        # at a time

        final_mins = mins % (24 * 60)
        diff_time = Time(self.hour(), self.minute(), self.am_pm())

        for i in range(final_mins):
            diff_time = diff_time.minute_back()
        return diff_time

    def __lt__(self, other):
        return self.total_minutes() < other.total_minutes()

    def __gt__(self, other):
        return self.total_minutes() > other.total_minutes()        

    def __le__(self, other):
        return self.total_minutes() <= other.total_minutes()

    def __ge__(self, other):
        return self.total_minutes() >= other.total_minutes()
    
    def __eq__(self, other):
        return self.total_minutes() == other.total_minutes()

    def __ne__(self, other):
        return self.total_minutes() != other.total_minutes()        

def time_interval(T1, T2):
    """
    Returns a 2-tuple containing the number of hours and minutes 
    between T1 and T2

    T1, T2: Time objects
    """
    minutes_elapsed = abs(T2.total_minutes() - T1.total_minutes())
    return (minutes_elapsed//60, minutes_elapsed%60)

def time_schedule(start_time, duration, N):
    """
    Returns a list of N times starting at start_time and separated
    by duration minutes

    start_time: a Time object
    duration: an integer
    N: an integer
    """

    if N <= 0:
        return []

    S = Time(start_time.hour(), start_time.minute(), start_time.am_pm())
    L = [S]
    for i in range(N-1):
        S = S + duration
        L.append(S)
    return L

