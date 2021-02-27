import edu.uci.ics.jung.algorithms.layout
import edu.uci.ics.jung.visualization
import ghidra.graph.viewer
import ghidra.graph.viewer.vertex
import java.awt
import java.lang


class VisualVertexSatelliteRenderer(ghidra.graph.viewer.vertex.AbstractVisualVertexRenderer):
    """
    A renderer for vertices for the satellite view.  This is really just a basic renderer
     that adds emphasis capability, as seen in the primary function graph renderer.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFullShape(self, __a0: edu.uci.ics.jung.visualization.RenderContext, __a1: edu.uci.ics.jung.algorithms.layout.Layout, __a2: ghidra.graph.viewer.VisualVertex) -> java.awt.Shape: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def paintVertex(self, __a0: edu.uci.ics.jung.visualization.RenderContext, __a1: edu.uci.ics.jung.algorithms.layout.Layout, __a2: object) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
