import ghidra.graph
import java.lang
import java.util


class GImplicitDirectedGraph(object):
    """
    A directed graph that need not be constructed explicitly

     Instead, the graph is constructed (and usually cached) as it is explored. For instance, if
     a path searching algorithm is being applied, incident edges and neighboring nodes need not
     be computed if they're never visited. This allows conceptually large (even infinite) graphs to
     be represented. A graph algorithm can be applied so long as it supports this interface, and
     does not attempt to exhaust an infinite graph.
    """









    def copy(self) -> ghidra.graph.GDirectedGraph:
        """
        Copy some portion of the implicit graph to an explicit graph

         Usually, this returns the cached (explored) portion of the graph
        @return a "copy" of this implicit graph
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getInEdges(self, __a0: object) -> java.util.Collection: ...

    def getOutEdges(self, __a0: object) -> java.util.Collection: ...

    def getPredecessors(self, __a0: object) -> java.util.Collection: ...

    def getSuccessors(self, __a0: object) -> java.util.Collection: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
