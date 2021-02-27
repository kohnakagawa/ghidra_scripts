import edu.uci.ics.jung.algorithms.layout
import edu.uci.ics.jung.visualization.picking
import java.awt
import java.lang
import java.util


class VisualGraphShapePickSupport(edu.uci.ics.jung.visualization.picking.ShapePickSupport):




    def __init__(self, viewer: edu.uci.ics.jung.visualization.VisualizationServer): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getEdge(self, layout: edu.uci.ics.jung.algorithms.layout.Layout, viewSpaceX: float, viewSpaceY: float) -> E:
        """
        Overridden to handle edge picking with our custom edge placement.  The painting and picking
         algorithms in Jung are all hard-coded to transform loop edges to above the vertex--there
         is no way to plug our own transformation into Jung :(
        @param layout
        @param viewSpaceX The x under which to look for an edge (view coordinates)
        @param viewSpaceY The y under which to look for an edge (view coordinates)
        @return The closest edge to the given point; null if no edge near the point
        """
        ...

    def getPickSize(self) -> float: ...

    def getStyle(self) -> edu.uci.ics.jung.visualization.picking.ShapePickSupport.Style: ...

    def getVertex(self, __a0: edu.uci.ics.jung.algorithms.layout.Layout, __a1: float, __a2: float) -> object: ...

    def getVertices(self, __a0: edu.uci.ics.jung.algorithms.layout.Layout, __a1: java.awt.Shape) -> java.util.Collection: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setPickSize(self, __a0: float) -> None: ...

    def setStyle(self, __a0: edu.uci.ics.jung.visualization.picking.ShapePickSupport.Style) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
