import edu.uci.ics.jung.visualization
import ghidra.graph.viewer
import ghidra.graph.viewer.edge
import ghidra.graph.viewer.options
import ghidra.graph.viewer.vertex
import java.awt
import java.lang
import java.util
import javax.swing


class GraphComponent(object):
    """
    A component that contains primary and satellite graph views.  This viewer provides
     methods for manipulating the graph using the mouse.

     To gain the full functionality offered by this class, clients will need to subclass
     this class and override #createPrimaryGraphViewer(VisualGraphLayout, Dimension)
     and #createSatelliteGraphViewer(GraphViewer, Dimension) as needed.   This allows
     them to customize renderers and other viewer attributes.  To use the subclass, see the
     VisualGraphView and its installGraphViewer() method.
    """





    def __init__(self, __a0: ghidra.graph.VisualGraph): ...



    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getComponent(self) -> javax.swing.JComponent: ...

    def getGraph(self) -> G: ...

    def getPathHighlighter(self) -> ghidra.graph.viewer.edge.VisualGraphPathHighlighter: ...

    def getPrimaryViewer(self) -> ghidra.graph.viewer.GraphViewer: ...

    def getRenderContext(self) -> edu.uci.ics.jung.visualization.RenderContext: ...

    def getSatelliteBounds(self) -> java.awt.Rectangle:
        """
        Returns an empty rectangle if the satellite is not visible
        @return the bounds
        """
        ...

    def getSatelliteViewer(self) -> ghidra.graph.viewer.SatelliteGraphViewer: ...

    def getVertexFocusPathHighlightMode(self) -> ghidra.graph.viewer.PathHighlightMode: ...

    def getVertexHoverPathHighlightMode(self) -> ghidra.graph.viewer.PathHighlightMode: ...

    def hashCode(self) -> int: ...

    def isGraphViewStale(self) -> bool: ...

    def isSatelliteComponent(self, c: java.awt.Component) -> bool: ...

    def isSatelliteDocked(self) -> bool: ...

    def isSatelliteShowing(self) -> bool: ...

    def isSatelliteUnDocked(self) -> bool: ...

    def isUninitialized(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def repaint(self) -> None: ...

    def setGraphOptions(self, options: ghidra.graph.viewer.options.VisualGraphOptions) -> None: ...

    def setGraphPerspective(self, info: ghidra.graph.viewer.GraphPerspectiveInfo) -> None: ...

    def setGraphViewStale(self, isStale: bool) -> None: ...

    def setPopupsVisible(self, visible: bool) -> None: ...

    def setSatelliteDocked(self, docked: bool) -> None: ...

    def setSatelliteVisible(self, visible: bool) -> None: ...

    def setStatusMessage(self, message: unicode) -> None:
        """
        Sets a message to be painted on the viewer.  This is useful to show a text message to the
         user.  Passing null will clear the message.
        @param message the message
        """
        ...

    def setVertexClickListener(self, l: ghidra.graph.viewer.vertex.VertexClickListener) -> None: ...

    def setVertexFocusListener(self, l: ghidra.graph.viewer.vertex.VertexFocusListener) -> None: ...

    def setVertexFocusPathHighlightMode(self, mode: ghidra.graph.viewer.PathHighlightMode) -> None: ...

    def setVertexFocused(self, __a0: ghidra.graph.viewer.VisualVertex) -> None: ...

    def setVertexHoverPathHighlightMode(self, mode: ghidra.graph.viewer.PathHighlightMode) -> None: ...

    def setVerticesSelected(self, vertices: java.util.Collection) -> None: ...

    def toString(self) -> unicode: ...

    def twinkleVertex(self, __a0: ghidra.graph.viewer.VisualVertex) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def component(self) -> javax.swing.JComponent: ...

    @property
    def graph(self) -> ghidra.graph.VisualGraph: ...

    @property
    def graphOptions(self) -> None: ...  # No getter available.

    @graphOptions.setter
    def graphOptions(self, value: ghidra.graph.viewer.options.VisualGraphOptions) -> None: ...

    @property
    def graphPerspective(self) -> None: ...  # No getter available.

    @graphPerspective.setter
    def graphPerspective(self, value: ghidra.graph.viewer.GraphPerspectiveInfo) -> None: ...

    @property
    def graphViewStale(self) -> bool: ...

    @graphViewStale.setter
    def graphViewStale(self, value: bool) -> None: ...

    @property
    def pathHighlighter(self) -> ghidra.graph.viewer.edge.VisualGraphPathHighlighter: ...

    @property
    def popupsVisible(self) -> None: ...  # No getter available.

    @popupsVisible.setter
    def popupsVisible(self, value: bool) -> None: ...

    @property
    def primaryViewer(self) -> ghidra.graph.viewer.GraphViewer: ...

    @property
    def renderContext(self) -> edu.uci.ics.jung.visualization.RenderContext: ...

    @property
    def satelliteBounds(self) -> java.awt.Rectangle: ...

    @property
    def satelliteDocked(self) -> bool: ...

    @satelliteDocked.setter
    def satelliteDocked(self, value: bool) -> None: ...

    @property
    def satelliteShowing(self) -> bool: ...

    @property
    def satelliteUnDocked(self) -> bool: ...

    @property
    def satelliteViewer(self) -> ghidra.graph.viewer.SatelliteGraphViewer: ...

    @property
    def satelliteVisible(self) -> None: ...  # No getter available.

    @satelliteVisible.setter
    def satelliteVisible(self, value: bool) -> None: ...

    @property
    def statusMessage(self) -> None: ...  # No getter available.

    @statusMessage.setter
    def statusMessage(self, value: unicode) -> None: ...

    @property
    def uninitialized(self) -> bool: ...

    @property
    def vertexClickListener(self) -> None: ...  # No getter available.

    @vertexClickListener.setter
    def vertexClickListener(self, value: ghidra.graph.viewer.vertex.VertexClickListener) -> None: ...

    @property
    def vertexFocusListener(self) -> None: ...  # No getter available.

    @vertexFocusListener.setter
    def vertexFocusListener(self, value: ghidra.graph.viewer.vertex.VertexFocusListener) -> None: ...

    @property
    def vertexFocusPathHighlightMode(self) -> ghidra.graph.viewer.PathHighlightMode: ...

    @vertexFocusPathHighlightMode.setter
    def vertexFocusPathHighlightMode(self, value: ghidra.graph.viewer.PathHighlightMode) -> None: ...

    @property
    def vertexFocused(self) -> None: ...  # No getter available.

    @vertexFocused.setter
    def vertexFocused(self, value: ghidra.graph.viewer.VisualVertex) -> None: ...

    @property
    def vertexHoverPathHighlightMode(self) -> ghidra.graph.viewer.PathHighlightMode: ...

    @vertexHoverPathHighlightMode.setter
    def vertexHoverPathHighlightMode(self, value: ghidra.graph.viewer.PathHighlightMode) -> None: ...

    @property
    def verticesSelected(self) -> None: ...  # No getter available.

    @verticesSelected.setter
    def verticesSelected(self, value: java.util.Collection) -> None: ...
