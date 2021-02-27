from typing import List
import ghidra.app.plugin.core.format
import java.lang


class IndexMap(object):








    def equals(self, __a0: object) -> bool: ...

    def getBlocksBetween(self, __a0: ghidra.app.plugin.core.format.ByteBlockInfo, __a1: ghidra.app.plugin.core.format.ByteBlockInfo) -> List[object]: ...

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
