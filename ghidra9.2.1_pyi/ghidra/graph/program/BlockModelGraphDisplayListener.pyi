import ghidra.app.plugin.core.graph
import ghidra.framework.model
import ghidra.framework.plugintool
import ghidra.program.model.address
import ghidra.service.graph
import java.lang
import java.util


class BlockModelGraphDisplayListener(ghidra.app.plugin.core.graph.AddressBasedGraphDisplayListener):




    def __init__(self, __a0: ghidra.framework.plugintool.PluginTool, __a1: ghidra.program.model.block.CodeBlockModel, __a2: ghidra.service.graph.GraphDisplay): ...



    def cloneWith(self, __a0: ghidra.service.graph.GraphDisplay) -> ghidra.service.graph.GraphDisplayListener: ...

    def dispose(self) -> None: ...

    def domainObjectChanged(self, __a0: ghidra.framework.model.DomainObjectChangedEvent) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def eventSent(self, __a0: ghidra.framework.plugintool.PluginEvent) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def getVertex(self, __a0: ghidra.program.model.address.Address) -> ghidra.service.graph.AttributedVertex: ...

    def graphClosed(self) -> None: ...

    def hashCode(self) -> int: ...

    def locationFocusChanged(self, __a0: ghidra.service.graph.AttributedVertex) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def selectionChanged(self, __a0: java.util.Set) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
