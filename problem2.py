"""
Author: Victer Phiathep
Object Oriented Programming, Fall 2022

Test module for Homework 3, Problem 2
"""

class Time:

    def __init__(self, hour='12', minute='0', am_pm='AM') -> None:
        """
        Constructor
        """

        if int(hour) <= 12 and int(hour) > 0:
            self.hours = hour
        else:
            raise Exception("Error")

        if int(minute) < 60 and int(minute) >= 0:
            self.minutes = minute
        else:
            raise Exception("Error")

        if am_pm.lower() == 'am' or am_pm.lower() == 'pm':
            self.daytime = am_pm.upper()
        else:
            raise Exception("Error")

    def hour(self):
        """Returns the hour of the Time instance"""
        return self.hours

    def minute(self):
        """Returns the minutes of the Time instance"""
        return self.minutes

    def am_pm(self):
        """Returns whether the time is AM or PM of the Time instance"""
        return self.daytime

    def total_minutes(self):
        """
        Returns the total numbers of minutes that was passed since 12:00AM
        """
        mins = int(self.minutes)
        hours = int(self.hours)
        if self.daytime == 'AM':

            if hours == 12:
                return mins

            return hours*60 + mins

        else:
            if hours == 12:
                return hours*60 + mins

            return (12*60)+(hours*60)+mins

    def minute_ahead(self):
        """
        Returns the time a minute ahead in a string format
        """
        minute_up = int(self.minutes) + 1

        if minute_up == 60:
            time = f"{self.hours+1}:00"

            # Convert 12:59 to 1 PM/AM
            if self.hours+1 == 12 and self.daytime == "AM":
                return time+'PM'

            else:
                return time+'AM'

        elif minute_up < 10:
            return f"{self.hours}:0{minute_up}{self.daytime}"

        return f"{self.hours}:{minute_up}{self.daytime}"

    def minute_back(self):
        """
        Returns the time a minute behind in a string format
        """
        mins = int(self.minutes)
        hours = int(self.hours)

        minute_down = mins-1
        if mins == 0:
            # Check for 12:00 to swithc AM and PM
            if hours == 12 and self.daytime == 'AM':
                return f"11:59PM"
            elif hours == 12 and self.daytime == 'PM':
                return f"11:59AM"
            # Check for 1:00 to convert to 12:59
            elif hours == 1:
                return f"12:59{self.daytime}"
            else:
                return f"{hours-1}:59{self.daytime}"
        elif mins <= 10:
            return f"{hours}:0{minute_down}{self.daytime}"

        return f"{hours}:{minute_down}{self.daytime}"

    def __str__(self):
        """
        Returns time in a reading string format
        """

        # Special case for single digit times
        if int(self.minutes) < 10:
            return "%s:0%s%s" % (self.hours, self.minutes, self.daytime)
        else:
            return "%s:%s%s" % (self.hours, self.minutes, self.daytime)

    def __repr__(self):
        if int(self.minutes) < 10:
            return "%s:0%s%s" % (self.hours, self.minutes, self.daytime)
        else:
            return "%s:%s%s" % (self.hours, self.minutes, self.daytime)
