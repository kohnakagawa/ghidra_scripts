import edu.uci.ics.jung.algorithms.layout
import edu.uci.ics.jung.graph
import edu.uci.ics.jung.visualization
import edu.uci.ics.jung.visualization.renderers
import ghidra.graph.viewer
import ghidra.graph.viewer.edge
import java.awt
import java.lang


class VisualGraphEdgeSatelliteRenderer(ghidra.graph.viewer.edge.VisualEdgeRenderer):
    """
    A renderer designed to override default edge rendering to NOT paint emphasizing effects.  We
     do this because space is limited in the satellite and because this rendering can take excess
     processing time.
    """





    def __init__(self, delegate: ghidra.graph.viewer.edge.VisualEdgeRenderer): ...



    @overload
    def drawSimpleEdge(self, __a0: edu.uci.ics.jung.visualization.RenderContext, __a1: edu.uci.ics.jung.algorithms.layout.Layout, __a2: ghidra.graph.viewer.VisualEdge) -> None: ...

    @overload
    def drawSimpleEdge(self, __a0: edu.uci.ics.jung.visualization.RenderContext, __a1: edu.uci.ics.jung.algorithms.layout.Layout, __a2: object) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getBaseColor(self, __a0: edu.uci.ics.jung.graph.Graph, __a1: ghidra.graph.viewer.VisualEdge) -> java.awt.Color: ...

    def getClass(self) -> java.lang.Class: ...

    def getEdgeArrowRenderingSupport(self) -> edu.uci.ics.jung.visualization.renderers.EdgeArrowRenderingSupport: ...

    def getEdgeShape(self, __a0: edu.uci.ics.jung.visualization.RenderContext, __a1: edu.uci.ics.jung.graph.Graph, __a2: ghidra.graph.viewer.VisualEdge, __a3: float, __a4: float, __a5: float, __a6: float, __a7: bool, __a8: java.awt.Shape) -> java.awt.Shape: ...

    def getFullShape(self, __a0: edu.uci.ics.jung.visualization.RenderContext, __a1: edu.uci.ics.jung.algorithms.layout.Layout, __a2: ghidra.graph.viewer.VisualVertex) -> java.awt.Shape: ...

    def getHighlightColor(self, __a0: edu.uci.ics.jung.graph.Graph, __a1: ghidra.graph.viewer.VisualEdge) -> java.awt.Color: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def paintEdge(self, __a0: edu.uci.ics.jung.visualization.RenderContext, __a1: edu.uci.ics.jung.algorithms.layout.Layout, __a2: object) -> None: ...

    def setBaseColor(self, color: java.awt.Color) -> None: ...

    def setDashingPatternOffset(self, dashingPatterOffset: float) -> None:
        """
        Sets the offset value for painting dashed lines.  This allows clients to animate the
         lines being drawn for edges in the edge direction.
        @param dashingPatterOffset the offset value
        """
        ...

    def setEdgeArrowRenderingSupport(self, __a0: edu.uci.ics.jung.visualization.renderers.EdgeArrowRenderingSupport) -> None: ...

    def setHighlightColor(self, highlightColor: java.awt.Color) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
