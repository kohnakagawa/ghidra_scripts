import edu.uci.ics.jung.graph.util
import ghidra.graph
import java.lang
import java.util


class JungToGDirectedGraphAdapter(object, ghidra.graph.GDirectedGraph):
    """
    A class that turns a Graph into a GDirectedGraph.
    """





    def __init__(self, delegate: edu.uci.ics.jung.graph.Graph): ...



    @overload
    def addEdge(self, __a0: ghidra.graph.GEdge) -> None: ...

    @overload
    def addEdge(self, __a0: ghidra.graph.GEdge, __a1: java.util.Collection) -> bool: ...

    @overload
    def addEdge(self, __a0: ghidra.graph.GEdge, __a1: java.util.Collection, __a2: edu.uci.ics.jung.graph.util.EdgeType) -> bool: ...

    @overload
    def addEdge(self, __a0: ghidra.graph.GEdge, __a1: object, __a2: object) -> bool: ...

    @overload
    def addEdge(self, __a0: ghidra.graph.GEdge, __a1: object, __a2: object, __a3: edu.uci.ics.jung.graph.util.EdgeType) -> bool: ...

    def addVertex(self, __a0: object) -> bool: ...

    @overload
    def containsEdge(self, __a0: ghidra.graph.GEdge) -> bool: ...

    @overload
    def containsEdge(self, __a0: object, __a1: object) -> bool: ...

    def containsVertex(self, __a0: object) -> bool: ...

    def copy(self) -> ghidra.graph.GDirectedGraph: ...

    def degree(self, __a0: object) -> int: ...

    def emptyCopy(self) -> ghidra.graph.GDirectedGraph: ...

    def equals(self, __a0: object) -> bool: ...

    def findEdge(self, __a0: object, __a1: object) -> ghidra.graph.GEdge: ...

    def findEdgeSet(self, __a0: object, __a1: object) -> java.util.Collection: ...

    def getClass(self) -> java.lang.Class: ...

    def getDefaultEdgeType(self) -> edu.uci.ics.jung.graph.util.EdgeType: ...

    def getDest(self, __a0: ghidra.graph.GEdge) -> object: ...

    @overload
    def getEdgeCount(self) -> int: ...

    @overload
    def getEdgeCount(self, edge_type: edu.uci.ics.jung.graph.util.EdgeType) -> int: ...

    def getEdgeType(self, __a0: ghidra.graph.GEdge) -> edu.uci.ics.jung.graph.util.EdgeType: ...

    @overload
    def getEdges(self) -> java.util.Collection: ...

    @overload
    def getEdges(self, edge_type: edu.uci.ics.jung.graph.util.EdgeType) -> java.util.Collection: ...

    def getEndpoints(self, __a0: ghidra.graph.GEdge) -> edu.uci.ics.jung.graph.util.Pair: ...

    def getInEdges(self, __a0: object) -> java.util.Collection: ...

    def getIncidentCount(self, __a0: ghidra.graph.GEdge) -> int: ...

    def getIncidentEdges(self, __a0: object) -> java.util.Collection: ...

    def getIncidentVertices(self, __a0: ghidra.graph.GEdge) -> java.util.Collection: ...

    def getNeighborCount(self, __a0: object) -> int: ...

    def getNeighbors(self, __a0: object) -> java.util.Collection: ...

    def getOpposite(self, __a0: object, __a1: ghidra.graph.GEdge) -> object: ...

    def getOutEdges(self, __a0: object) -> java.util.Collection: ...

    def getPredecessorCount(self, __a0: object) -> int: ...

    def getPredecessors(self, __a0: object) -> java.util.Collection: ...

    def getSource(self, __a0: ghidra.graph.GEdge) -> object: ...

    def getSuccessorCount(self, __a0: object) -> int: ...

    def getSuccessors(self, __a0: object) -> java.util.Collection: ...

    def getVertexCount(self) -> int: ...

    def getVertices(self) -> java.util.Collection: ...

    def hashCode(self) -> int: ...

    def inDegree(self, __a0: object) -> int: ...

    def isDest(self, __a0: object, __a1: ghidra.graph.GEdge) -> bool: ...

    def isEmpty(self) -> bool: ...

    def isIncident(self, __a0: object, __a1: ghidra.graph.GEdge) -> bool: ...

    def isNeighbor(self, __a0: object, __a1: object) -> bool: ...

    def isPredecessor(self, __a0: object, __a1: object) -> bool: ...

    def isSource(self, __a0: object, __a1: ghidra.graph.GEdge) -> bool: ...

    def isSuccessor(self, __a0: object, __a1: object) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def outDegree(self, __a0: object) -> int: ...

    def removeEdge(self, __a0: ghidra.graph.GEdge) -> bool: ...

    def removeEdges(self, edges: java.lang.Iterable) -> None: ...

    def removeVertex(self, __a0: object) -> bool: ...

    def removeVertices(self, vertices: java.lang.Iterable) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def defaultEdgeType(self) -> edu.uci.ics.jung.graph.util.EdgeType: ...

    @property
    def edgeCount(self) -> int: ...

    @property
    def edges(self) -> java.util.Collection: ...

    @property
    def empty(self) -> bool: ...

    @property
    def vertexCount(self) -> int: ...

    @property
    def vertices(self) -> java.util.Collection: ...