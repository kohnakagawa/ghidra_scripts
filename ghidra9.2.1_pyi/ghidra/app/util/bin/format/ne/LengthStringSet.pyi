import java.lang


class LengthStringSet(object):
    """
    A class to store a length/string set,
     where the string is not null-terminated
     and the length field determines the string
     length
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getIndex(self) -> long:
        """
        Returns the byte index of this string,
         relative to the beginning of the file.
        @return the byte index of this string
        """
        ...

    def getLength(self) -> int:
        """
        Returns the length of the string.
        @return the length of the string
        """
        ...

    def getString(self) -> unicode:
        """
        Returns the string.
        @return the string
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def index(self) -> long: ...

    @property
    def length(self) -> int: ...

    @property
    def string(self) -> unicode: ...
