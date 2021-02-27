import ghidra.program.model.mem
import java.io
import java.lang


class ExpressionValue(java.io.Serializable, object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def length(self, buf: ghidra.program.model.mem.MemBuffer, offset: int) -> int: ...

    def longValue(self, buf: ghidra.program.model.mem.MemBuffer, offset: int) -> long: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
