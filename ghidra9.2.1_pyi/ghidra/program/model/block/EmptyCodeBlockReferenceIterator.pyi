import ghidra.program.model.block
import java.lang


class EmptyCodeBlockReferenceIterator(object, ghidra.program.model.block.CodeBlockReferenceIterator):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hasNext(self) -> bool: ...

    def hashCode(self) -> int: ...

    def next(self) -> ghidra.program.model.block.CodeBlockReference: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
