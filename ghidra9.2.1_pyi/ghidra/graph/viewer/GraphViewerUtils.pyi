from typing import List
import com.google.common.base
import edu.uci.ics.jung.algorithms.layout
import edu.uci.ics.jung.graph
import edu.uci.ics.jung.visualization
import ghidra.graph.viewer
import ghidra.graph.viewer.event.mouse
import ghidra.graph.viewer.layout
import java.awt
import java.awt.event
import java.awt.geom
import java.awt.geom.Point2D
import java.lang
import java.util


class GraphViewerUtils(object):
    """
    This class houses various methods for translating location and size data from the various
     graph coordinate spaces.

     Graph Spaces
     Size and location information is represented in multiple coordinate spaces, as listed below.
     To translate from one to the other, use GraphViewerUtils; for example, to see if a
     mouse click is on a given vertex.


     	Layout Space - the layout contains Point2D objects that represent positions of the
                         vertices.
      Graph Space - the space where the Layout points are transformed as the view is moved
                        around the screen (e.g., as the user pans)
      View Space - the coordinate system of Java 2D rendering; scaling (zooming) transformations
                       are applied at this layer


      Note: vertex relative means that the value is from inside the vertex, or the vertex's
           coordinate space (like a component that is inside the vertex), where it's
           coordinate values are relative to the component's parent.
    """

    EDGE_COLUMN_SPACING: int = 25
    EDGE_ROW_SPACING: int = 25
    EXTRA_LAYOUT_COLUMN_SPACING: int = 50
    EXTRA_LAYOUT_COLUMN_SPACING_CONDENSED: int = 10
    EXTRA_LAYOUT_ROW_SPACING: int = 50
    EXTRA_LAYOUT_ROW_SPACING_CONDENSED: int = 25
    GRAPH_BUILDER_THREAD_POOL_NAME: unicode = u'Graph Builder'
    GRAPH_DECORATOR_THREAD_POOL_NAME: unicode = u'Graph Decorator'
    INTERACTION_ZOOM_THRESHOLD: float = 0.2
    PAINT_ZOOM_THRESHOLD: float = 0.1



    def __init__(self): ...



    @staticmethod
    def addPaddingToRectangle(padding: int, rectangle: java.awt.Rectangle) -> None: ...

    @staticmethod
    def adjustEdgePickSizeForZoom(viewer: edu.uci.ics.jung.visualization.VisualizationServer) -> None: ...

    @staticmethod
    def convertMouseEventToVertexMouseEvent(viewer: ghidra.graph.viewer.GraphViewer, mouseEvent: java.awt.event.MouseEvent) -> ghidra.graph.viewer.event.mouse.VertexMouseInfo: ...

    @staticmethod
    def createCollectionWithZOrderBySelection(vertices: java.util.Collection) -> List[V]:
        """
        Moves the selected vertices to the end of the list of vertices so that when picked (or
         painted), we will prefer the selected vertices, since we have configured the algorithms for
         the graph stuff to prefer the last accessed vertex (like when picking and painting).
        @param vertices the vertices to order
        @return the given vertices, ordered by selected/emphasized state
        """
        ...

    @overload
    @staticmethod
    def createEgdeLoopInGraphSpace(vertexShape: java.awt.Shape, x: float, y: float) -> java.awt.Shape:
        """
        Creates a loop shape for a vertex that calls itself.  The loop is transformed to graph space,
         which includes updating the size and location of the loop to be relative to
         the vertex.
        @param vertexShape The shape of the vertex for which the edge is being created.
        @param x The x coordinate of the vertex
        @param y The y coordinate of the vertex
        @return a loop shape for a vertex that calls itself.
        """
        ...

    @overload
    @staticmethod
    def createEgdeLoopInGraphSpace(edgeLoopShape: java.awt.Shape, vertexShape: java.awt.Shape, x: float, y: float) -> java.awt.Shape:
        """
        Transforms the given edge loop shape to graph space, which includes updating
         the size and location of the loop to be relative to the vertex.
        @param edgeLoopShape The shape to transform
        @param vertexShape The shape of the vertex for which the edge is being created
        @param x The x coordinate of the vertex
        @param y The y coordinate of the vertex
        @return the transformed edge loop shape
        """
        ...

    @staticmethod
    def createHollowEgdeLoop() -> java.awt.Shape: ...

    @staticmethod
    def createHollowEgdeLoopInGraphSpace(vertexShape: java.awt.Shape, x: float, y: float) -> java.awt.Shape:
        """
        Creates a self-loop edge to be used with a vertex that calls itself.  The returned shape
         is hollow (not a filled loop) so that mouse hit detection does not occur in the middle of
         the circle.
        @param vertexShape The shape of the vertex for which the edge is being created.
        @param x The x coordinate of the vertex
        @param y The y coordinate of the vertex
        @return a self-loop edge to be used with a vertex that calls itself.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    @overload
    @staticmethod
    def getBoundsForVerticesInLayoutSpace(viewer: edu.uci.ics.jung.visualization.VisualizationServer, vertices: java.util.Collection) -> java.awt.Rectangle:
        """
        Returns a rectangle that contains all give vertices
        @param viewer the viewer containing the UI
        @param vertices the vertices
        @return a rectangle that contains all give vertices
        """
        ...

    @overload
    @staticmethod
    def getBoundsForVerticesInLayoutSpace(vertices: java.util.Collection, vertexToBounds: com.google.common.base.Function) -> java.awt.Rectangle:
        """
        Returns a rectangle that contains all vertices, in the layout space
        @param vertices the vertices for which to calculate the bounds
        @param vertexToBounds a function that can turn a single vertex into a rectangle
        @return the bounds
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getEdgeFromPointInViewSpace(viewer: edu.uci.ics.jung.visualization.VisualizationServer, point: java.awt.Point) -> E: ...

    @staticmethod
    def getEdgeShapeInGraphSpace(__a0: edu.uci.ics.jung.visualization.VisualizationServer, __a1: object) -> java.awt.Shape: ...

    @staticmethod
    def getGraphCenterInLayoutSpace(viewer: edu.uci.ics.jung.visualization.VisualizationServer) -> java.awt.Point: ...

    @staticmethod
    def getGraphScale(vv: edu.uci.ics.jung.visualization.VisualizationServer) -> float: ...

    @staticmethod
    def getOffsetFromCenterForPointInViewSpace(viewer: edu.uci.ics.jung.visualization.VisualizationServer, point: java.awt.geom.Point2D) -> java.awt.geom.Point2D.Double: ...

    @staticmethod
    def getOffsetFromCenterInLayoutSpace(viewer: edu.uci.ics.jung.visualization.VisualizationServer, pointInLayoutSpace: java.awt.Point) -> java.awt.geom.Point2D.Double: ...

    @staticmethod
    def getPointInViewSpaceForVertex(__a0: edu.uci.ics.jung.visualization.VisualizationServer, __a1: object) -> java.awt.Point: ...

    @staticmethod
    def getScaleRatioToFitInDimension(currentSize: java.awt.Dimension, targetSize: java.awt.Dimension) -> float: ...

    @overload
    @staticmethod
    def getTotalGraphSizeInLayoutSpace(viewer: edu.uci.ics.jung.visualization.VisualizationServer) -> java.awt.Rectangle: ...

    @overload
    @staticmethod
    def getTotalGraphSizeInLayoutSpace(vertices: java.util.Collection, edges: java.util.Collection, vertexToBounds: com.google.common.base.Function, edgeToArticulations: com.google.common.base.Function) -> java.awt.Rectangle: ...

    @staticmethod
    def getVertexBoundsInGraphSpace(__a0: edu.uci.ics.jung.visualization.VisualizationServer, __a1: object) -> java.awt.Rectangle: ...

    @staticmethod
    def getVertexBoundsInLayoutSpace(__a0: edu.uci.ics.jung.visualization.VisualizationServer, __a1: object) -> java.awt.Rectangle: ...

    @staticmethod
    def getVertexBoundsInViewSpace(__a0: edu.uci.ics.jung.visualization.VisualizationServer, __a1: object) -> java.awt.Rectangle: ...

    @staticmethod
    def getVertexCenterPointInViewSpace(__a0: edu.uci.ics.jung.visualization.VisualizationServer, __a1: object) -> java.awt.geom.Point2D: ...

    @staticmethod
    def getVertexFromPointInViewSpace(viewer: edu.uci.ics.jung.visualization.VisualizationServer, point: java.awt.Point) -> V: ...

    @staticmethod
    def getVertexOffsetFromLayoutCenter(__a0: edu.uci.ics.jung.visualization.VisualizationServer, __a1: object) -> java.awt.geom.Point2D.Double: ...

    @staticmethod
    def getVertexOffsetFromLayoutCenterTop(__a0: edu.uci.ics.jung.visualization.VisualizationServer, __a1: object) -> java.awt.geom.Point2D.Double: ...

    @staticmethod
    def getVertexUpperLeftCornerInGraphSpace(__a0: edu.uci.ics.jung.visualization.VisualizationServer, __a1: object) -> java.awt.Point: ...

    @staticmethod
    def getVertexUpperLeftCornerInLayoutSpace(__a0: edu.uci.ics.jung.visualization.VisualizationServer, __a1: object) -> java.awt.Point: ...

    @staticmethod
    def getVertexUpperLeftCornerInViewSpace(__a0: edu.uci.ics.jung.visualization.VisualizationServer, __a1: object) -> java.awt.Point: ...

    @staticmethod
    def getVerticesOfHoveredEdges(graph: edu.uci.ics.jung.graph.Graph) -> java.util.Collection: ...

    @staticmethod
    def getVerticesOfSelectedEdges(graph: edu.uci.ics.jung.graph.Graph) -> java.util.Collection:
        """
        Returns a collection of vertices that are incident to selected edges.
        @param graph the graph from which to retrieve vertices
        @return a collection of vertices that are incident to selected edges.
        """
        ...

    @staticmethod
    def getVisualGraphLayout(graphLayout: edu.uci.ics.jung.algorithms.layout.Layout) -> ghidra.graph.viewer.layout.VisualGraphLayout: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isScaledPastVertexInteractionThreshold(viewer: edu.uci.ics.jung.visualization.VisualizationServer) -> bool: ...

    @staticmethod
    def layoutUsesEdgeArticulations(graphLayout: edu.uci.ics.jung.algorithms.layout.Layout) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def setGraphScale(viewer: edu.uci.ics.jung.visualization.VisualizationServer, scale: float) -> None: ...

    def toString(self) -> unicode: ...

    @staticmethod
    def translatePointFromGraphSpaceToLayoutSpace(pointInGraphSpace: java.awt.geom.Point2D, viewer: edu.uci.ics.jung.visualization.VisualizationServer) -> java.awt.Point: ...

    @staticmethod
    def translatePointFromGraphSpaceToViewSpace(pointInGraphSpace: java.awt.geom.Point2D, viewer: edu.uci.ics.jung.visualization.VisualizationServer) -> java.awt.Point: ...

    @staticmethod
    def translatePointFromLayoutSpaceToGraphSpace(pointInLayoutSpace: java.awt.geom.Point2D, viewer: edu.uci.ics.jung.visualization.VisualizationServer) -> java.awt.Point: ...

    @staticmethod
    def translatePointFromLayoutSpaceToViewSpace(pointInLayoutSpace: java.awt.geom.Point2D, viewer: edu.uci.ics.jung.visualization.VisualizationServer) -> java.awt.Point: ...

    @staticmethod
    def translatePointFromVertexRelativeSpaceToViewSpace(__a0: edu.uci.ics.jung.visualization.VisualizationServer, __a1: object, __a2: java.awt.Point) -> java.awt.Point: ...

    @staticmethod
    def translatePointFromViewSpaceToGraphSpace(pointInViewSpace: java.awt.geom.Point2D, viewer: edu.uci.ics.jung.visualization.VisualizationServer) -> java.awt.Point: ...

    @staticmethod
    def translatePointFromViewSpaceToLayoutSpace(pointInViewSpace: java.awt.geom.Point2D, viewer: edu.uci.ics.jung.visualization.VisualizationServer) -> java.awt.Point: ...

    @overload
    @staticmethod
    def translatePointFromViewSpaceToVertexRelativeSpace(viewer: edu.uci.ics.jung.visualization.VisualizationServer, startPoint: java.awt.Point) -> java.awt.Point: ...

    @overload
    @staticmethod
    def translatePointFromViewSpaceToVertexRelativeSpace(__a0: edu.uci.ics.jung.visualization.VisualizationServer, __a1: java.awt.Point, __a2: object) -> java.awt.Point: ...

    @staticmethod
    def translateRectangleFromLayoutSpaceToViewSpace(viewer: edu.uci.ics.jung.visualization.VisualizationServer, rectangle: java.awt.Rectangle) -> java.awt.Rectangle: ...

    @staticmethod
    def translateRectangleFromVertexRelativeSpaceToViewSpace(__a0: edu.uci.ics.jung.visualization.VisualizationServer, __a1: object, __a2: java.awt.Rectangle) -> java.awt.Rectangle: ...

    @staticmethod
    def translateShapeFromLayoutSpaceToGraphSpace(shape: java.awt.Shape, viewer: edu.uci.ics.jung.visualization.VisualizationServer) -> java.awt.Shape: ...

    @staticmethod
    def translateShapeFromLayoutSpaceToViewSpace(shape: java.awt.Shape, viewer: edu.uci.ics.jung.visualization.VisualizationServer) -> java.awt.Shape: ...

    @staticmethod
    def translateShapeFromViewSpaceToLayoutSpace(shape: java.awt.Shape, viewer: edu.uci.ics.jung.visualization.VisualizationServer) -> java.awt.Shape: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
