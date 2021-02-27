import java.awt
import java.lang


class MaximizeSpecificColumnGridLayout(object, java.awt.LayoutManager):
    """
    MaximizeSpecificColumnGridLayout is a row oriented grid type of layout.
     It lays out rows of information in a table format using a specific number of columns.
     Components are added left to right and top to bottom. The table will try to give each column
     the width that is necessary to display the longest item in that column. The columns with the
     widest desired component size will get reduced first if there isn't enough room.
     The maximizeColumn(int) method allows you to indicate that you want to try to keep the size
     of a column at the preferred size of the widest component in that column as the parent
     container component is resized. Any column that has been maximized won't shrink until the
     non-maximized windows are reduced to a width of zero.
     The intent is that all non-maximized columns will shrink from largest to smallest so that
     they all will become zero width together at which point the maximized columns will begin
     shrinking in a similar manner.
    """





    @overload
    def __init__(self, columnCount: int):
        """
        Constructor with no gap between rows or columns.
        @param columnCount the number of columns in this grid
        """
        ...

    @overload
    def __init__(self, vgap: int, hgap: int, columnCount: int):
        """
        Constructor.
        @param vgap the gap (in pixels) between rows.
        @param hgap the gap (in pixels) between the two columns.
        @param columnCount the number of columns in this grid
        """
        ...



    def addLayoutComponent(self, name: unicode, comp: java.awt.Component) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def layoutContainer(self, parent: java.awt.Container) -> None: ...

    def maximizeColumn(self, column: int) -> None:
        """
        Allows you to indicate that you want to try to keep the size of a column at the preferred
         size of the widest component in that column as the parent container component is resized.
         Any column that has been maximized won't shrink until the non-maximized windows are reduced
         to a width of zero.
        @param column the number (0 based) of the column to keep maximized.
        """
        ...

    def minimumLayoutSize(self, parent: java.awt.Container) -> java.awt.Dimension: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def preferredLayoutSize(self, parent: java.awt.Container) -> java.awt.Dimension: ...

    def removeLayoutComponent(self, comp: java.awt.Component) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
