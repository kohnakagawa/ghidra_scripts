import java.awt
import java.lang


class VerticalLayout(object, java.awt.LayoutManager):
    """
    LayoutManager for arranging components in a single column.  All components
     retain their preferred heights, but are sized to the same width.
    """





    def __init__(self, vgap: int):
        """
        Constructor for VerticalLayout.
        @param vgap gap (in pixels) between components.
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
