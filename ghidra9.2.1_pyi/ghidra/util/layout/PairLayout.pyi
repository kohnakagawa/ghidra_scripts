import java.awt
import java.lang


class PairLayout(object, java.awt.LayoutManager):
    """
    LayoutManger for arranging components into exactly two columns.  The right column and the
     left column may have differing widths.  Also, each row is the same height,
     which is the largest of all rows.
    """





    @overload
    def __init__(self): ...

    @overload
    def __init__(self, vgap: int, hgap: int):
        """
        Constructs a new PairLayout.
        @param vgap the gap (in pixels) between rows.
        @param hgap the gap (in pixels) between the two columns.
        """
        ...

    @overload
    def __init__(self, vgap: int, hgap: int, minimumRightColumnWidth: int):
        """
        Constructs a new PairLayout.
        @param vgap the gap (in pixels) between rows.
        @param hgap the gap (in pixels) between the two columns.
        @param minimumRightColumnWidth specifies the minimum width of the second column.
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

    def layoutContainer(self, parent: java.awt.Container) -> None: ...

    def minimumLayoutSize(self, parent: java.awt.Container) -> java.awt.Dimension: ...

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

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
