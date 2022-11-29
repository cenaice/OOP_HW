"""
Author: Victer Phiathep
Module for Homework 4, Problem 1
Object Oriented Programming (50:198:113), Fall 2022

Insert the remaining methods (overloaded operators) of the
Time class. Also insert the two functions time_interval
and time_schedule after the Time class

Please insert documentation for all the new methods and functions
inserted into this module. 
"""


class Time:
    def __init__(self, init_hr=12, init_min=0, init_ampm="AM"):
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
            answer_mins = self.hour() * 60 + self.minute()
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
                # Using %12 ensures that the hour 13 is stored as 1
                return Time((self.hour() + 1) % 12, 0, self.am_pm())
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

    # IMPLEMENT THE OVERLOADED OPERATORS OF THE Time CLASS BELOW!

    def __add__(self, other):
        """
        Overloads the + operator and returns the "sum" of a Time instance
        and a non-negative integer "mins"
        """
        hour = self.hour()
        minutes = self.minute()
        ampm = self.am_pm()

        # Convert the minutes added into hour, minutes to create a new Time instance
        while other > 0: # Keep looping until amount added is 0
            if other > 60:
                other -= 60
                hour += 1
                if hour == 12: # If hour is 12, we must change from AM,PM
                    if ampm == "AM":
                        ampm = "PM"
                    else:
                        ampm = "AM"
                elif hour > 12:
                    hour = 1

            else:
                minutes += other
                other = 0
                if minutes >= 60: 
                    minutes -= 60
                    hour += 1
                    if hour == 12: # If hour is 12, we must change from AM,PM
                        if ampm == "AM":
                            ampm = "PM"
                        else:
                            ampm = "AM"
                    elif hour > 12:
                        hour = 1

        return Time(hour, minutes, ampm)

    def __sub__(self, other):
        """
        Overloads the - operator and subtracts a non-negative integer from a Time instance
        """
        hour = self.hour()
        minutes = self.minute()
        ampm = self.am_pm()

        while other > 60:
            hour -= 1
            other -= 60
            if hour == 0:
                hour = 12
            elif hour == 11:
                if ampm == "AM":
                    ampm = "PM"
                else:
                    ampm = "AM"

        new_mins = minutes - other

        if new_mins < 0:
            hour -= 1
            if hour == 0:
                hour = 12
            elif hour == 11:
                if ampm == "AM":
                    ampm = "PM"
                else:
                    ampm = "AM"
            new_mins = 60-(new_mins*-1)
        return Time(hour, new_mins, ampm)

    def __lt__(self, other):
        """
        Overloads the < operator and compares two Time objects. Returns TRUE if the time instance
        on the left hand side occurs strictly before the instance on the right hand side. 
        """
        return self.total_minutes() < other.total_minutes()

    def __gt__(self, other):
        """
        This method overloads the > operator and returns a True or False value.
        """
        return self.total_minutes() > other.total_minutes()

    def __le__(self, other):
        """
        Overloads the <= operator to return a True or False value
        """
        return self.total_minutes() <= other.total_minutes()

    def __ge__(self, other):
        """
        Overloads the >= operator to return a True or False value
        """
        return self.total_minutes() >= other.total_minutes()

    def __eq__(self, other):
        """
        Overloads the == operator to return a True or False value
        """
        return self.total_minutes() == other.total_minutes()

    def __ne__(self, other):
        """
        Overloads the != operator to return a True or False value
        """
        return self.total_minutes() != other.total_minutes()


# IMPLEMENT THE FUNCTIONS time_interval AND time_schedule below
def time_interval(T1, T2):
    """
    This function takes in two Time objects and returns the number of hours and minutes in
    the intervals between T1 and T2 in a pair "(hours, minutes)"
    """

    if T1.am_pm() == T2.am_pm(): # Check if both are AM,PM
        hours = abs(T1.hour() - T2.hour()) # Subtracting hours together
        minutes = abs(T1.minute() - T2.minute()) # Subtracting minutes
        return (hours, minutes)
    elif T1.am_pm() == 'AM': # If one is PM, add 12 to the hours 
        if T1.hour() == 12:
            hours = abs((T2.hour()+12))
            minutes = abs(T1.minute() - T2.minute())
        else:
            hours = abs((T2.hour()+12) - T1.hour())
            minutes = abs(T1.minute() - T2.minute())
        return (hours, minutes)
    elif T2.am_pm() == 'AM':  # If one is PM, add 12 to the hours 
        if T2.hour() == 12:
            hours = abs((T2.hour()+12))
            minutes = abs(T1.minute() - T2.minute())

        else:
            hours = abs((T1.hour()+12) - (T2.hour()))
            minutes = abs(T1.minute() - T2.minute())

        return (hours, minutes)


def time_schedule(start_time, duration, N):
    """
    Return a list of length N that contains the N Times that occur every duration minutes starting
    at start_time. The list contains Time Objects and not strings.
    """
    count = 0 
    arr = [start_time]

    while count != N-1: # While loop will run until it hits the length of N
        start_time+=duration # Using our __add__ method to simply add the duration onto the start time
        arr.append(start_time)
        count += 1
    return arr
