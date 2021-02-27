import ghidra.framework.data
import ghidra.framework.model
import ghidra.framework.plugintool
import java.lang


class GhidraToolStateFactory(ghidra.framework.data.ToolStateFactory):




    def __init__(self): ...



    @staticmethod
    def createToolState(tool: ghidra.framework.plugintool.PluginTool, domainObject: ghidra.framework.model.DomainObject) -> ghidra.framework.data.ToolState: ...

    def equals(self, __a0: object) -> bool: ...

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
