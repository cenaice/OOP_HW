
"""
Object Oriented Programming, Fall 2022
Test module for Homework 4, Problem 1
"""

from time import *

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

    print("------------------------------------------------------ ")
    print("This test program tests your implementation of the ")
    print("Time class overloaded operators, the time_interval function,")
    print("and the time_schedule function")
    print("The correct output will be shown along with the output")
    print("given by your implementation. ")
    print("------------------------------------------------------ \n")


    print("\nTesting the overloaded + operator")
    print("---------------------------------\n")

    print("*** Correct output ***")
    print("201 minutes after   ", t2, " the time is 5:51AM")
    print("645 minutes after   ", t3, " the time is 8:55PM")
    print("2450 minutes after  ", t5, " the time is 5:05AM")
    print("49 minutes after    ", t8, " the time is 7:07PM")
    print("800 minutes after   ", t7, " the time is 4:32AM")
    print("6100 minutes after  ", t9, " the time is 12:40AM")

    print("*** Your output ***")
    print("201 minutes after   ", t2, " the time is", t2 + 201)
    print("645 minutes after   ", t3, " the time is", t3 + 645)
    print("2450 minutes after  ", t5, " the time is", t5 + 2450)
    print("49 minutes after    ", t8, " the time is", t8 + 49)
    print("800 minutes after   ", t7, " the time is", t7 + 800)
    print("6100 minutes after  ", t9, " the time is", t9 + 6100)

    ans = input("\nReady for the next test [y/n]?")
    if (ans != 'y'):
        exit()

    print("\nTesting the overloaded - operator")
    print("---------------------------------\n")

    print("*** Correct output ***")
    print("201 minutes before    ", t1, " the time is 8:39PM")
    print("645 minutes before    ", t4, " the time is 1:15AM")
    print("2450 minutes before   ", t6, " the time is 9:10PM")
    print("49 minutes before     ", t10, " the time is 8:53PM")
    print("800 minutes before    ", t11, " the time is 9:28AM")
    print("6100 minutes before   ", t12, " the time is 6:19PM")
    
    print("*** Your output ***")
    print("201 minutes before    ", t1, " the time is", t1 - 201)
    print("645 minutes before    ", t4, " the time is", t4 - 645)
    print("2450 minutes before   ", t6, " the time is", t6 - 2450)
    print("49 minutes before     ", t10, " the time is", t10 - 49)
    print("800 minutes before    ", t11, " the time is", t11 - 800)
    print("6100 minutes before   ", t12, " the time is", t12 - 6100)

    ans = input("\nReady for the next test [y/n]?")
    if (ans != 'y'):
        exit()

    t13 = Time()
    t14 = Time()
    t15 = Time(5, 30, "am")
    t16 = Time(11, 45, "am")
    t17 = Time(1, 11, "pm")
    t18 = Time(8, 29, "pm")
    t19 = Time(8, 28, "pm")

    print("\nTesting the overloaded == operator")
    print("----------------------------------\n")

    if (t13 == t14):
        print(t13, " and ", t14, " are equal. (CORRECT) ")
    else:
        print(t13, " and ", t14, " are not equal. (WRONG) ")
    if (t13 == t16):
        print(t13, " and ", t16, " are equal. (WRONG) ")
    else:
        print(t13, " and ", t16, " are not equal. (CORRECT) ")

    t13 = t13 + 1
    if (t13 == t14):
        print(t13, " and ", t14, " are equal. (WRONG) ")
    else:
        print(t13, " and ", t14, " are not equal. (CORRECT) ")
    t13 = t13 - 1

    t15 = t15 + 15
    if (t15 == t16):
        print(t15, " and ", t16, " are equal. (WRONG) ")
    else:
        print(t15, " and ", t16, " are not equal. (CORRECT) ")
    t15 = t15 - 15

    ans = input("\nReady for the next test [y/n]?")
    if (ans != 'y'):
        exit()

    print("\nTesting the overloaded < operator")
    print("---------------------------------\n")

    if (t13 < t14):
        print(t13, " occurs before ", t14, " (WRONG) ")
    else:
        print(t13, " does not occur before ", t14, " (CORRECT) ")
    if (t15 < t16):
        print(t15, " occurs before ", t16, " (CORRECT) ")
    else:
        print(t15, " does not occur before ", t16, " (WRONG) ")
    if (t17 < t14):
        print(t17, " occurs before ", t14, " (WRONG) ")
    else:
        print( t17, " does not occur before ", t14, " (CORRECT) ")
    if (t18 < t19):
        print(t18, " occurs before ", t19, " (WRONG) ")
    else:
        print(t18, " does not occur before ", t19, " (CORRECT) ")

    ans = input("\nReady for the next test [y/n]?")
    if (ans != 'y'):
        exit()

    print("\nTesting the overloaded operator > function ")
    print("------------------------------------------ \n")

    if (t13 > t14):
        print(t13, " occurs after ", t14, " (WRONG) ")
    else:
        print(t13, " does not occur after ", t14, " (CORRECT) ")
    if (t15 > t14):
        print(t15, " occurs after ", t14, " (CORRECT) ")
    else:
        print(t15, " does not occur after ", t14, " (WRONG) ")
    if (t16 > t17):
        print(t16, " occurs after ", t17, " (WRONG) ")
    else:
        print(t16, " does not occur after ", t17, " (CORRECT) ")
    if (t18 > t19):
        print(t18, " occurs after ", t19, " (CORRECT) ")
    else:
        print(t18, " does not occur after ", t19, " (WRONG) ")

    ans = input("\nReady for the next test [y/n]?")
    if (ans != 'y'):
        exit()

    print("\nTesting the time_interval(...) function")
    print("---------------------------------------\n")

    (h, m) = time_interval(t13, t14)
    print("Correct answer: The time interval between ", t13, " and ", t14)
    print("                is 0 hours and 0 minutes. ")
    print("   Your answer: The time interval between ", t13, " and ", t14)
    print("                is ", h, " hours and ", m, " minutes. ")

    (h, m) = time_interval(t15, t16)
    print()
    print( "Correct answer: The time interval between ", t15, " and ", t16)
    print( "                is 6 hours and 15 minutes. ")
    print( "   Your answer: The time interval between ", t15, " and ", t16)
    print( "                is ", h, " hours and ", m, " minutes. ")

    (h, m) = time_interval(t16, t17)
    print()
    print("Correct answer: The time interval between ", t16, " and ", t17)
    print("                is 1 hour and 26 minutes. ")
    print("   Your answer: The time interval between ", t16, " and ", t17)
    print("                is ", h, " hours and ", m, " minutes. ")

    (h, m) = time_interval(t19, t18)
    print()
    print("Correct answer: The time interval between ", t19, " and ", t18)
    print("                is 0 hours and 1 minute.  ")
    print("   Your answer: The time interval between ", t19, " and ", t18)
    print("                is ", h, " hours and ", m, " minutes. ")

    (h, m) = time_interval(t13, t18)
    print()
    print("Correct answer: The time interval between ", t13, " and ", t18)
    print("                is 20 hours and 29 minutes. ")
    print("   Your answer: The time interval between ", t13, " and ", t18)
    print("                is ", h, " hours and ", m, " minutes. ")

    t19 = Time(10, 45, "am")

    ans = input("\nReady for the next test [y/n]?")
    if (ans != 'y'):
        exit()

    print("\nTesting the time_schedule(...) function")
    print("---------------------------------------\n")

    L = time_schedule(t19, 12, 10)
    print("Starting at ", t19, "the 10 times occurring every 12 minutes are: ")
    print("Correct answer: [10:45AM, 10:57AM, 11:09AM, 11:21AM, 11:33AM, 11:45AM, 11:57AM, 12:09PM, 12:21PM, 12:33PM]")
    print("   Your answer:", L)

    L = time_schedule(t17, 15, 1)
    print()
    print("Starting at ", t17, "the 1 time occurring every 15 minutes is: ")
    print("Correct answer: [1:11PM]")
    print("   Your answer:", L)

    L = time_schedule(t15, 30, 12)
    print()    
    print("Starting at ", t15, "the 12 times occurring every 30 minutes are: ")
    print("Correct answer: [5:30AM, 6:00AM, 6:30AM, 7:00AM, 7:30AM, 8:00AM, 8:30AM, 9:00AM, 9:30AM, 10:00AM, 10:30AM, 11:00AM]")
    print("   Your answer:", L)

    L = time_schedule(t18, 75, 6)
    print()    
    print("Starting at ", t18, "the 6 times occurring every 75 minutes are: ")
    print("Correct answer: [8:29PM, 9:44PM, 10:59PM, 12:14AM, 1:29AM, 2:44AM]")
    print("   Your answer:", L)

    L = time_schedule(t16, 54, 8)
    print()    
    print("Starting at ", t16, "the 8 times occurring every 54 minutes are: ")
    print("Correct answer: [11:45AM, 12:39PM, 1:33PM, 2:27PM, 3:21PM, 4:15PM, 5:09PM, 6:03PM]")
    print("   Your answer:", L)


    print("\nThat wraps it up! Until next time........")
