import ghidra.program.model.address
import java.lang


class SearchAddressIterator(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hasNext(self) -> bool: ...

    def hashCode(self) -> int: ...

    def next(self) -> ghidra.program.model.address.Address: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
