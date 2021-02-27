from typing import List
import ghidra.graph
import ghidra.graph.algo
import ghidra.util.datastruct
import ghidra.util.task
import java.io
import java.lang
import java.util


class GraphAlgorithms(object):
    """
    A set of convenience methods for performing graph algorithms on a graph.

     Some definitions:


     		dominance:
     					a node 'a' dominates node 'b' if all paths from start to 'b' contain 'a';
    		            a node always dominates itself (except in 'strict dominance', which is all
    		            dominators except for itself)


    		post-dominance:
    					 A node 'b' is said to post-dominate node 'a' if all paths from 'a'
    		             to END contain 'b'


    		immediate dominator:
    					the closest dominator of a node


    		dominance tree:
    					A dominator tree is a tree where each node's children are those nodes
    					it *immediately* dominates (a idom b)


         	dominance frontier:
         				the immediate successors of the nodes dominated by 'a'; it is the set of
         				nodes where d's dominance stops.


         	strongly connected components:
         				a graph is said to be strongly connected if every vertex is reachable
         				from every other vertex. The strongly connected components
         				of an arbitrary directed graph form a partition into
         				subgraphs that are themselves strongly connected.

         	graph density:

                            E
              Density =  --------
                          V(V-1)


    """









    @staticmethod
    def createSubGraph(g: ghidra.graph.GDirectedGraph, vertices: java.util.Collection) -> ghidra.graph.GDirectedGraph:
        """
        Creates a subgraph of the given graph for each edge of the given graph that is
         contained in the list of vertices.
        @param g the existing graph
        @param vertices the vertices to be in the new graph
        @return the new subgraph
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    @overload
    @staticmethod
    def findCircuits(g: ghidra.graph.GDirectedGraph, monitor: ghidra.util.task.TaskMonitor) -> List[java.util.List]:
        """
        Finds all the circuits, or cycles, in the given graph.
        @param g the graph
        @param monitor the task monitor
        @return the circuits
        @throws CancelledException if the monitor is cancelled
        """
        ...

    @overload
    @staticmethod
    def findCircuits(g: ghidra.graph.GDirectedGraph, uniqueCircuits: bool, monitor: ghidra.util.task.TimeoutTaskMonitor) -> List[java.util.List]:
        """
        Finds all the circuits, or cycles, in the given graph.  <B>This version
         of <code>findCircuits()</code> takes a {@link TimeoutTaskMonitor}, which allows for the
         client to control the duration of work.</B>   This is useful for finding paths on very
         large, dense graphs.
        @param g the graph
        @param uniqueCircuits true signals to return only unique circuits, where no two
                circuits will contain the same vertex
        @param monitor the timeout task monitor
        @return the circuits
        @throws CancelledException if the monitor is cancelled
        @throws TimeoutException if the algorithm times-out, as defined by the monitor
        """
        ...

    @overload
    @staticmethod
    def findCircuits(g: ghidra.graph.GDirectedGraph, uniqueCircuits: bool, monitor: ghidra.util.task.TaskMonitor) -> List[java.util.List]:
        """
        Finds all the circuits, or cycles, in the given graph.
        @param g the graph
        @param uniqueCircuits true signals to return only unique circuits, where no two
                circuits will contain the same vertex
        @param monitor the task monitor
        @return the circuits
        @throws CancelledException if the monitor is cancelled
        """
        ...

    @staticmethod
    def findDominance(__a0: ghidra.graph.GDirectedGraph, __a1: object, __a2: ghidra.util.task.TaskMonitor) -> java.util.Set: ...

    @staticmethod
    def findDominanceTree(g: ghidra.graph.GDirectedGraph, monitor: ghidra.util.task.TaskMonitor) -> ghidra.graph.GDirectedGraph:
        """
        Returns the dominance tree of the given graph.  A dominator tree of the vertices where each
         node's children are those nodes it *immediately* dominates (a idom b)
        @param g the graph
        @param monitor the task monitor
        @return the tree
        @throws CancelledException if the monitor is cancelled
        """
        ...

    @overload
    @staticmethod
    def findPaths(__a0: ghidra.graph.GDirectedGraph, __a1: object, __a2: object, __a3: ghidra.util.datastruct.Accumulator, __a4: ghidra.util.task.TimeoutTaskMonitor) -> None: ...

    @overload
    @staticmethod
    def findPaths(__a0: ghidra.graph.GDirectedGraph, __a1: object, __a2: object, __a3: ghidra.util.datastruct.Accumulator, __a4: ghidra.util.task.TaskMonitor) -> None: ...

    @staticmethod
    def findPostDominance(__a0: ghidra.graph.GDirectedGraph, __a1: object, __a2: ghidra.util.task.TaskMonitor) -> java.util.Set: ...

    @staticmethod
    def getAncestors(g: ghidra.graph.GDirectedGraph, vertices: java.util.Collection) -> java.util.Set:
        """
        Returns all ancestors for the given vertices in the given graph.  Ancestors for a given
         vertex are all nodes at the incoming side of an edge, as well as their incoming
         vertices, etc.
        @param g the graph
        @param vertices the vertices for which to find descendants
        @return the ancestors
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getComplexityDepth(g: ghidra.graph.GDirectedGraph) -> java.util.Map:
        """
        Calculates 'complexity depth', which is, for each vertex, the deepest/longest path
         from that vertex for a depth-first traversal.   So, for a vertex with a single
         successor that has no children, the depth would be 1.
        @param g the graph
        @return the map of each vertex to its complexity depth
        """
        ...

    @staticmethod
    def getDescendants(g: ghidra.graph.GDirectedGraph, vertices: java.util.Collection) -> java.util.Set:
        """
        Returns all descendants for the given vertices in the given graph.  Descendants for a given
         vertex are all nodes at the outgoing side of an edge, as well as their outgoing
         vertices, etc.
        @param g the graph
        @param vertices the vertices for which to find descendants
        @return the descendants
        """
        ...

    @overload
    @staticmethod
    def getEdgesFrom(g: ghidra.graph.GDirectedGraph, vertices: java.util.Collection, topDown: bool) -> java.util.Set:
        """
        Returns a set of all edges that are reachable from the given collection of vertices.
        @param g the graph
        @param vertices the vertices for which to get edges
        @param topDown true for outgoing edges; false for incoming edges
        @return the set of edges
        """
        ...

    @overload
    @staticmethod
    def getEdgesFrom(__a0: ghidra.graph.GDirectedGraph, __a1: object, __a2: bool) -> java.util.Set: ...

    @staticmethod
    def getEntryPoints(g: ghidra.graph.GDirectedGraph) -> java.util.Set:
        """
        Returns all entry points in the given graph.  This includes sources, vertices which
         have no incoming edges, as well as strongly connected sub-graphs.  The latter being a
         group vertices where each vertex is reachable from every other vertex.  In the case of
         strongly connected components, we pick one of them arbitrarily to be the entry point.
        @param g the graph
        @return the entry points into the graph
        """
        ...

    @staticmethod
    def getSinks(g: ghidra.graph.GDirectedGraph) -> java.util.Set:
        """
        Returns all sink vertices (those with no outgoing edges) in the graph.
        @param g the graph
        @return sink vertices
        """
        ...

    @staticmethod
    def getSources(g: ghidra.graph.GDirectedGraph) -> java.util.Set:
        """
        Returns all source vertices (those with no incoming edges) in the graph.
        @param g the graph
        @return source vertices
        """
        ...

    @staticmethod
    def getStronglyConnectedComponents(g: ghidra.graph.GDirectedGraph) -> java.util.Set:
        """
        Returns a list where each set therein is a strongly connected component of the given
         graph.  Each strongly connected component is that in which each vertex is reachable from
         any other vertex in that set.

         <P>This method can be used to determine reachability of a set of vertices.

         <P>This can also be useful for cycle detection, as a multi-vertex strong component
         is by definition a cycle.  This method differs from
         {@link #findCircuits(GDirectedGraph, boolean, TaskMonitor)} in that the latter will
         return cycles within the strong components, or sub-cycles.
        @param g the graph
        @return the list of strongly connected components
        """
        ...

    @staticmethod
    def getVerticesInPostOrder(g: ghidra.graph.GDirectedGraph, navigator: ghidra.graph.algo.GraphNavigator) -> List[V]:
        """
        Returns the vertices of the graph in post-order.   Pre-order is the order the vertices
         are last visited when performing a depth-first traversal.
        @param g the graph
        @param navigator the knower of the direction the graph should be traversed
        @return the vertices
        """
        ...

    @staticmethod
    def getVerticesInPreOrder(g: ghidra.graph.GDirectedGraph, navigator: ghidra.graph.algo.GraphNavigator) -> List[V]:
        """
        Returns the vertices of the graph in pre-order.   Pre-order is the order the vertices
         are encountered when performing a depth-first traversal.
        @param g the graph
        @param navigator the knower of the direction the graph should be traversed
        @return the vertices
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def printGraph(g: ghidra.graph.GDirectedGraph, ps: java.io.PrintStream) -> None:
        """
        A method to debug the given graph by printing it.
        @param g the graph to print
        @param ps the output stream
        """
        ...

    @staticmethod
    def retainEdges(graph: ghidra.graph.GDirectedGraph, vertices: java.util.Set) -> java.util.Set:
        """
        Retain all edges in the graph where each edge's endpoints are in the given set of
         vertices.
        @param graph the graph
        @param vertices the vertices of the edges to keep
        @return the set of edges
        """
        ...

    def toString(self) -> unicode: ...

    @staticmethod
    def toVertices(edges: java.util.Collection) -> java.util.Set:
        """
        Returns the set of vertices contained within the given edges.
        @param edges the edges
        @return the vertices
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
