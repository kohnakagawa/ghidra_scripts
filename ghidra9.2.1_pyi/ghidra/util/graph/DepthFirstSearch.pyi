from typing import List
import ghidra.util.graph
import java.lang


class DepthFirstSearch(object):
    """
    Provides a depth first search service to directed graphs.
     Once a search has finished information about the search
     can be obtained.
    """





    def __init__(self, graph: ghidra.util.graph.DirectedGraph, initialSeeds: List[ghidra.util.graph.Vertex], getAdditionalSeedsIfNeeded: bool, goForward: bool, goBackward: bool):
        """
        Upon creation a depth first search of the given graph is performed.
        @param graph The graph to search
        @param initialSeeds The vertices used to start the search
        @param getAdditionalSeedsIfNeeded If true, when searching from the initial
         seeds does not find all vertices in the graph, additional start vertices will
         be selected until every vertex is the graph has been found.
        @param goForward Follow edges in their specifed direction
        @param goBackward Follow edges in the opposite of their specified direction.
        """
        ...



    def backEdges(self) -> List[ghidra.util.graph.Edge]:
        """
        Return the back edges found in this depth first search.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isAcyclic(self) -> bool:
        """
        Return true iff no back edges were found.

         Note that if the graph
         is not completely explored the answer is only for the portion
         of the graph expored.
        """
        ...

    def isCompleted(self, v: ghidra.util.graph.Vertex) -> bool:
        """
        Return true if the vertex has completed its role in the depth first
         search.
        """
        ...

    def isTree(self) -> bool:
        """
        Return true iff the every edge is a tree edge. Will always be false
         if the entire graph is not explored.
        """
        ...

    def isUnseen(self, v: ghidra.util.graph.Vertex) -> bool:
        """
        Return true if the vertex has not yet been discovered in the depth first
         search.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def spanningTree(self) -> ghidra.util.graph.DirectedGraph:
        """
        Returns a spanning tree (in the form of a DirectedGraph).
         No claims that the spanning tree returned has any special
         properties.
        """
        ...

    def toString(self) -> unicode: ...

    def topologicalSort(self) -> List[ghidra.util.graph.Vertex]:
        """
        Returns a topological sort of the directed graph.
         Return the vertices in the explored
         portion of the graph with the following
         property:
         <ol>
         <li>{@literal If the graph is acyclic then v[i] -> v[j] => i < j .}</li>
         <li>If the graph contains cycles, then the above is true except when
             (v[i],v[j]) is a back edge.</li>
         </ol>
        """
        ...

    def treeEdges(self) -> List[ghidra.util.graph.Edge]:
        """
        Return the tree edges in this depth first search.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def acyclic(self) -> bool: ...

    @property
    def tree(self) -> bool: ...
