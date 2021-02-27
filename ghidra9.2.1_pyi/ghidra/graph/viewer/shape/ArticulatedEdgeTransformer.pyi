import edu.uci.ics.jung.graph.util
import edu.uci.ics.jung.visualization.decorators
import ghidra.graph.viewer
import java.awt
import java.lang


class ArticulatedEdgeTransformer(edu.uci.ics.jung.visualization.decorators.ParallelEdgeShapeTransformer):
    """
    An edge shape that renders as a series of straight lines between articulation points.
    """





    def __init__(self): ...



    @overload
    def apply(self, __a0: ghidra.graph.viewer.VisualEdge) -> java.awt.Shape: ...

    @overload
    def apply(self, __a0: object) -> object: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getEdgeIndexFunction(self) -> edu.uci.ics.jung.graph.util.EdgeIndexFunction: ...

    def getOverlapOffset(self, __a0: ghidra.graph.viewer.VisualEdge) -> int: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setControlOffsetIncrement(self, __a0: float) -> None: ...

    def setEdgeIndexFunction(self, __a0: edu.uci.ics.jung.graph.util.EdgeIndexFunction) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
