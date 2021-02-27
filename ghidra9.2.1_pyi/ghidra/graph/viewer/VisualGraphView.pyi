import ghidra.graph
import ghidra.graph.viewer
import ghidra.graph.viewer.event.mouse
import ghidra.graph.viewer.layout
import ghidra.graph.viewer.vertex
import java.awt
import java.awt.event
import java.lang
import java.util
import javax.swing


class VisualGraphView(object):
    """
    A view object, where 'view' is used in the sense of the Model-View-Controller (MVC) pattern.
     This class will contain all UI widgets need to display and interact with a graph.

     Implementation Note:

     	The graph of this component can be null, changing to non-null values over the
     lifetime of this view.  This allows this view to be installed in a UI component, with the
     contents changing as needed.


     	When the graph is #setGraph(VisualGraph), the view portion of the class is
     	recreated.


      At any given point in time there may not be a #graphComponent.  This means that
      this class must maintain settings state that it will apply when the component is created.
      This state is atypical and makes this class a bit harder to understand.


    """





    def __init__(self): ...



    def arePopupsEnabled(self) -> bool: ...

    def cleanup(self) -> None:
        """
        Effectively clears this display.  This method is not called dispose, as that implies
         the end of an object's lifecycle.  This object can be re-used after this method is
         called.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def generateGraphPerspective(self) -> ghidra.graph.viewer.GraphPerspectiveInfo: ...

    def getClass(self) -> java.lang.Class: ...

    def getFocusedVertex(self) -> V: ...

    def getGraphComponent(self) -> ghidra.graph.viewer.GraphComponent: ...

    def getLayoutProvider(self) -> ghidra.graph.viewer.layout.LayoutProvider: ...

    def getPrimaryGraphViewer(self) -> ghidra.graph.viewer.GraphViewer:
        """
        Returns the primary viewer of the graph (as opposed to the satellite viewer).   The
         viewer returned is responsible for maintaining view information for a given graph.
        @return the primary viewer
        """
        ...

    def getSatelliteViewer(self) -> ghidra.graph.viewer.SatelliteGraphViewer: ...

    def getSelectedVertices(self) -> java.util.Set: ...

    def getUndockedSatelliteComponent(self) -> javax.swing.JComponent: ...

    def getVertexFocusPathHighlightMode(self) -> ghidra.graph.viewer.PathHighlightMode: ...

    def getVertexHoverPathHighlightMode(self) -> ghidra.graph.viewer.PathHighlightMode: ...

    def getVertexPointInViewSpace(self, __a0: ghidra.graph.viewer.VisualVertex) -> java.awt.Point: ...

    def getViewComponent(self) -> javax.swing.JComponent: ...

    def getViewUpdater(self) -> ghidra.graph.viewer.VisualGraphViewUpdater: ...

    def getVisualGraph(self) -> G: ...

    def hashCode(self) -> int: ...

    def isSatelliteComponent(self, c: java.awt.Component) -> bool: ...

    def isSatelliteDocked(self) -> bool:
        """
        Returns whether the satellite intended to be docked.  If this component is built, then
         a result of true means that the satellite is docked.  If the component is not yet
         built, then a result of true means that the satellite will be made docked when the
         component is built.
        @return true if visible
        """
        ...

    def isSatelliteVisible(self) -> bool:
        """
        Returns whether the satellite intended to be visible.  If this component is built, then
         a result of true means that the satellite is showing.  If the component is not yet
         built, then a result of true means that the satellite will be made visible when the
         component is built.
        @return true if visible
        """
        ...

    def isScaledPastInteractionThreshold(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def repaint(self) -> None: ...

    def requestFocus(self) -> None: ...

    def setGraph(self, __a0: ghidra.graph.VisualGraph) -> None: ...

    def setGraphPerspective(self, newPerspective: ghidra.graph.viewer.GraphPerspectiveInfo) -> None:
        """
        Sets the perspective for this view
        @param newPerspective the new perspective
        """
        ...

    def setLayoutProvider(self, newLayoutProvider: ghidra.graph.viewer.layout.LayoutProvider) -> None:
        """
        Sets the given layout provider, <b>but does not actually perform a layout</b>.
        @param newLayoutProvider the new provider
        """
        ...

    def setPopupsVisible(self, visible: bool) -> None: ...

    def setSatelliteDocked(self, docked: bool) -> None: ...

    def setSatelliteListener(self, l: ghidra.graph.viewer.GraphSatelliteListener) -> None: ...

    def setSatelliteVisible(self, visible: bool) -> None: ...

    def setStatusMessage(self, message: unicode) -> None:
        """
        Sets a message to be painted on the viewer.  This is useful to show a text message to the
         user.  Passing null will clear the message.
        @param message the status message
        """
        ...

    def setTooltipProvider(self, provider: ghidra.graph.viewer.event.mouse.VertexTooltipProvider) -> None: ...

    def setVertexClickListener(self, l: ghidra.graph.viewer.vertex.VertexClickListener) -> None:
        """
        Sets a listener that allows clients to be notified of vertex double-clicks.  Normal
         mouse processing is handled by the {@link VisualGraphMousePlugin} class.  This is a
         convenience method so that clients do not have to deal with the mouse plugin.
        @param l the listener
        """
        ...

    def setVertexFocusListener(self, l: ghidra.graph.viewer.vertex.VertexFocusListener) -> None: ...

    def setVertexFocusPathHighlightMode(self, mode: ghidra.graph.viewer.PathHighlightMode) -> None: ...

    def setVertexHoverPathHighlightMode(self, mode: ghidra.graph.viewer.PathHighlightMode) -> None: ...

    def showErrorView(self, errorMessage: unicode) -> None: ...

    def toString(self) -> unicode: ...

    def translateMouseEventFromVertexToViewSpace(self, __a0: ghidra.graph.viewer.VisualVertex, __a1: java.awt.event.MouseEvent) -> java.awt.event.MouseEvent: ...

    def translatePointFromVertexToViewSpace(self, __a0: ghidra.graph.viewer.VisualVertex, __a1: java.awt.Point) -> java.awt.Point: ...

    def translateRectangleFromVertexToViewSpace(self, __a0: ghidra.graph.viewer.VisualVertex, __a1: java.awt.Rectangle) -> java.awt.Rectangle: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def zoomInGraph(self) -> None: ...

    def zoomOutGraph(self) -> None: ...

    def zoomToVertex(self, __a0: ghidra.graph.viewer.VisualVertex) -> None: ...

    def zoomToWindow(self) -> None: ...

    @property
    def focusedVertex(self) -> ghidra.graph.viewer.VisualVertex: ...

    @property
    def graph(self) -> None: ...  # No getter available.

    @graph.setter
    def graph(self, value: ghidra.graph.VisualGraph) -> None: ...

    @property
    def graphComponent(self) -> ghidra.graph.viewer.GraphComponent: ...

    @property
    def graphPerspective(self) -> None: ...  # No getter available.

    @graphPerspective.setter
    def graphPerspective(self, value: ghidra.graph.viewer.GraphPerspectiveInfo) -> None: ...

    @property
    def layoutProvider(self) -> ghidra.graph.viewer.layout.LayoutProvider: ...

    @layoutProvider.setter
    def layoutProvider(self, value: ghidra.graph.viewer.layout.LayoutProvider) -> None: ...

    @property
    def popupsVisible(self) -> None: ...  # No getter available.

    @popupsVisible.setter
    def popupsVisible(self, value: bool) -> None: ...

    @property
    def primaryGraphViewer(self) -> ghidra.graph.viewer.GraphViewer: ...

    @property
    def satelliteDocked(self) -> bool: ...

    @satelliteDocked.setter
    def satelliteDocked(self, value: bool) -> None: ...

    @property
    def satelliteListener(self) -> None: ...  # No getter available.

    @satelliteListener.setter
    def satelliteListener(self, value: ghidra.graph.viewer.GraphSatelliteListener) -> None: ...

    @property
    def satelliteViewer(self) -> ghidra.graph.viewer.SatelliteGraphViewer: ...

    @property
    def satelliteVisible(self) -> bool: ...

    @satelliteVisible.setter
    def satelliteVisible(self, value: bool) -> None: ...

    @property
    def scaledPastInteractionThreshold(self) -> bool: ...

    @property
    def selectedVertices(self) -> java.util.Set: ...

    @property
    def statusMessage(self) -> None: ...  # No getter available.

    @statusMessage.setter
    def statusMessage(self, value: unicode) -> None: ...

    @property
    def tooltipProvider(self) -> None: ...  # No getter available.

    @tooltipProvider.setter
    def tooltipProvider(self, value: ghidra.graph.viewer.event.mouse.VertexTooltipProvider) -> None: ...

    @property
    def undockedSatelliteComponent(self) -> javax.swing.JComponent: ...

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
    def vertexHoverPathHighlightMode(self) -> ghidra.graph.viewer.PathHighlightMode: ...

    @vertexHoverPathHighlightMode.setter
    def vertexHoverPathHighlightMode(self, value: ghidra.graph.viewer.PathHighlightMode) -> None: ...

    @property
    def viewComponent(self) -> javax.swing.JComponent: ...

    @property
    def viewUpdater(self) -> ghidra.graph.viewer.VisualGraphViewUpdater: ...

    @property
    def visualGraph(self) -> ghidra.graph.VisualGraph: ...
