import com.google.common.base
import edu.uci.ics.jung.graph.util
import ghidra.app.plugin.core.functiongraph.graph.layout
import ghidra.app.plugin.core.functiongraph.graph.vertex
import ghidra.app.plugin.core.functiongraph.mvc
import ghidra.graph
import ghidra.graph.event
import ghidra.graph.graphs
import ghidra.graph.viewer
import ghidra.graph.viewer.layout
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.util
import java.awt
import java.lang
import java.util
import org.jdom


class FunctionGraph(ghidra.graph.graphs.GroupingVisualGraph):








    @overload
    def addEdge(self, __a0: ghidra.graph.GEdge) -> None: ...

    @overload
    def addEdge(self, __a0: object, __a1: edu.uci.ics.jung.graph.util.Pair) -> bool: ...

    @overload
    def addEdge(self, __a0: object, __a1: java.util.Collection) -> bool: ...

    @overload
    def addEdge(self, __a0: ghidra.graph.viewer.VisualEdge, __a1: edu.uci.ics.jung.graph.util.Pair, __a2: edu.uci.ics.jung.graph.util.EdgeType) -> bool: ...

    @overload
    def addEdge(self, __a0: object, __a1: edu.uci.ics.jung.graph.util.Pair, __a2: edu.uci.ics.jung.graph.util.EdgeType) -> bool: ...

    @overload
    def addEdge(self, __a0: object, __a1: java.util.Collection, __a2: edu.uci.ics.jung.graph.util.EdgeType) -> bool: ...

    @overload
    def addEdge(self, __a0: object, __a1: object, __a2: object) -> bool: ...

    @overload
    def addEdge(self, __a0: object, __a1: object, __a2: object, __a3: edu.uci.ics.jung.graph.util.EdgeType) -> bool: ...

    def addGraphChangeListener(self, __a0: ghidra.graph.event.VisualGraphChangeListener) -> None: ...

    @overload
    def addVertex(self, __a0: ghidra.graph.viewer.VisualVertex) -> bool: ...

    @overload
    def addVertex(self, __a0: object) -> bool: ...

    def clearAllUserLayoutSettings(self) -> None: ...

    def clearSavedVertexLocations(self) -> None: ...

    def clearSelectedVertices(self) -> None: ...

    def clearVertexColor(self, __a0: ghidra.app.plugin.core.functiongraph.graph.vertex.FGVertex) -> None: ...

    @overload
    def containsEdge(self, __a0: ghidra.graph.GEdge) -> bool: ...

    @overload
    def containsEdge(self, __a0: object) -> bool: ...

    @overload
    def containsEdge(self, __a0: object, __a1: object) -> bool: ...

    def containsVertex(self, __a0: object) -> bool: ...

    def copy(self) -> ghidra.graph.GDirectedGraph: ...

    def createDummySinks(self) -> java.util.Set: ...

    def createDummySources(self) -> java.util.Set: ...

    def degree(self, __a0: object) -> int: ...

    def dispose(self) -> None: ...

    def emptyCopy(self) -> ghidra.graph.GDirectedGraph: ...

    def equals(self, __a0: object) -> bool: ...

    def findEdge(self, __a0: object, __a1: object) -> object: ...

    def findEdgeSet(self, __a0: object, __a1: object) -> java.util.Collection: ...

    @overload
    def findMatchingVertex(self, __a0: ghidra.app.plugin.core.functiongraph.graph.vertex.FGVertex) -> ghidra.app.plugin.core.functiongraph.graph.vertex.FGVertex: ...

    @overload
    def findMatchingVertex(self, __a0: ghidra.graph.viewer.VisualVertex) -> ghidra.graph.viewer.VisualVertex: ...

    @overload
    def findMatchingVertex(self, __a0: ghidra.app.plugin.core.functiongraph.graph.vertex.FGVertex, __a1: java.util.Collection) -> ghidra.app.plugin.core.functiongraph.graph.vertex.FGVertex: ...

    @overload
    def findMatchingVertex(self, __a0: ghidra.graph.viewer.VisualVertex, __a1: java.util.Collection) -> ghidra.graph.viewer.VisualVertex: ...

    def getAllEdges(self, __a0: ghidra.graph.viewer.VisualVertex) -> java.lang.Iterable: ...

    def getClass(self) -> java.lang.Class: ...

    def getDefaultEdgeType(self) -> edu.uci.ics.jung.graph.util.EdgeType: ...

    def getDest(self, __a0: object) -> object: ...

    @overload
    def getEdgeCount(self) -> int: ...

    @overload
    def getEdgeCount(self, __a0: edu.uci.ics.jung.graph.util.EdgeType) -> int: ...

    def getEdgeType(self, __a0: object) -> edu.uci.ics.jung.graph.util.EdgeType: ...

    @overload
    def getEdges(self) -> java.util.Collection: ...

    @overload
    def getEdges(self, __a0: edu.uci.ics.jung.graph.util.EdgeType) -> java.util.Collection: ...

    @overload
    def getEdges(self, __a0: ghidra.graph.viewer.VisualVertex, __a1: ghidra.graph.viewer.VisualVertex) -> java.lang.Iterable: ...

    def getEndpoints(self, __a0: object) -> edu.uci.ics.jung.graph.util.Pair: ...

    def getEntryPoints(self) -> java.util.Set: ...

    def getExitPoints(self) -> java.util.Set: ...

    @staticmethod
    def getFactory() -> com.google.common.base.Supplier: ...

    def getFocusedVertex(self) -> ghidra.graph.viewer.VisualVertex: ...

    def getFunction(self) -> ghidra.program.model.listing.Function: ...

    @overload
    def getGroupHistory(self) -> java.util.Collection: ...

    @overload
    def getGroupHistory(self, __a0: ghidra.app.plugin.core.functiongraph.graph.vertex.FGVertex) -> ghidra.app.plugin.core.functiongraph.graph.vertex.GroupHistoryInfo: ...

    def getInEdges(self, __a0: object) -> java.util.Collection: ...

    def getIncidentCount(self, __a0: object) -> int: ...

    def getIncidentEdges(self, __a0: object) -> java.util.Collection: ...

    def getIncidentVertices(self, __a0: object) -> java.util.Collection: ...

    def getLayout(self) -> ghidra.graph.viewer.layout.VisualGraphLayout: ...

    def getNeighborCount(self, __a0: object) -> int: ...

    def getNeighbors(self, __a0: object) -> java.util.Collection: ...

    def getOpposite(self, __a0: object, __a1: object) -> object: ...

    def getOptions(self) -> ghidra.app.plugin.core.functiongraph.mvc.FunctionGraphOptions: ...

    def getOutEdges(self, __a0: object) -> java.util.Collection: ...

    def getPredecessorCount(self, __a0: object) -> int: ...

    def getPredecessors(self, __a0: object) -> java.util.Collection: ...

    def getProgramSelectionForAllVertices(self) -> ghidra.program.util.ProgramSelection: ...

    def getRootVertex(self) -> ghidra.app.plugin.core.functiongraph.graph.vertex.FGVertex: ...

    def getSavedGroupHistory(self) -> org.jdom.Element: ...

    def getSavedGroupedVertexSettings(self) -> org.jdom.Element: ...

    def getSavedVertexLocations(self) -> java.util.Map: ...

    def getSelectedVertices(self) -> java.util.Set: ...

    def getSettings(self) -> ghidra.app.plugin.core.functiongraph.mvc.FunctionGraphVertexAttributes: ...

    def getSource(self, __a0: object) -> object: ...

    def getSuccessorCount(self, __a0: object) -> int: ...

    def getSuccessors(self, __a0: object) -> java.util.Collection: ...

    def getUngroupedEdges(self) -> java.util.Set: ...

    def getUngroupedVertices(self) -> java.util.Set: ...

    def getVertexCount(self) -> int: ...

    @overload
    def getVertexForAddress(self, __a0: ghidra.program.model.address.Address) -> ghidra.app.plugin.core.functiongraph.graph.vertex.FGVertex: ...

    @overload
    def getVertexForAddress(self, __a0: ghidra.program.model.address.Address, __a1: java.util.Collection) -> ghidra.app.plugin.core.functiongraph.graph.vertex.FGVertex: ...

    def getVertices(self) -> java.util.Collection: ...

    def groupAdded(self, __a0: ghidra.app.plugin.core.functiongraph.graph.vertex.GroupedFunctionGraphVertex) -> None: ...

    def groupRemoved(self, __a0: ghidra.app.plugin.core.functiongraph.graph.vertex.GroupedFunctionGraphVertex) -> None: ...

    def groupRestored(self, __a0: ghidra.app.plugin.core.functiongraph.graph.vertex.GroupedFunctionGraphVertex) -> None: ...

    def hashCode(self) -> int: ...

    def inDegree(self, __a0: object) -> int: ...

    def isDest(self, __a0: object, __a1: object) -> bool: ...

    def isEmpty(self) -> bool: ...

    def isIncident(self, __a0: object, __a1: object) -> bool: ...

    def isNeighbor(self, __a0: object, __a1: object) -> bool: ...

    def isPredecessor(self, __a0: object, __a1: object) -> bool: ...

    def isSource(self, __a0: object, __a1: object) -> bool: ...

    def isSuccessor(self, __a0: object, __a1: object) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def outDegree(self, __a0: object) -> int: ...

    @overload
    def removeEdge(self, __a0: ghidra.graph.viewer.VisualEdge) -> bool: ...

    @overload
    def removeEdge(self, __a0: ghidra.graph.GEdge) -> bool: ...

    @overload
    def removeEdge(self, __a0: object) -> bool: ...

    def removeEdges(self, __a0: java.lang.Iterable) -> None: ...

    def removeFromGroupHistory(self, __a0: ghidra.app.plugin.core.functiongraph.graph.vertex.FGVertex) -> None: ...

    def removeGraphChangeListener(self, __a0: ghidra.graph.event.VisualGraphChangeListener) -> None: ...

    @overload
    def removeVertex(self, __a0: ghidra.graph.viewer.VisualVertex) -> bool: ...

    @overload
    def removeVertex(self, __a0: object) -> bool: ...

    def removeVertices(self, __a0: java.lang.Iterable) -> None: ...

    def restoreSettings(self) -> None: ...

    def saveSettings(self) -> None: ...

    def setGraphLayout(self, __a0: ghidra.app.plugin.core.functiongraph.graph.layout.FGLayout) -> None: ...

    def setGroupHistory(self, __a0: java.util.Collection) -> None: ...

    def setOptions(self, __a0: ghidra.app.plugin.core.functiongraph.mvc.FunctionGraphOptions) -> None: ...

    def setProgramHighlight(self, __a0: ghidra.program.util.ProgramSelection) -> None: ...

    def setProgramSelection(self, __a0: ghidra.program.util.ProgramSelection) -> None: ...

    def setRootVertex(self, __a0: ghidra.app.plugin.core.functiongraph.graph.vertex.FGVertex) -> None: ...

    def setSelectedVertices(self, __a0: java.util.Set) -> None: ...

    def setVertexFocused(self, __a0: ghidra.graph.viewer.VisualVertex, __a1: bool) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def vertexLocationChanged(self, __a0: ghidra.app.plugin.core.functiongraph.graph.vertex.FGVertex, __a1: java.awt.Point, __a2: ghidra.graph.viewer.layout.LayoutListener.ChangeType) -> None: ...

    @overload
    def vertexLocationChanged(self, __a0: ghidra.graph.viewer.VisualVertex, __a1: java.awt.Point, __a2: ghidra.graph.viewer.layout.LayoutListener.ChangeType) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def entryPoints(self) -> java.util.Set: ...

    @property
    def exitPoints(self) -> java.util.Set: ...

    @property
    def function(self) -> ghidra.program.model.listing.Function: ...

    @property
    def graphLayout(self) -> None: ...  # No getter available.

    @graphLayout.setter
    def graphLayout(self, value: ghidra.app.plugin.core.functiongraph.graph.layout.FGLayout) -> None: ...

    @property
    def groupHistory(self) -> java.util.Collection: ...

    @groupHistory.setter
    def groupHistory(self, value: java.util.Collection) -> None: ...

    @property
    def layout(self) -> ghidra.app.plugin.core.functiongraph.graph.layout.FGLayout: ...

    @property
    def options(self) -> ghidra.app.plugin.core.functiongraph.mvc.FunctionGraphOptions: ...

    @options.setter
    def options(self, value: ghidra.app.plugin.core.functiongraph.mvc.FunctionGraphOptions) -> None: ...

    @property
    def programHighlight(self) -> None: ...  # No getter available.

    @programHighlight.setter
    def programHighlight(self, value: ghidra.program.util.ProgramSelection) -> None: ...

    @property
    def programSelection(self) -> None: ...  # No getter available.

    @programSelection.setter
    def programSelection(self, value: ghidra.program.util.ProgramSelection) -> None: ...

    @property
    def programSelectionForAllVertices(self) -> ghidra.program.util.ProgramSelection: ...

    @property
    def rootVertex(self) -> ghidra.app.plugin.core.functiongraph.graph.vertex.FGVertex: ...

    @rootVertex.setter
    def rootVertex(self, value: ghidra.app.plugin.core.functiongraph.graph.vertex.FGVertex) -> None: ...

    @property
    def savedGroupHistory(self) -> org.jdom.Element: ...

    @property
    def savedGroupedVertexSettings(self) -> org.jdom.Element: ...

    @property
    def savedVertexLocations(self) -> java.util.Map: ...

    @property
    def settings(self) -> ghidra.app.plugin.core.functiongraph.mvc.FunctionGraphVertexAttributes: ...

    @property
    def ungroupedEdges(self) -> java.util.Set: ...

    @property
    def ungroupedVertices(self) -> java.util.Set: ...