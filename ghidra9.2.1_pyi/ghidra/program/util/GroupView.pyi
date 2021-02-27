import ghidra.program.util
import java.io
import java.lang


class GroupView(object, java.io.Serializable):
    """
    Class to define a selection of GroupPath objects.
    """





    @overload
    def __init__(self, paths: List[ghidra.program.util.GroupPath]):
        """
        Constructor
        @param paths paths in the view
        """
        ...

    @overload
    def __init__(self, path: ghidra.program.util.GroupPath):
        """
        Constructor for a single path in the view.
        @param path the path that is used to create this view.
        """
        ...



    def addPath(self, path: ghidra.program.util.GroupPath) -> None:
        """
        Add the given group path to this view.
        @param path path to add
        """
        ...

    def equals(self, obj: object) -> bool:
        """
        Test if the given object is equal to this.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getCount(self) -> int:
        """
        Get the number of paths in the view
        """
        ...

    def getPath(self, index: int) -> ghidra.program.util.GroupPath:
        """
        Get the path at the specified index.
        @param index the index of the desired path in the view.
        @throws ArrayIndexOutOfBoundsException if index is invalid.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode:
        """
        Return string representation for this object.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def count(self) -> int: ...
