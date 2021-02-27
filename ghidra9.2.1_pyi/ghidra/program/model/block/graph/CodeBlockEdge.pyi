import ghidra.graph
import java.lang


class CodeBlockEdge(ghidra.graph.DefaultGEdge):
    """
    A simple edge type for representing a link between two
     CodeBlockVertex.
    """





    def __init__(self, start: ghidra.program.model.block.graph.CodeBlockVertex, end: ghidra.program.model.block.graph.CodeBlockVertex):
        """
        Constructor.
        @param start the start vertex
        @param end the end vertex
        """
        ...



    def equals(self, obj: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getEnd(self) -> V: ...

    def getStart(self) -> V: ...

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
