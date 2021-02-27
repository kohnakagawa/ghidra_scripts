import edu.uci.ics.jung.algorithms.layout
import edu.uci.ics.jung.graph
import edu.uci.ics.jung.visualization
import edu.uci.ics.jung.visualization.renderers
import ghidra.graph.viewer
import java.awt
import java.lang


class VisualEdgeRenderer(edu.uci.ics.jung.visualization.renderers.BasicEdgeRenderer):
    """
    Edge render for the VisualGraph system

     Implementation Notes

     Jung Vertex/Edge Rendering
     Jung creates shapes for vertices (see VertexShapeFactory) that are centered.  They
     do this by getting the width/height of the shape and then creating an x/y value that is
     half of the width and height, respectively.  This has the effect of the vertex appearing
     centered over its connected edge.  We mimic that with our
     VisualGraphVertexShapeTransformer so that our edge rendering code is similar to
     Jung's.
     If we ever decide instead to not center our shapes, then this renderer would have to be
     updated to itself center the edge shape created herein, like this:

     Also, there are other spots in the system where we account for this center that would
     have to be changed, such as the AbstractVisualGraphLayout, which needs the centering
     offsets to handle vertex clipping.
    """





    def __init__(self): ...



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

    @property
    def baseColor(self) -> None: ...  # No getter available.

    @baseColor.setter
    def baseColor(self, value: java.awt.Color) -> None: ...

    @property
    def dashingPatternOffset(self) -> None: ...  # No getter available.

    @dashingPatternOffset.setter
    def dashingPatternOffset(self, value: float) -> None: ...

    @property
    def highlightColor(self) -> None: ...  # No getter available.

    @highlightColor.setter
    def highlightColor(self, value: java.awt.Color) -> None: ...
