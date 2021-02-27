import ghidra.service.graph
import java.lang
import java.util


class GraphDisplayListener(object):
    """
    Interface for being notified when the user interacts with a visual graph display
    """









    def cloneWith(self, graphDisplay: ghidra.service.graph.GraphDisplay) -> ghidra.service.graph.GraphDisplayListener:
        """
        Makes a new GraphDisplayListener of the same type as the specific
         instance of this GraphDisplayListener
        @param graphDisplay the new {@link GraphDisplay} the new listener will support
        @return A new instance of a GraphDisplayListener that is the same type as as the instance
         on which it is called
        """
        ...

    def dispose(self) -> None:
        """
        Tells the listener that it is no longer needed and it can release any listeners/resources
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def graphClosed(self) -> None:
        """
        Notification that the graph window has been closed
        """
        ...

    def hashCode(self) -> int: ...

    def locationFocusChanged(self, vertex: ghidra.service.graph.AttributedVertex) -> None:
        """
        Notification that the "focused" (active) vertex has changed
        @param vertex the vertex that is currently "focused"
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def selectionChanged(self, vertices: java.util.Set) -> None:
        """
        Notification that the set of selected vertices has changed
        @param vertices the set of currently selected vertices
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
