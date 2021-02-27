import ghidra.framework.options
import ghidra.framework.plugintool
import ghidra.service.graph
import ghidra.util
import ghidra.util.task
import java.lang


class ExportAttributedGraphDisplayProvider(object, ghidra.service.graph.GraphDisplayProvider):




    def __init__(self): ...



    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getGraphDisplay(self, __a0: bool, __a1: ghidra.util.task.TaskMonitor) -> ghidra.service.graph.GraphDisplay: ...

    def getHelpLocation(self) -> ghidra.util.HelpLocation: ...

    def getName(self) -> unicode: ...

    def getOptions(self) -> ghidra.framework.options.Options: ...

    def getPluginTool(self) -> ghidra.framework.plugintool.PluginTool: ...

    def hashCode(self) -> int: ...

    def initialize(self, __a0: ghidra.framework.plugintool.PluginTool, __a1: ghidra.framework.options.Options) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def optionsChanged(self, __a0: ghidra.framework.options.Options) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def helpLocation(self) -> ghidra.util.HelpLocation: ...

    @property
    def name(self) -> unicode: ...

    @property
    def options(self) -> ghidra.framework.options.Options: ...

    @property
    def pluginTool(self) -> ghidra.framework.plugintool.PluginTool: ...
