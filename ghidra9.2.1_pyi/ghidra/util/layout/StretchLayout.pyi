import java.awt
import java.io
import java.lang


class StretchLayout(object, java.awt.LayoutManager, java.io.Serializable):
    """
    A layout manager that gives the affect of CENTER in BorderLayout.
    """





    def __init__(self): ...



    def addLayoutComponent(self, name: unicode, comp: java.awt.Component) -> None:
        """
        @see java.awt.LayoutManager#addLayoutComponent(java.lang.String, java.awt.Component)
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def layoutContainer(self, container: java.awt.Container) -> None:
        """
        @see java.awt.LayoutManager#layoutContainer(java.awt.Container)
        """
        ...

    def minimumLayoutSize(self, cont: java.awt.Container) -> java.awt.Dimension:
        """
        @see java.awt.LayoutManager#minimumLayoutSize(java.awt.Container)
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def preferredLayoutSize(self, container: java.awt.Container) -> java.awt.Dimension:
        """
        @see java.awt.LayoutManager#preferredLayoutSize(java.awt.Container)
        """
        ...

    def removeLayoutComponent(self, comp: java.awt.Component) -> None:
        """
        @see java.awt.LayoutManager#removeLayoutComponent(java.awt.Component)
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
