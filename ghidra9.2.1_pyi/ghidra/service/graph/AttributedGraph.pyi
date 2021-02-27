import ghidra.service.graph
import java.lang
import java.util
import java.util.function
import org.jgrapht
import org.jgrapht.graph


class AttributedGraph(org.jgrapht.graph.AbstractBaseGraph):
    """
    Basic graph implementation for a directed graph whose vertices and edges support attributes.

     The graph can be configured as to how to handle multiple edges with the same source and destination
     vertices. One option is to simply allow multiple edges.  The second option is to collapse
     duplicate edges such that there is only ever one edge with the same
     source and destination.  In this case, each additional duplicate edge added will cause the
     edge to have a "Weight" attribute that will be the total number of edges that were added
     to the same source/destination vertex pair.
    """





    @overload
    def __init__(self):
        """
        Create a new empty AttributedGraph that automatically collapses duplicate edges
        """
        ...

    @overload
    def __init__(self, collapseDuplicateEdges: bool):
        """
        Create a new empty AttributedGraph.
        @param collapseDuplicateEdges if true, duplicate edges will be collapsed into a single
         edge with a "Weight" attribute whose value is the number of edges between those vertices.
        """
        ...



    @overload
    def addEdge(self, source: ghidra.service.graph.AttributedVertex, target: ghidra.service.graph.AttributedVertex) -> ghidra.service.graph.AttributedEdge:
        """
        Creates and adds a new directed edge between the given source and
         target vertices. If the graph is set to collapse duplicate edges and an edge for that
         source and target exists, then the existing edge will be return with its "Weight" attribute
         set to the total number of edges that have been added between the source and target vertices.
        @param source the source vertex of the directed edge to be created.
        @param target the target vertex of the directed edge to be created.
        @return a new edge between the source and target if it is the first one or the graph is
         not collapsing edges.  Otherwise, an existing edge with its "Weight" attribute set accordingly.
        """
        ...

    @overload
    def addEdge(self, __a0: object, __a1: object) -> object: ...

    @overload
    def addEdge(self, source: ghidra.service.graph.AttributedVertex, target: ghidra.service.graph.AttributedVertex, edgeId: unicode) -> ghidra.service.graph.AttributedEdge:
        """
        Creates and adds a new directed edge with the given id between the given source and
         target vertices. If the graph is set to collapse duplicate edges and an edge for that
         source and target exists, then the existing edge will be return with its "Weight" attribute
         set to the total number of edges that have been added between the source and target vertices.
        @param source the source vertex of the directed edge to be created.
        @param target the target vertex of the directed edge to be created.
        @param edgeId the id to use for the new edge.  Note: if this is a duplicate and edges
         are being collapsed, then this edgeId will not be used.
        @return a new edge between the source and target if it is the first one or the graph is
         not collapsing edges.  Otherwise, an existing edge with its "Weight" attribute set accordingly.
        """
        ...

    @overload
    def addEdge(self, source: ghidra.service.graph.AttributedVertex, target: ghidra.service.graph.AttributedVertex, edge: ghidra.service.graph.AttributedEdge) -> bool:
        """
        Creates and adds a new directed edge with the given edge object. If the graph is set to
         collapse duplicate edges and an edge for that
         source and target exists, then the existing edge will be return with its "Weight" attribute
         set to the total number of edges that have been added between the source and target vertices.
        @param source the source vertex of the directed edge to be created.
        @param target the target vertex of the directed edge to be created.
        @param edge the BasicEdge object to use for the new edge.  Note: if this is a duplicate and
         edges are being collapsed, then this edge object will not be used.
        @return true if the edge was added. Note that if this graph is collapsing duplicate edges, then
         it will always return true.
        """
        ...

    @overload
    def addEdge(self, __a0: object, __a1: object, __a2: object) -> bool: ...

    @overload
    def addVertex(self) -> ghidra.service.graph.AttributedVertex: ...

    @overload
    def addVertex(self, id: unicode) -> ghidra.service.graph.AttributedVertex:
        """
        Adds a new vertex with the given id.  The vertex's name will be the same as the id.
         If a vertex already exists with that id,
         then that vertex will be returned.
        @param id the unique vertex id that the graph should have a vertex for.
        @return either an existing vertex with that id, or a newly added vertex with that id
        """
        ...

    @overload
    def addVertex(self, vertex: ghidra.service.graph.AttributedVertex) -> bool: ...

    @overload
    def addVertex(self, __a0: object) -> bool: ...

    @overload
    def addVertex(self, id: unicode, name: unicode) -> ghidra.service.graph.AttributedVertex:
        """
        Adds a new vertex with the given id and name.  If a vertex already exists with that id,
         then that vertex will be returned, but with its name changed to the given name.
        @param id the unique vertex id that the graph should have a vertex for.
        @param name the name to associate with this vertex
        @return either an existing vertex with that id, or a newly added vertex with that id
        """
        ...

    def clone(self) -> object: ...

    @overload
    def containsEdge(self, __a0: object) -> bool: ...

    @overload
    def containsEdge(self, __a0: object, __a1: object) -> bool: ...

    def containsVertex(self, __a0: object) -> bool: ...

    def degreeOf(self, __a0: object) -> int: ...

    def edgeSet(self) -> java.util.Set: ...

    def edgesOf(self, __a0: object) -> java.util.Set: ...

    def equals(self, __a0: object) -> bool: ...

    def getAllEdges(self, __a0: object, __a1: object) -> java.util.Set: ...

    def getClass(self) -> java.lang.Class: ...

    def getEdge(self, __a0: object, __a1: object) -> object: ...

    def getEdgeCount(self) -> int:
        """
        Returns the total number of edges in the graph
        @return the total number of edges in the graph
        """
        ...

    def getEdgeSource(self, __a0: object) -> object: ...

    def getEdgeSupplier(self) -> java.util.function.Supplier: ...

    def getEdgeTarget(self, __a0: object) -> object: ...

    def getEdgeWeight(self, __a0: object) -> float: ...

    def getType(self) -> org.jgrapht.GraphType: ...

    def getVertex(self, vertexId: unicode) -> ghidra.service.graph.AttributedVertex:
        """
        Returns the vertex with the given vertex id
        @param vertexId the id of the vertex to retrieve
        @return the vertex with the given vertex id or null if none found
        """
        ...

    def getVertexCount(self) -> int:
        """
        Returns the total number of vertices in the graph
        @return the total number of vertices in the graph
        """
        ...

    def getVertexSupplier(self) -> java.util.function.Supplier: ...

    def hashCode(self) -> int: ...

    def inDegreeOf(self, __a0: object) -> int: ...

    def incomingEdgesOf(self, __a0: object) -> java.util.Set: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def outDegreeOf(self, __a0: object) -> int: ...

    def outgoingEdgesOf(self, __a0: object) -> java.util.Set: ...

    @overload
    def removeAllEdges(self, __a0: java.util.Collection) -> bool: ...

    @overload
    def removeAllEdges(self, __a0: object, __a1: object) -> java.util.Set: ...

    def removeAllVertices(self, __a0: java.util.Collection) -> bool: ...

    @overload
    def removeEdge(self, __a0: object) -> bool: ...

    @overload
    def removeEdge(self, __a0: object, __a1: object) -> object: ...

    def removeVertex(self, __a0: object) -> bool: ...

    def setEdgeSupplier(self, __a0: java.util.function.Supplier) -> None: ...

    @overload
    def setEdgeWeight(self, __a0: object, __a1: float) -> None: ...

    @overload
    def setEdgeWeight(self, __a0: object, __a1: object, __a2: float) -> None: ...

    def setVertexSupplier(self, __a0: java.util.function.Supplier) -> None: ...

    def toString(self) -> unicode: ...

    def vertexSet(self) -> java.util.Set: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def edgeCount(self) -> int: ...

    @property
    def vertexCount(self) -> int: ...
