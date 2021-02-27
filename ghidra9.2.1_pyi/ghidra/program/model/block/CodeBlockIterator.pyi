import ghidra.program.model.block
import java.lang


class CodeBlockIterator(object):
    """
    An iterator interface over CodeBlocks.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hasNext(self) -> bool:
        """
        Return true if next() will return a CodeBlock.
        @throws CancelledException thrown if the operation is cancelled.
        """
        ...

    def hashCode(self) -> int: ...

    def next(self) -> ghidra.program.model.block.CodeBlock:
        """
        Return the next CodeBlock.
        @throws CancelledException thrown if the operation is cancelled.
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
