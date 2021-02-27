import java.lang


class FieldStringInfo(object):
    """
    A simple data container class that contains a part string that is part of a parent string with the
     index of the part string into the parent string.
    """





    def __init__(self, parentString: unicode, fieldString: unicode, offset: int):
        """
        @param parentString The parent string
        @param fieldString The part string that exists within the parent
        @param offset the offset of the part string into the parent
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFieldString(self) -> unicode:
        """
        The string that exists within the parent string.
        @return The string that exists within the parent string.
        """
        ...

    def getOffset(self) -> int:
        """
        The offset of the part string into the parent string
        @return The offset of the part string into the parent string
        """
        ...

    def getParentString(self) -> unicode:
        """
        The string that contains the field string
        @return The string that contains the field string
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
    def fieldString(self) -> unicode: ...

    @property
    def offset(self) -> int: ...

    @property
    def parentString(self) -> unicode: ...
