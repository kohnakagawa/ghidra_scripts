from typing import Iterator
import ghidra.program.model.symbol
import java.lang
import java.util
import java.util.function


class ReferenceIteratorAdapter(object, ghidra.program.model.symbol.ReferenceIterator):




    def __init__(self, iterator: java.util.Iterator): ...

    def __iter__(self) -> Iterator[ghidra.program.model.symbol.Reference]: ...

    def equals(self, __a0: object) -> bool: ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    def forEachRemaining(self, __a0: java.util.function.Consumer) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def hasNext(self) -> bool: ...

    def hashCode(self) -> int: ...

    def iterator(self) -> Iterator[ghidra.program.model.symbol.Reference]: ...

    def next(self) -> ghidra.program.model.symbol.Reference: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def remove(self) -> None: ...

    def spliterator(self) -> java.util.Spliterator: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
