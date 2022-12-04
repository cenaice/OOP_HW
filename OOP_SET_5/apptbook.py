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
        self.__appointments = []

    def insert(self, item):
        """
        Inserts a new appointment into the appointment book if it does not conflict with existing ones.
        If it does conflict, the user will receive an indication of all available time slots.
        """
        # if len(self.__appointments) == 0:
        #     self.__appointments.append(item)
        # else:
        #     # Use the conflicts method in apptbook.py to check for any scheduling conflicts
        #     count = 0
        #     for app in self.__appointments:
        #         if app.conflicts(item) == False:
        #             # Checks if time slot can occur before current position
        #             if item.start() < app.start() and item.end() < app.end():
        #                 self.__appointments.insert(count, item)
        #             # If it doesn't occur before any slots, append to end of list
        #             if count == len(self.__appointments):
        #                 self.__appointments.append(item)
        #             count+=1

        #         else:
        #             # Returns available schedules
        #             print("Conflict of schedule. See available schedules below")
        #             return self.available()
        self.__appointments.append(item)

    def searchtime(self, t1, t2):
        """
        This method takes in two Time objects and searched for appointments who start time lie between T1 and T2
        and returns all such appointments in a list.
        """
        # Create a new Appointment instance in order to use the conflict method
        search = Appointment(t1, t2, 'Search')
        conflicts = []

        # Check if appointments fall between the time frames
        for app in self.__appointments:
            if search.start() > app.start() and search.start() < app.end():
                conflicts.append(app)

        return conflicts

    def searchkey(self, keyword):
        """
        Searches for appointments by keyword(parameter) in the description and/or notes; the appointments
        that will be returned in a list.
        """
        search = []
        for app in self.__appointments:
            if keyword in app.description():
                search.append(app)
        return search

    def searchloc(self, location):
        """
        search for appointments by location, appointments that match should be returned in a list
        """
        loc_arr = []
        for app in self.__appointments:
            if location in app.location():
                loc_arr.append(app)
        return loc_arr

    def delete(self, idx):
        """
        Deletes an item in our appointment book by index number in our collection.
        """
        del self.__appointments[idx]

    def create_report(self):
        """
        Creates a report of all appointments scheduled for the day.
        Appointments should appear in chronological order
        """

        # Create file
        file = open("report.txt", "w")
        count = 1
        for app in self.__appointments:
            file.write(f"-Appointment {count}-\n\n-{str(app)}\n\n")
            print(f"-Appointment {count}-")
            print(app)
            print("-----------------------------")
            count += 1
        print("Reports created as report.txt")
        file.close()

    def available(self):
        """
        Shows all available slots during the day that no appointment is scheduled.
        The slots will be shown in sorted order by starting time.
        """
        if len(self.__appointments) == 0:
            return "All time slots are available."
        
        for app in self.__appointments:
            if app == self.__appointments[0]:
                print("Opening between: ")
                print(app.end())
            else:
                print(app.start())
                print("Opening between: ")
                print(app.end())
                

    def __iter__(self):
        """
        Iterator
        """
        return AppointmentBookIterator(self.__appointments)

    def __len__(self):
        """
        Allows the use of the len() function on our instance
        """
        return len(self.__appointments)

    def __getitem__(self, idx):
        """
        Overload the index operator
        """
        if idx < 0 or idx >= len(self.__appointments)//2: 
            raise IndexError

        return self.__appointments[2*idx] + self.__appointments[2*idx + 1] 


class AppointmentBookIterator():
    def __init__(self, Appointment_Book):
        self.__apptbook = Appointment_Book
        self.current = 0

    def __next__(self):
        if self.__current > len(self.__apptbook):
            raise StopIteration
        answer = self.__apptbook[self.current]
        self.__current += 1
        return answer
