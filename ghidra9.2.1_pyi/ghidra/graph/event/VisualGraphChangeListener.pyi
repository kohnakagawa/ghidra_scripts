import java.lang


class VisualGraphChangeListener(object):
    """
    A listener to get notified of graph changes.
    """









    def edgesAdded(self, edges: java.lang.Iterable) -> None:
        """
        Called when the given edges have been added from the graph
        @param edges the added edges
        """
        ...

    def edgesRemoved(self, edges: java.lang.Iterable) -> None:
        """
        Called when the given edges have been removed from the graph
        @param edges the removed edges
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    def verticesAdded(self, vertices: java.lang.Iterable) -> None:
        """
        Called when the given vertices have been added from the graph
        @param vertices the added vertices
        """
        ...

    def verticesRemoved(self, vertices: java.lang.Iterable) -> None:
        """
        Called when the given vertices have been removed from the graph
        @param vertices the removed vertices
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
