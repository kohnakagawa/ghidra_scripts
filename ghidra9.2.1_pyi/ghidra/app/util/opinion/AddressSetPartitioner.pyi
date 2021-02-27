from typing import Iterator
import ghidra.program.model.address
import java.lang
import java.util
import java.util.function


class AddressSetPartitioner(object, java.lang.Iterable):




    def __init__(self, set: ghidra.program.model.address.AddressSet, rangeMap: java.util.Map, partitionSet: java.util.Set): ...

    def __iter__(self): ...

    def equals(self, __a0: object) -> bool: ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def getPartionedRangeMap(self) -> java.util.Map: ...

    def hashCode(self) -> int: ...

    def iterator(self) -> Iterator[ghidra.program.model.address.AddressRange]: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def spliterator(self) -> java.util.Spliterator: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def partionedRangeMap(self) -> java.util.Map: ...