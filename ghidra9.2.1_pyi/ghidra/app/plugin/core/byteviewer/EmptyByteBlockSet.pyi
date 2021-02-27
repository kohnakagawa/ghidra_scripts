from typing import List
import ghidra.app.events
import ghidra.app.plugin.core.format
import java.lang


class EmptyByteBlockSet(object, ghidra.app.plugin.core.format.ByteBlockSet):




    def __init__(self): ...



    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getBlocks(self) -> List[ghidra.app.plugin.core.format.ByteBlock]: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    def getPluginEvent(self, __a0: unicode, __a1: ghidra.app.plugin.core.format.ByteBlockSelection) -> ghidra.app.events.ProgramSelectionPluginEvent: ...

    @overload
    def getPluginEvent(self, __a0: unicode, __a1: ghidra.app.plugin.core.format.ByteBlock, __a2: long, __a3: int) -> ghidra.app.events.ProgramLocationPluginEvent: ...

    def hashCode(self) -> int: ...

    def isChanged(self, __a0: ghidra.app.plugin.core.format.ByteBlock, __a1: long, __a2: int) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def notifyByteEditing(self, __a0: ghidra.app.plugin.core.format.ByteBlock, __a1: long, __a2: List[int], __a3: List[int]) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def blocks(self) -> List[ghidra.app.plugin.core.format.ByteBlock]: ...