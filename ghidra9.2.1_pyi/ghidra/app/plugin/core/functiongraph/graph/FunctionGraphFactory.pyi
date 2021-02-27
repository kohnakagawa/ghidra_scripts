import ghidra.app.plugin.core.functiongraph.mvc
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class FunctionGraphFactory(object):




    def __init__(self): ...



    @staticmethod
    def createClonedGraph(__a0: ghidra.app.plugin.core.functiongraph.mvc.FGData, __a1: ghidra.app.plugin.core.functiongraph.mvc.FGController) -> ghidra.app.plugin.core.functiongraph.mvc.FGData: ...

    @staticmethod
    def createNewGraph(__a0: ghidra.program.model.listing.Function, __a1: ghidra.app.plugin.core.functiongraph.mvc.FGController, __a2: ghidra.program.model.listing.Program, __a3: ghidra.util.task.TaskMonitor) -> ghidra.app.plugin.core.functiongraph.mvc.FGData: ...

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
