import edu.uci.ics.jung.visualization
import ghidra.app.plugin.core.functiongraph.graph.vertex
import ghidra.app.plugin.core.functiongraph.mvc
import ghidra.graph
import ghidra.graph.viewer
import ghidra.graph.viewer.edge
import ghidra.graph.viewer.options
import ghidra.graph.viewer.vertex
import ghidra.program.util
import java.awt
import java.lang
import java.util
import javax.swing


class FGComponent(ghidra.graph.viewer.GraphComponent):




    def __init__(self, __a0: ghidra.app.plugin.core.functiongraph.mvc.FGView, __a1: ghidra.app.plugin.core.functiongraph.mvc.FGData, __a2: ghidra.graph.viewer.layout.LayoutProvider): ...



    def clearAllUserLayoutSettings(self) -> None: ...

    def clearLayoutPositionCache(self) -> None: ...

    def dispose(self) -> None: ...

    def ensureCursorVisible(self, __a0: ghidra.app.plugin.core.functiongraph.graph.vertex.FGVertex) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getComponent(self) -> javax.swing.JComponent: ...

    def getFucntionGraphOptions(self) -> ghidra.app.plugin.core.functiongraph.mvc.FunctionGraphOptions: ...

    def getGraph(self) -> ghidra.graph.VisualGraph: ...

    def getPathHighlighter(self) -> ghidra.graph.viewer.edge.VisualGraphPathHighlighter: ...

    def getPrimaryViewer(self) -> ghidra.graph.viewer.GraphViewer: ...

    def getRenderContext(self) -> edu.uci.ics.jung.visualization.RenderContext: ...

    def getSatelliteBounds(self) -> java.awt.Rectangle: ...

    def getSatelliteViewer(self) -> ghidra.graph.viewer.SatelliteGraphViewer: ...

    def getVertexFocusPathHighlightMode(self) -> ghidra.graph.viewer.PathHighlightMode: ...

    def getVertexHoverPathHighlightMode(self) -> ghidra.graph.viewer.PathHighlightMode: ...

    def hashCode(self) -> int: ...

    def isGraphViewStale(self) -> bool: ...

    def isSatelliteComponent(self, __a0: java.awt.Component) -> bool: ...

    def isSatelliteDocked(self) -> bool: ...

    def isSatelliteShowing(self) -> bool: ...

    def isSatelliteUnDocked(self) -> bool: ...

    def isUninitialized(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def repaint(self) -> None: ...

    def restoreSettings(self) -> None: ...

    def setGraphOptions(self, __a0: ghidra.graph.viewer.options.VisualGraphOptions) -> None: ...

    def setGraphPerspective(self, __a0: ghidra.graph.viewer.GraphPerspectiveInfo) -> None: ...

    def setGraphViewStale(self, __a0: bool) -> None: ...

    def setPopupsVisible(self, __a0: bool) -> None: ...

    def setSatelliteDocked(self, __a0: bool) -> None: ...

    def setSatelliteVisible(self, __a0: bool) -> None: ...

    def setStatusMessage(self, __a0: unicode) -> None: ...

    def setVertexClickListener(self, __a0: ghidra.graph.viewer.vertex.VertexClickListener) -> None: ...

    def setVertexFocusListener(self, __a0: ghidra.graph.viewer.vertex.VertexFocusListener) -> None: ...

    def setVertexFocusPathHighlightMode(self, __a0: ghidra.graph.viewer.PathHighlightMode) -> None: ...

    @overload
    def setVertexFocused(self, __a0: ghidra.graph.viewer.VisualVertex) -> None: ...

    @overload
    def setVertexFocused(self, __a0: ghidra.app.plugin.core.functiongraph.graph.vertex.FGVertex, __a1: ghidra.program.util.ProgramLocation) -> None: ...

    def setVertexHoverPathHighlightMode(self, __a0: ghidra.graph.viewer.PathHighlightMode) -> None: ...

    def setVerticesSelected(self, __a0: java.util.Collection) -> None: ...

    def toString(self) -> unicode: ...

    def twinkleVertex(self, __a0: ghidra.graph.viewer.VisualVertex) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def fucntionGraphOptions(self) -> ghidra.app.plugin.core.functiongraph.mvc.FunctionGraphOptions: ...
