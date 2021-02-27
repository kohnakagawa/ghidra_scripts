import java.io
import java.lang


class IntIndexManager(object, java.io.Serializable):
    """
    Class to generate int indexes to be used for arrays or tables.  If a location
     or entry in a table becomes available, the index for that location is released.
     This class manages the use and reuse of those indexes.
    """





    def __init__(self):
        """
        Constructs an IntIndexManager.
        """
        ...



    def allocate(self) -> int:
        """
        Returns the smallest unused index value.
        @exception IndexOutOfBoundsException thrown if there are no unused
         indexes.
        """
        ...

    def clear(self) -> None:
        """
        frees all index values.
        """
        ...

    def deallocate(self, index: int) -> None:
        """
        Returns the index value so that it can be reused.
        @param index the index to be free'd for reuse.
        """
        ...

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
