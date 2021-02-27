import ghidra.app.plugin.core.format
import ghidra.framework.plugintool
import ghidra.program.model.listing
import java.lang


class ByteBlockChangePluginEvent(ghidra.framework.plugintool.PluginEvent):




    def __init__(self, __a0: unicode, __a1: ghidra.app.plugin.core.format.ByteEditInfo, __a2: ghidra.program.model.listing.Program): ...



    def equals(self, __a0: object) -> bool: ...

    def getByteEditInfo(self) -> ghidra.app.plugin.core.format.ByteEditInfo: ...

    def getClass(self) -> java.lang.Class: ...

    def getEventName(self) -> unicode: ...

    def getProgram(self) -> ghidra.program.model.listing.Program: ...

    def getSourceName(self) -> unicode: ...

    def getToolEventName(self) -> unicode: ...

    def getTriggerEvent(self) -> ghidra.framework.plugintool.PluginEvent: ...

    def hashCode(self) -> int: ...

    def isToolEvent(self) -> bool: ...

    @staticmethod
    def lookupToolEventName(__a0: java.lang.Class) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setSourceName(self, __a0: unicode) -> None: ...

    def setTriggerEvent(self, __a0: ghidra.framework.plugintool.PluginEvent) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def byteEditInfo(self) -> ghidra.app.plugin.core.format.ByteEditInfo: ...

    @property
    def program(self) -> ghidra.program.model.listing.Program: ...