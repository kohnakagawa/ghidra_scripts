from typing import List
import java.lang


class Row(object):
    """
    A row in a grid.   This class stores its row index, its y offset and its height.   The
     y value is the layout space y value of a Point2D object.   That is, unlike the
     GridLocationMap, the y value of this object is in layout space and not indexes
     of a grid.

     This class maintains a collection of vertices on this row, organized by column index.  You
     can get the column of a vertex from #getColumn(Object).
    """

    height: int
    index: int
    y: int







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getColumn(self, __a0: object) -> int: ...

    def getColumnCount(self) -> int:
        """
        Represents the range of columns in this row.  For this given row in a grid:
         <pre>
         	0 1 2 3 4 5 6
         	- - v - v - -
         </pre>
         the column count is 3--where the column range is 2-4, inclusive.

         <p>Note: this differs from then number of vertices in this row, as the column count
         includes columns that have no vertex.
        @return the number of columns in this row, including empty columns between start and end
        """
        ...

    def getEndColumn(self) -> int:
        """
        Returns the largest column index in this row
        @return the largest column index in this row
        """
        ...

    def getPaddedHeight(self, isCondensed: bool) -> int: ...

    def getStartColumn(self) -> int:
        """
        Returns the smallest column index in this row
        @return the smallest column index in this row
        """
        ...

    def getVertex(self, column: int) -> V:
        """
        Returns the vertex at the given column index or null if there is no vertex at that column
        @param column the column index
        @return the vertex
        """
        ...

    def getVertices(self) -> List[V]:
        """
        Returns all vertices in this row, sorted by column index (min to max).

         <p>Note: the index of a vertex in the list does not match the column index.  To get the
         column index for a vertex, call {@link #getColumn(Object) getColumn(V)}.
        @return all vertices in this row
        """
        ...

    def hashCode(self) -> int: ...

    def isInitialized(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setColumn(self, __a0: object, __a1: int) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def columnCount(self) -> int: ...

    @property
    def endColumn(self) -> int: ...

    @property
    def initialized(self) -> bool: ...

    @property
    def startColumn(self) -> int: ...

    @property
    def vertices(self) -> List[object]: ...
