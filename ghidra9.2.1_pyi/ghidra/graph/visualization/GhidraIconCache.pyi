import ghidra.service.graph
import java.lang


class GhidraIconCache(object):








    def clear(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def evict(self, __a0: ghidra.service.graph.AttributedVertex) -> None: ...

    def getClass(self) -> java.lang.Class: ...

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
