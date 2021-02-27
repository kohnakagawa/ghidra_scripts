import java.lang


class ToolSet(object):
    """
    Interface to define a set of Tools. NOTE: ToolSets are currently not
     implemented.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode:
        """
        Get the description of the toolset.
        """
        ...

    def getName(self) -> unicode:
        """
        Get the name for the toolset.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setName(self, name: unicode) -> None:
        """
        Set the name on the toolset.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def description(self) -> unicode: ...

    @property
    def name(self) -> unicode: ...

    @name.setter
    def name(self, value: unicode) -> None: ...
