import java.awt
import java.lang


class VariableHeightPairLayout(object, java.awt.LayoutManager):
    """
    LayoutManger for arranging components into exactly two columns.
    """





    @overload
    def __init__(self):
        """
        Constructor for PairLayout.
        """
        ...

    @overload
    def __init__(self, vgap: int, hgap: int):
        """
        Constructs a new PairLayout.
        @param vgap the gap (in pixels) between rows.
        @param hgap the gap (in pixels) between the two columns.
        """
        ...

    @overload
    def __init__(self, vgap: int, hgap: int, preferredWidth2: int):
        """
        Constructs a new PairLayout.
        @param vgap the gap (in pixels) between rows.
        @param hgap the gap (in pixels) between the two columns.
        @param preferredWidth2 specifies the preferred width of the second column.
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

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
