import ghidra.graph
import ghidra.graph.event
import ghidra.graph.viewer
import ghidra.graph.viewer.layout
import java.awt
import java.lang
import java.util


class VisualGraph(ghidra.graph.GDirectedGraph, object):
    """
    The primary interface for graphs that are to be rendered.  This class defines methods
     commonly used in the GUI while extending the primary non-visual graph interface.

     The Visual Graph API will typically provide services for taking a Visual Graph and
     creating a UI that handles basic user interaction elements (similar to how complex Java
     widgets handle user interaction for the developer).  The Visual Graph is the model of the
     UI components.  A typical Visual Graph UI will render developer-defined components,
     handling mouse event translations for the developer.

     Some features found in Visual Graphs:

     	Mouse event translation - the JComponent being rendered in the graph will be handed
          mouse events that are relative to its coordinate space, not that of the graph.

      Hover and Selection - vertex hover and selection events are handled by the API

      Zooming - zoom level and related events (when zoomed too far, mouse events are
          not passed-through to the component) and handled by the API


    """









    def addEdge(self, __a0: ghidra.graph.GEdge) -> None: ...

    def addGraphChangeListener(self, l: ghidra.graph.event.VisualGraphChangeListener) -> None:
        """
        Adds the given listener to this graph
        @param l the listener
        """
        ...

    def addVertex(self, __a0: object) -> bool: ...

    def clearSelectedVertices(self) -> None:
        """
        Clears any selected vertices as well as the focused vertex
        """
        ...

    @overload
    def containsEdge(self, __a0: ghidra.graph.GEdge) -> bool: ...

    @overload
    def containsEdge(self, __a0: object, __a1: object) -> bool: ...

    def containsVertex(self, __a0: object) -> bool: ...

    def copy(self) -> ghidra.graph.VisualGraph: ...

    def emptyCopy(self) -> ghidra.graph.GDirectedGraph: ...

    def equals(self, __a0: object) -> bool: ...

    def findEdge(self, __a0: object, __a1: object) -> ghidra.graph.GEdge: ...

    def getClass(self) -> java.lang.Class: ...

    def getEdgeCount(self) -> int: ...

    def getEdges(self) -> java.util.Collection: ...

    def getFocusedVertex(self) -> V:
        """
        Returns the focused vertex; null if no vertex has focus.  Focus is equivalent to
         being selected, but further distinguishes the vertex as being the only selected
         vertex.  This is useful for key event processing.
        @return the focused vertex
        """
        ...

    def getInEdges(self, __a0: object) -> java.util.Collection: ...

    def getIncidentEdges(self, __a0: object) -> java.util.Collection: ...

    def getLayout(self) -> ghidra.graph.viewer.layout.VisualGraphLayout:
        """
        Returns the layout that has been applied to the graph.  The graph does not need its
         layout to function, but rather it is convenient for the visual graph system to be able
         to get the layout from the graph, rather than passing the layout everywhere it is
         needed.
        @return the layout applied to the graph
        """
        ...

    def getOutEdges(self, __a0: object) -> java.util.Collection: ...

    def getPredecessors(self, __a0: object) -> java.util.Collection: ...

    def getSelectedVertices(self) -> java.util.Set:
        """
        Returns the selected vertices.
        @return the selected vertices
        """
        ...

    def getSuccessors(self, __a0: object) -> java.util.Collection: ...

    def getVertexCount(self) -> int: ...

    def getVertices(self) -> java.util.Collection: ...

    def hashCode(self) -> int: ...

    def isEmpty(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeEdge(self, __a0: ghidra.graph.GEdge) -> bool: ...

    def removeEdges(self, __a0: java.lang.Iterable) -> None: ...

    def removeGraphChangeListener(self, l: ghidra.graph.event.VisualGraphChangeListener) -> None:
        """
        Removes the given listener from this graph
        @param l the listener
        """
        ...

    def removeVertex(self, __a0: object) -> bool: ...

    def removeVertices(self, __a0: java.lang.Iterable) -> None: ...

    def setSelectedVertices(self, vertices: java.util.Set) -> None:
        """
        Selects the given vertices

         <P>Note: this method is called by other APIs to ensure that the graph's notion of the
         focused vertex matches what is happening externally (e.g., from the user clicking the
         screen).  If you wish to programmatically select a vertex, then you should not be calling
         this API directly, but you should instead be using the {@link GPickedState} or one
         of the APIs that uses that, such as the {@link GraphComponent}.
        @param vertices the vertices
        """
        ...

    def setVertexFocused(self, __a0: ghidra.graph.viewer.VisualVertex, __a1: bool) -> None: ...

    def toString(self) -> unicode: ...

    def vertexLocationChanged(self, __a0: ghidra.graph.viewer.VisualVertex, __a1: java.awt.Point, __a2: ghidra.graph.viewer.layout.LayoutListener.ChangeType) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def edgeCount(self) -> int: ...

    @property
    def edges(self) -> java.util.Collection: ...

    @property
    def empty(self) -> bool: ...

    @property
    def focusedVertex(self) -> ghidra.graph.viewer.VisualVertex: ...

    @property
    def layout(self) -> ghidra.graph.viewer.layout.VisualGraphLayout: ...

    @property
    def selectedVertices(self) -> java.util.Set: ...

    @selectedVertices.setter
    def selectedVertices(self, value: java.util.Set) -> None: ...

    @property
    def vertexCount(self) -> int: ...

    @property
    def vertices(self) -> java.util.Collection: ...
