import java.lang


class IndexRange(object):
    """
    Class for holding a begin and end index.
    """





    def __init__(self, start: long, end: long):
        """
        Constructor for IndexRange.
        @param start the starting index of the range.
        @param end the ending index of the range.
        """
        ...



    def equals(self, obj: object) -> bool:
        """
        @see java.lang.Object#equals(java.lang.Object)
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getEnd(self) -> long:
        """
        Returns the ending index of the range.
        @return the ending index of the range.
        """
        ...

    def getStart(self) -> long:
        """
        Returns the starting index of the range.
        @return the starting index of the range.
        """
        ...

    def hashCode(self) -> int:
        """
        @see java.lang.Object#hashCode()
        """
        ...

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
    def end(self) -> long: ...

    @property
    def start(self) -> long: ...
