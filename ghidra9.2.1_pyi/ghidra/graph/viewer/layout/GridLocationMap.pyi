from typing import List
import ghidra.graph.viewer.layout
import java.lang


class GridLocationMap(object):
    """
    An object that maps vertices to rows and columns and edges to their articulation points.
     This class is essentially a container that allows layout algorithms to store results, which
     can later be turned into layout positioning points.   The integer point values in this
     class are row, column grid values, starting at 0,0.

     Note: the Point2D values for the edge articulations use x,y values that are row and
     column index values, the same values as calling #row(Object) and #col(Object).

     After building the grid using this class, clients can call #rows() to get
     high-order object that represent rows.
    """





    def __init__(self): ...



    def centerRows(self) -> None:
        """
        Updates each row within the grid such that it's x values are set to center the row in
         the grid.  Each row will be updated so that all its columns start at zero.  After that,
         each column will be centered in the grid.
        """
        ...

    @overload
    def col(self, __a0: object) -> int: ...

    @overload
    def col(self, __a0: object, __a1: int) -> None: ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getArticulations(self, __a0: object) -> List[object]: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def row(self, __a0: object) -> int: ...

    @overload
    def row(self, __a0: object, __a1: int) -> None: ...

    def rows(self) -> List[ghidra.graph.viewer.layout.Row]:
        """
        Returns the rows in this grid, sorted by index (index can be negative)
        @return the rows in this grid
        """
        ...

    def set(self, __a0: object, __a1: int, __a2: int) -> None: ...

    def setArticulations(self, __a0: object, __a1: List[object]) -> None: ...

    def toString(self) -> unicode: ...

    def toStringGrid(self) -> unicode:
        """
        Creates a string representation of this grid
        @return a string representation of this grid
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
