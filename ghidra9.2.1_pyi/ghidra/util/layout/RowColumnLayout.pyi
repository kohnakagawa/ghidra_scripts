import java.awt
import java.lang


class RowColumnLayout(object, java.awt.LayoutManager):
    """
    This layout arranges components in rows, putting as many components as possible on a
     row and using as many rows as necessary. All components are sized the same, the largest width
     and the largest height of all components.  The components prefer to be layout as close to
     a square as possible.
    """

    COLUMN: int = 1
    LEFT_TO_RIGHT: int = 0
    ROW: int = 0
    TOP_TO_BOTTOM: int = 1



    def __init__(self, hgap: int, vgap: int, orientation: int, maxSize: int):
        """
        Constructs a new RowColumnLayout
        @param hgap the gap (in pixels) between columns
        @param vgap the gap (in pixels) between rows
        @param orientation either ROW or COLUMN.  If ROW, components are layed out
         in rows up to prefered width, using as many rows a necessary.  If COLUMN, components are layed out
         in columns up to the prefered height, using as many columns as necessary.
        @param maxSize
        """
        ...



    def addLayoutComponent(self, name: unicode, comp: java.awt.Component) -> None:
        """
        @see LayoutManager#addLayoutComponent(String, Component)
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def layoutContainer(self, parent: java.awt.Container) -> None:
        """
        @see LayoutManager#layoutContainer(Container)
        """
        ...

    def minimumLayoutSize(self, parent: java.awt.Container) -> java.awt.Dimension:
        """
        @see LayoutManager#minimumLayoutSize(Container)
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def preferredLayoutSize(self, parent: java.awt.Container) -> java.awt.Dimension:
        """
        @see LayoutManager#preferredLayoutSize(Container)
        """
        ...

    def removeLayoutComponent(self, comp: java.awt.Component) -> None:
        """
        @see LayoutManager#removeLayoutComponent(Component)
        """
        ...

    def setMaxSize(self, maxSize: int) -> None:
        """
        @param maxSize
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
    def maxSize(self) -> None: ...  # No getter available.

    @maxSize.setter
    def maxSize(self, value: int) -> None: ...
