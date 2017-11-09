#
# hw10pr1.py
#
# name:
#

# First, the class definition
# Below, we define several useful objects of type Date
#  +++ keep those and/or add your own! +++


class Date:
    """ a user-defined data structure that
        stores and manipulates dates
    """

    # the constructor is always named __init__ !
    def __init__(self, month, day, year):
        """ the constructor for objects of type Date """
        self.month = month
        self.day = day
        self.year = year


    # the "printing" function is always named __repr__ !
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.
        """
        s =  "{:02d}/{:02d}/{:04d}".format(self.month, self.day, self.year)
        return s

    def copy(self):
        """ Returns a new object with the same month, day, year
            as the calling object (self).
        """
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        """ Decides if self and d2 represent the same calendar date,
            whether or not they are the in the same place in memory.
        """
        if self.year == d2.year and self.month == d2.month and self.day == d2.day:
            return True
        else:
            return False

    def __eq__(self, d2):
        """ Overrides the == operator so that it declares two of the same dates in history as ==
        This way , we don't need to use the awkward d.equals(d2) syntax...
        """
        if self.year == d2.year and self.month == d2.month and self.day == d2.day:
            return True
        else:
            return False

    def isBefore(self, d2):
        """ returns True is self is a calendar date before d2 and False otherwise
        """
        if self.year < d2.year:
            return True

        if self.month < d2.month and self.year == d2.year:
            return True

        if self.day < d2.day and self.year == d2.year and self.month < d2.month:
            return True

        return False

    def isAfter(self, d2):
        """ returns True is self is a calendar date after d2 and False otherwise
        """
        if self.year > d2.year:
            return True

        if self.month > d2.month and self.year == d2.year:
            return True

        if self.day > d2.day and self.year == d2.year and self.month < d2.month:
            return True

        return False



    # here is an example of a "method" of the Date class:
    def isLeapYear(self):
        """ Returns True if the calling object is
            in a leap year; False otherwise. """
        if self.year % 400 == 0: return True
        elif self.year % 100 == 0: return False
        elif self.year % 4 == 0: return True
        return False

    def tomorrow(self):
        if self.isLeapYear() == True:
            fdays = 29
        else:
            fdays = 28
        DIM = [0,31,fdays,31,30,31,30,31,31,30,31,30,31]
        self.day += 1
        if self.day > DIM[self.month]:
            self.month += 1
            self.day =1
            if self.month > 12:
               self.year += 1
               self.month = 1

    def yesterday(self):
        if self.isLeapYear() == True:
            fdays = 29
        else:
            fdays = 28
        DIM = [0, 31, fdays, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.day -= 1
        if self.day == 0:
            self.month += -1
            if self.month == 0:
                self.year += -1
                self.month = 12
            self.day = DIM[self.month]

    def addNDays(self, N):
        for i in range(N):
            self.tomorrow()
            print(self)

    def subNDays(self, N):
        for i in range(N):
            self.yesterday()
            print(self)




    def diff(self, d2):
        self_copy = self.copy()
        d2_copy = d2.copy()
        i = 0
        if self_copy.isBefore(d2_copy):
            while not (self_copy == d2_copy):
                self_copy.tomorrow()
                i -= 1
        if self_copy.isAfter(d2_copy):
            while not self_copy == d2_copy:
                self_copy.yesterday()
                i += 1
        return i
#
# be sure to add code for the Date class ABOVE -- inside the class definirun hw10pr1
#





#
# lots of dates to work with...
#
# The nice this about putting them here is that they get redefined with each run
#   of the software (and this is needed for testing!)
#

d = Date(11,12,2013)
d2 = Date(12,16,2017); # d = Date(11,8,2017)
ny = Date(1,1,2018)   # new year
nd = Date(1,1,2020)   # new decade
nc = Date(1,1,2100)   # new century
graduation = Date(5,16,2021)   # alter to suit!
vacation = Date(12,16,2017)    # ditto!
sm1 = Date(10,28,1929)    # stock market crash
sn2 = Date(10,19,1987)    # another s.m. crash: Mondays in Oct. are risky...

d = Date(11,8,2017)     # now...

d2 = Date(12,16,2017)    # winter break!

