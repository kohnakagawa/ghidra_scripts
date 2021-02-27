import java.lang


class VisitorResults(object):
    """
    Some constants for controlling traversal

     A callback () can return one of these constants to control whether or not
     traversal continues.  methods will return a value to indicate how traversal
     terminated.
    """

    CONTINUE: int = 0
    FINISHED: int = 1
    TERMINATE: int = 2







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

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
