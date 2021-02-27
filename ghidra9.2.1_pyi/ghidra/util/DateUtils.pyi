from typing import List
import java.lang
import java.util


class DateUtils(object):
    MS_PER_DAY: long = 0x5265c00L
    MS_PER_HOUR: long = 0x36ee80L
    MS_PER_MIN: long = 0xea60L
    MS_PER_SEC: long = 0x3e8L



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def formatCurrentTime() -> unicode:
        """
        Returns the current local time zone time-of-day as simple time string.
         See {@value #TIME_FORMAT_STRING}.
        @return current time-of-day a a string
        """
        ...

    @staticmethod
    def formatDate(date: java.util.Date) -> unicode:
        """
        Formats the given date into a string.   This is in contrast to
         {@link #formatDateTimestamp(Date)}, which will also return the time portion of the date.
        @param date the date to format
        @return the date string
        """
        ...

    @staticmethod
    def formatDateTimestamp(date: java.util.Date) -> unicode:
        """
        Formats the given date into a string that contains the date and time.  This is in
         contrast to {@link #formatDate(Date)}, which only returns a date string.
        @param date the date to format
        @return the date and time string
        """
        ...

    @staticmethod
    def formatDuration(millis: long) -> unicode:
        """
        Formats a millisecond duration as a English string expressing the number of
         hours, minutes and seconds in the duration
        @param millis Count of milliseconds of an elapsed duration.
        @return String such as "5 hours, 3 mins, 22 secs".
        """
        ...

    @staticmethod
    def getBusinessDaysBetween(date1: java.util.Date, date2: java.util.Date) -> int:
        """
        Returns the <b>business days</b> between the two dates.  Returns 0 if the same date is
         passed for both parameters.  The order of the dates does not matter.
        @param date1 the first date
        @param date2 the second date
        @return the number of days
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getDate(year: int, month: int, day: int) -> java.util.Date:
        """
        Returns a date for the given numeric values
        @param year the year
        @param month the month; 0-based
        @param day the day of month; 1-based
        @return the date
        """
        ...

    @staticmethod
    def getDaysBetween(date1: java.util.Date, date2: java.util.Date) -> int:
        """
        Returns all days between the two dates.  Returns 0 if the same date is passed for both
         parameters.  The order of the dates does not matter.
        @param date1 the first date
        @param date2 the second date
        @return the number of days
        """
        ...

    @staticmethod
    def getHolidays(year: int) -> List[java.util.Date]: ...

    @staticmethod
    def getNormalizedToday() -> java.util.Date: ...

    def hashCode(self) -> int: ...

    @overload
    @staticmethod
    def isHoliday(cal: java.util.Calendar) -> bool: ...

    @overload
    @staticmethod
    def isHoliday(date: java.util.Date) -> bool: ...

    @staticmethod
    def isWeekend(cal: java.util.Calendar) -> bool: ...

    @staticmethod
    def normalizeDate(date: java.util.Date) -> java.util.Date: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
