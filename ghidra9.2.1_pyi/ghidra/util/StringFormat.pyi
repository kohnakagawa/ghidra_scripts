import java.lang


class StringFormat(object):
    """
    Class with static methods formatting values in hex.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def hexByteString(b: int) -> unicode:
        """
        Gets a hexadecimal representation of a byte value.
        @param b the byte value
        @return the byte as a hexadecimal string.
        """
        ...

    @staticmethod
    def hexWordString(s: int) -> unicode:
        """
        Gets a hexadecimal representation of a short value.
        @param s the short value
        @return the short as a hexadecimal string.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def padIt(str: unicode, padlen: int, endchar: int, padded: bool) -> unicode:
        """
        Creates a string prepended with zeros, if padding is indicated, and adds
         the indicated endchar as the suffix.
        @param str the original string
        @param padlen length of the padded string without the suffix character.
        @param endchar the suffix character
        @param padded if true then prepend with zeros
        @return return the possibly padded string containing the suffix.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
