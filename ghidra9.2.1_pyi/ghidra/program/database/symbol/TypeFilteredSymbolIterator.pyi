from typing import Iterator
import ghidra.program.model.symbol
import java.lang
import java.util
import java.util.function


class TypeFilteredSymbolIterator(object, ghidra.program.model.symbol.SymbolIterator):
    """
    Filters a symbol iterator to only return a specific symbol type
    """





    def __init__(self, it: ghidra.program.model.symbol.SymbolIterator, type: ghidra.program.model.symbol.SymbolType):
        """
        Construct a new TypeFilteredSymbolIterator
        @param it the symbol iterator to filter
        @param type the symbol type to filter on.
        """
        ...

    def __iter__(self) -> Iterator[ghidra.program.model.symbol.Symbol]: ...

    def equals(self, __a0: object) -> bool: ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    def forEachRemaining(self, __a0: java.util.function.Consumer) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def hasNext(self) -> bool:
        """
        @see ghidra.program.model.symbol.SymbolIterator#hasNext()
        """
        ...

    def hashCode(self) -> int: ...

    def iterator(self) -> Iterator[ghidra.program.model.symbol.Symbol]: ...

    def next(self) -> ghidra.program.model.symbol.Symbol:
        """
        @see ghidra.program.model.symbol.SymbolIterator#next()
        """
        ...

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
