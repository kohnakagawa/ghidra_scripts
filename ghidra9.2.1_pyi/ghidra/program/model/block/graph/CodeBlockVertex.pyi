import ghidra.program.model.block
import ghidra.program.model.block.graph
import java.lang


class CodeBlockVertex(object, java.lang.Comparable):
    """
    A class for representing a code block within a graph.
    """





    @overload
    def __init__(self, name: unicode):
        """
        A constructor that allows for the creation of dummy nodes.  This is useful in graphs
         where multiple entry or exit points need to be parented by a single vertex.
        @param name the name of this vertex
        """
        ...

    @overload
    def __init__(self, codeBlock: ghidra.program.model.block.CodeBlock):
        """
        Constructor.
        @param codeBlock the code block for this vertex
        """
        ...



    @overload
    def compareTo(self, o: ghidra.program.model.block.graph.CodeBlockVertex) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, obj: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getCodeBlock(self) -> ghidra.program.model.block.CodeBlock: ...

    def getName(self) -> unicode: ...

    def hashCode(self) -> int: ...

    def isDummy(self) -> bool:
        """
        Returns true if this vertex is not backed by a code block.
        @return true if this vertex is not backed by a code block.
        """
        ...

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
    def codeBlock(self) -> ghidra.program.model.block.CodeBlock: ...

    @property
    def dummy(self) -> bool: ...

    @property
    def name(self) -> unicode: ...
