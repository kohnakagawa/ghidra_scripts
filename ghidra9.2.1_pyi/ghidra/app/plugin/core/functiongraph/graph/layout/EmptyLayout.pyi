import com.google.common.base
import edu.uci.ics.jung.graph
import edu.uci.ics.jung.visualization.renderers
import ghidra.app.plugin.core.functiongraph.graph.layout
import ghidra.app.plugin.core.functiongraph.graph.vertex
import ghidra.graph
import ghidra.graph.viewer
import ghidra.graph.viewer.layout
import ghidra.util.task
import java.awt
import java.awt.geom
import java.lang


class EmptyLayout(ghidra.graph.viewer.layout.AbstractVisualGraphLayout, ghidra.app.plugin.core.functiongraph.graph.layout.FGLayout):




    def __init__(self, __a0: ghidra.app.plugin.core.functiongraph.graph.FunctionGraph): ...



    def addLayoutListener(self, __a0: ghidra.graph.viewer.layout.LayoutListener) -> None: ...

    def apply(self, __a0: object) -> java.awt.geom.Point2D: ...

    def calculateLocations(self, __a0: ghidra.graph.VisualGraph, __a1: ghidra.util.task.TaskMonitor) -> ghidra.graph.viewer.layout.LayoutPositions: ...

    def cloneLayout(self, __a0: ghidra.graph.VisualGraph) -> ghidra.graph.viewer.layout.VisualGraphLayout: ...

    def createClonedLayout(self, __a0: ghidra.graph.VisualGraph) -> ghidra.graph.viewer.layout.AbstractVisualGraphLayout: ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getEdgeLabelRenderer(self) -> edu.uci.ics.jung.visualization.renderers.Renderer.EdgeLabel: ...

    def getEdgeRenderer(self) -> edu.uci.ics.jung.visualization.renderers.BasicEdgeRenderer: ...

    def getEdgeShapeTransformer(self) -> com.google.common.base.Function: ...

    def getGraph(self) -> edu.uci.ics.jung.graph.Graph: ...

    def getLayoutName(self) -> unicode: ...

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

    def removeLayoutListener(self, __a0: ghidra.graph.viewer.layout.LayoutListener) -> None: ...

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
    def setLocation(self, __a0: ghidra.app.plugin.core.functiongraph.graph.vertex.FGVertex, __a1: java.awt.geom.Point2D, __a2: ghidra.graph.viewer.layout.LayoutListener.ChangeType) -> None: ...

    @overload
    def setLocation(self, __a0: ghidra.graph.viewer.VisualVertex, __a1: java.awt.geom.Point2D, __a2: ghidra.graph.viewer.layout.LayoutListener.ChangeType) -> None: ...

    def setSize(self, __a0: java.awt.Dimension) -> None: ...

    def setTaskMonitor(self, __a0: ghidra.util.task.TaskMonitor) -> None: ...

    def toString(self) -> unicode: ...

    def usesEdgeArticulations(self) -> bool: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def edgeRenderer(self) -> edu.uci.ics.jung.visualization.renderers.BasicEdgeRenderer: ...

    @property
    def edgeShapeTransformer(self) -> com.google.common.base.Function: ...

    @property
    def visualGraph(self) -> ghidra.app.plugin.core.functiongraph.graph.FunctionGraph: ...
