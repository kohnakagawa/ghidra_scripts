import java.lang


class Column(object):
    """
    A row in a grid.   This class stores it's row index, its x offset and its width.  The
     x value is the layout space x value of a Point2D object.   That is, unlike the
     GridLocationMap, the x value of this object is in layout space and not indexes
     of a grid.
    """

    index: int
    width: int
    x: int



    def __init__(self, index: int): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getPaddedWidth(self, isCondensed: bool) -> int: ...

    def hashCode(self) -> int: ...

    def isInitialized(self) -> bool: ...

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
    def initialized(self) -> bool: ...
