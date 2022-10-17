"""
Author: Victer Phiathep
Object Oriented Programming, Fall 2022

Test module for Homework 3, Problem 2
"""


from problem2 import Time










if __name__ == "__main__":
    t1 = Time()
    t2 = Time(2, 30, "am")
    t3 = Time(10, 10, "am")
    t4 = Time(12, 0, "pm")
    t5 = Time(12, 15, "pm")
    t6 = Time(2, 0, "pm")
    t7 = Time(3, 12, "pm")
    t8 = Time(6, 18, "pm")
    t9 = Time(7, 0, "pm")
    t10 = Time(9, 42, "pm")
    t11 = Time(10, 48, "pm")
    t12 = Time(11, 59, "pm")

    print("\n\n------------------------------------------------------ ")
    print("This test program tests your implementation of the ")
    print("Time class methods.")
    print("The correct output will be shown along with the output")
    print("given by your implementation. ")
    print("------------------------------------------------------ \n\n")

    print("Testing the constructor")
    print("-----------------------\n")

    try:
        t13 = Time(13, 1, "am")
    except:
        print("Exception correctly raised for invalid hour")
    else:
        print("ERROR: exception was not raised for invalid hour")

    try:
        t13 = Time(11, 67, "pm")
    except:
        print("Exception correctly raised for invalid minute")
    else:
        print("ERROR: exception was not raised for invalid minute")

    try:
        t13 = Time(12, 1, "xx")
    except:
        print("Exception correctly raised for invalid am/pm flag")
    else:
        print("ERROR: exception was not raised for invalid am/pm flag")        
        

    ans = input("\nReady for the next test [y/n]?")
    if (ans != 'y'):
        exit()
  
    print("Testing the hour, minute, and am_pm methods")
    print("-------------------------------------------\n")

    print("Correct answer: 12 0 AM     Your answer: ", t1.hour(), t1.minute(), t1.am_pm())
    print("Correct answer: 2 30 AM     Your answer: ", t2.hour(), t2.minute(), t2.am_pm())
    print("Correct answer: 12 0 PM     Your answer: ", t4.hour(), t4.minute(), t4.am_pm())
    print("Correct answer: 9 42 PM     Your answer: ", t10.hour(), t10.minute(), t10.am_pm())

    ans = input("\nReady for the next test [y/n]?")
    if (ans != 'y'):
        exit()
  
    print("Testing the __str__ method")
    print("--------------------------\n")

    print("Correct output: 12:00AM       Your output: ", t1)
    print("Correct output: 2:30AM        Your output: ", t2)
    print("Correct output: 10:10AM       Your output: ", t3)
    print("Correct output: 12:00PM       Your output: ", t4)
    print("Correct output: 2:00PM        Your output: ", t6)
    print("Correct output: 9:42PM        Your output: ", t10)
    print("Correct output: 11:59PM       Your output: ", t12)

    ans = input("\nReady for the next test [y/n]?")
    if (ans != 'y'):
        exit()
  
    print("\nTesting the total_minutes() method")
    print("----------------------------------\n")

    print("*** Correct output ***")
    print("Number of minutes from midnight to ", t1, ": 0")
    print("Number of minutes from midnight to ", t3, ": 610")
    print("Number of minutes from midnight to ", t4, ": 720")
    print("Number of minutes from midnight to ", t8, ": 1098")
    print("Number of minutes from midnight to ", t12, ": 1439")
    
    print("*** Your output ***")
    print("Number of minutes from midnight to ", t1, ": ", t1.total_minutes())
    print("Number of minutes from midnight to ", t3, ": ", t3.total_minutes())
    print("Number of minutes from midnight to ", t4, ": ", t4.total_minutes())
    print("Number of minutes from midnight to ", t8, ": ", t8.total_minutes())
    print("Number of minutes from midnight to ", t12, ": ", t12.total_minutes())

    ans = input("\nReady for the next test [y/n]?")
    if (ans != 'y'):
        exit()
  
    t13 = Time(11, 59, "am")
    t14 = Time(6, 59, "am")

    print("\nTesting the minute_ahead() method")
    print("----------------------------------\n")

    print("*** Correct output ***")
    print("One minute ahead of ", t1, " the time is 12:01AM")
    print("One minute ahead of ", t3, " the time is 10:11AM")
    print("One minute ahead of ", t7, " the time is 3:13PM")
    print("One minute ahead of ", t12, " the time is 12:00AM")
    print("One minute ahead of ", t13, " the time is 12:00PM")
    print("One minute ahead of ", t14, " the time is 7:00AM")

    print("*** Your output ***")
    print("One minute ahead of ", t1, " the time is ", t1.minute_ahead())
    print("One minute ahead of ", t3, " the time is ", t3.minute_ahead())
    print("One minute ahead of ", t7, " the time is ", t7.minute_ahead())
    print("One minute ahead of ", t12, " the time is ", t12.minute_ahead())
    print("One minute ahead of ", t13, " the time is ", t13.minute_ahead())
    print("One minute ahead of ", t14, " the time is ", t14.minute_ahead())        

    ans = input("\nReady for the next test [y/n]?")
    if (ans != 'y'):
        exit()

    t15 = Time(1, 0, "am")
  
    print("\nTesting the minute_back() method")
    print("----------------------------------\n")

    print("*** Correct output ***")
    print("One minute behind ", t1, " the time is 11:59PM")
    print("One minute behind ", t4, " the time is 11:59AM")
    print("One minute behind ", t6, " the time is 1:59PM")
    print("One minute behind ", t3, " the time is 10:09AM")
    print("One minute behind ", t12, " the time is 11:58PM")
    print("One minute behind ", t15, " the time is 12:59AM")

    print("*** Your output ***")
    print("One minute behind ", t1, " the time is ", t1.minute_back())
    print("One minute behind ", t4, " the time is ", t4.minute_back())
    print("One minute behind ", t6, " the time is ", t6.minute_back())
    print("One minute behind ", t3, " the time is ", t3.minute_back())
    print("One minute behind ", t12, " the time is ", t12.minute_back())
    print("One minute behind ", t15, " the time is ", t15.minute_back())

    print("\nThat wraps it up! Until next time........")
