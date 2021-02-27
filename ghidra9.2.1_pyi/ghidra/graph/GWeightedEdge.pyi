import ghidra.graph
import java.lang


class GWeightedEdge(ghidra.graph.GEdge, object):
    """
    An edge having a natural weight
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getEnd(self) -> object: ...

    def getStart(self) -> object: ...

    def getWeight(self) -> float:
        """
        The natural weight of the edge
        @return the weight
        """
        ...

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
    def end(self) -> object: ...

    @property
    def start(self) -> object: ...

    @property
    def weight(self) -> float: ...
