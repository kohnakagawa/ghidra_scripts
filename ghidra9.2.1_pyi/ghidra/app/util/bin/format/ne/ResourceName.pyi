import java.lang


class ResourceName(object):
    """
    A class for storing new-executable resource names.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getIndex(self) -> long:
        """
        Returns the byte index of this resource name, relative to the beginning of the file.
        @return the byte index of this resource name
        """
        ...

    def getLength(self) -> int:
        """
        Returns the length of the resource name.
        @return the length of the resource name
        """
        ...

    def getName(self) -> unicode:
        """
        Returns the name of the resource name.
        @return the name of the resource name
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
    def name(self) -> unicode: ...
