import edu.uci.ics.jung.algorithms.layout
import ghidra.graph
import ghidra.graph.viewer.layout
import java.lang
import java.util


class LayoutPositions(object):
    """
    Simple container class to hold vertex locations (points) and edge articulation locations
     (points).  The only complicated code in this class is the use of transformers to create
     copies of the given points as they are accessed so that the original points remain unmodified.
    """









    @staticmethod
    def createEmptyPositions() -> ghidra.graph.viewer.layout.LayoutPositions: ...

    @staticmethod
    def createNewPositions(vertexLocations: java.util.Map, edgeArticulations: java.util.Map) -> ghidra.graph.viewer.layout.LayoutPositions: ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getCurrentPositions(graph: ghidra.graph.VisualGraph, graphLayout: edu.uci.ics.jung.algorithms.layout.Layout) -> ghidra.graph.viewer.layout.LayoutPositions: ...

    def getEdgeArticulations(self) -> java.util.Map: ...

    def getVertexLocations(self) -> java.util.Map: ...

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

    @property
    def edgeArticulations(self) -> java.util.Map: ...

    @property
    def vertexLocations(self) -> java.util.Map: ...
