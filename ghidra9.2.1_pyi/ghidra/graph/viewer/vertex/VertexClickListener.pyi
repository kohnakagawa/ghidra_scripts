import ghidra.graph.viewer
import ghidra.graph.viewer.event.mouse
import java.lang


class VertexClickListener(object):
    """
    A listener that allows clients to be notified of vertex clicks.  Normal
     mouse processing is handled by the VisualGraphMousePlugin class.  This is a
     convenience method so that clients do not have to deal with the mouse plugin.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    def vertexDoubleClicked(self, __a0: ghidra.graph.viewer.VisualVertex, __a1: ghidra.graph.viewer.event.mouse.VertexMouseInfo) -> bool: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
