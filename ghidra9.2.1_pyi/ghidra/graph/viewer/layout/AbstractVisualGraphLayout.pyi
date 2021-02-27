import com.google.common.base
import edu.uci.ics.jung.algorithms.layout
import edu.uci.ics.jung.graph
import edu.uci.ics.jung.visualization.renderers
import edu.uci.ics.jung.visualization.renderers.Renderer
import ghidra.graph
import ghidra.graph.viewer
import ghidra.graph.viewer.layout
import ghidra.util.task
import java.awt
import java.awt.geom
import java.lang


class AbstractVisualGraphLayout(edu.uci.ics.jung.algorithms.layout.AbstractLayout, ghidra.graph.viewer.layout.VisualGraphLayout):
    """
    A base layout that marries the Visual Graph and Jung layout interfaces.   This class allows
     you to create new layouts while stubbing the Jung layout methods.

     This class essentially takes in client-produced grid row and column indices and
     produces layout locations for those values.

     This an implementation the Jung Layout interface that handles most of the
     layout implementation for you.  Things to know:

     	You should call initialize() inside of your constructor
      You must implement #performInitialGridLayout(VisualGraph) - this is where
          you align your vertices (and optionally edge articulations) on a grid.  This grid
          will be translated into layout space points for you.
      If you wish to use articulation points in your edges, you must override
          #usesEdgeArticulations() to return true.


     By default, this class will create x-position values that
     are aligned with the column's x-position.   You can override
     #getVertexLocation(VisualVertex, Column, Row, Rectangle) in order to center the
     vertex within its column
     #getCenteredVertexLocation(VisualVertex, Column, Row, Rectangle).  Also note though
     that if your layout returns true for #isCondensedLayout(),
     then the centering will be condensed and slightly off.
    """









    def addLayoutListener(self, listener: ghidra.graph.viewer.layout.LayoutListener) -> None: ...

    def apply(self, __a0: object) -> java.awt.geom.Point2D: ...

    def calculateLocations(self, visualGraph: ghidra.graph.VisualGraph, taskMonitor: ghidra.util.task.TaskMonitor) -> ghidra.graph.viewer.layout.LayoutPositions: ...

    def cloneLayout(self, newGraph: ghidra.graph.VisualGraph) -> ghidra.graph.viewer.layout.VisualGraphLayout: ...

    def createClonedLayout(self, newGraph: ghidra.graph.VisualGraph) -> ghidra.graph.viewer.layout.AbstractVisualGraphLayout:
        """
        This class has implemented {@link #cloneLayout(VisualGraph)} in order to properly
         initialize location information in the layout so that subclasses do not have to.  Each
         subclass still needs to create the new instance of the layout that is being cloned, as
         this class does not know how to do so.
        @param newGraph the new graph for the new layout
        @return the new layout
        """
        ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getEdgeLabelRenderer(self) -> edu.uci.ics.jung.visualization.renderers.Renderer.EdgeLabel: ...

    def getEdgeRenderer(self) -> edu.uci.ics.jung.visualization.renderers.BasicEdgeRenderer: ...

    def getEdgeShapeTransformer(self) -> com.google.common.base.Function: ...

    def getGraph(self) -> edu.uci.ics.jung.graph.Graph: ...

    def getLayoutName(self) -> unicode:
        """
        Returns the name of this layout
        @return the name of this layout
        """
        ...

    def getSize(self) -> java.awt.Dimension: ...

    def getVisualGraph(self) -> ghidra.graph.VisualGraph: ...

    def getX(self, __a0: object) -> float: ...

    def getY(self, __a0: object) -> float: ...

    def hashCode(self) -> int: ...

    def initialize(self) -> None: ...

    def isLocked(self, __a0: object) -> bool: ...

    @overload
    def lock(self, __a0: bool) -> None: ...

    @overload
    def lock(self, __a0: object, __a1: bool) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeLayoutListener(self, listener: ghidra.graph.viewer.layout.LayoutListener) -> None: ...

    def reset(self) -> None: ...

    def setGraph(self, __a0: edu.uci.ics.jung.graph.Graph) -> None: ...

    def setInitializer(self, __a0: com.google.common.base.Function) -> None: ...

    @overload
    def setLocation(self, __a0: ghidra.graph.viewer.VisualVertex, __a1: java.awt.geom.Point2D) -> None: ...

    @overload
    def setLocation(self, __a0: object, __a1: java.awt.geom.Point2D) -> None: ...

    @overload
    def setLocation(self, __a0: object, __a1: float, __a2: float) -> None: ...

    @overload
    def setLocation(self, __a0: ghidra.graph.viewer.VisualVertex, __a1: java.awt.geom.Point2D, __a2: ghidra.graph.viewer.layout.LayoutListener.ChangeType) -> None: ...

    def setSize(self, __a0: java.awt.Dimension) -> None: ...

    def setTaskMonitor(self, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def toString(self) -> unicode: ...

    def usesEdgeArticulations(self) -> bool: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def edgeLabelRenderer(self) -> edu.uci.ics.jung.visualization.renderers.Renderer.EdgeLabel: ...

    @property
    def edgeRenderer(self) -> edu.uci.ics.jung.visualization.renderers.BasicEdgeRenderer: ...

    @property
    def edgeShapeTransformer(self) -> com.google.common.base.Function: ...

    @property
    def layoutName(self) -> unicode: ...

    @property
    def taskMonitor(self) -> None: ...  # No getter available.

    @taskMonitor.setter
    def taskMonitor(self, value: ghidra.util.task.TaskMonitor) -> None: ...
