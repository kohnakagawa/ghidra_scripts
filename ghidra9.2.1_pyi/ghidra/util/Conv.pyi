from typing import List
import java.lang


class Conv(object):
    """
    Helper methods for converting between
     number data types without negative
     promotion.
    """

    BYTE_MASK: int = 255
    INT_MASK: long = 0xffffffffL
    SHORT_MASK: int = 65535







    @staticmethod
    def byteToInt(b: int) -> int:
        """
        Converts a byte to an integer.
        @param b the byte
        @return the integer equivalent of the byte
        """
        ...

    @staticmethod
    def byteToLong(b: int) -> long:
        """
        Converts a byte to a long.
        @param b the byte
        @return the long equivalent of the byte
        """
        ...

    @staticmethod
    def byteToShort(b: int) -> int:
        """
        Converts a byte to a short.
        @param b the byte
        @return the short equivalent of the byte
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def intToLong(i: int) -> long:
        """
        Converts an integer to a long.
        @param i the integer
        @return the long equivalent of the long
        """
        ...

    @staticmethod
    def main(args: List[unicode]) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def shortToInt(s: int) -> int:
        """
        Converts a short to an integer.
        @param s the short
        @return the integer equivalent of the short
        """
        ...

    @staticmethod
    def shortToLong(s: int) -> long:
        """
        Converts a short to a long.
        @param s the short
        @return the long eqivalent of the short
        """
        ...

    @overload
    @staticmethod
    def toHexString(l: long) -> unicode:
        """
        Converts a long into a padded hex string.
        @param l the long
        @return the padded hex string
        """
        ...

    @overload
    @staticmethod
    def toHexString(b: int) -> unicode:
        """
        Converts a byte into a padded hex string.
        @param b the byte
        @return the padded hex string
        """
        ...

    @overload
    @staticmethod
    def toHexString(b: int) -> unicode:
        """
        Converts a byte into a padded hex string.
        @param b the byte
        @return the padded hex string
        """
        ...

    @overload
    @staticmethod
    def toHexString(b: int) -> unicode:
        """
        Converts a byte into a padded hex string.
        @param b the byte
        @return the padded hex string
        """
        ...

    @overload
    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def toString(array: List[int]) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @staticmethod
    def zeropad(s: unicode, len: int) -> unicode:
        """
        Returns a string that is extended to
         length len with zeroes.
        @param s The string to pad
        @param len The length of the return string
        @return A string that has been padded to be of legnth len
        """
        ...
