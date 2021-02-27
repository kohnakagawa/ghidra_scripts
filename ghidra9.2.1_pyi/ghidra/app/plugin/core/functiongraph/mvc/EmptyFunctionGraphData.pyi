import ghidra.app.plugin.core.functiongraph.graph
import ghidra.app.plugin.core.functiongraph.mvc
import ghidra.program.model.listing
import ghidra.program.util
import java.lang


class EmptyFunctionGraphData(ghidra.app.plugin.core.functiongraph.mvc.FGData):




    def __init__(self, __a0: unicode): ...



    def containsLocation(self, __a0: ghidra.program.util.ProgramLocation) -> bool: ...

    def containsSelection(self, __a0: ghidra.program.util.ProgramSelection) -> bool: ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFunction(self) -> ghidra.program.model.listing.Function: ...

    def getFunctionGraph(self) -> ghidra.app.plugin.core.functiongraph.graph.FunctionGraph: ...

    def getMessage(self) -> unicode: ...

    def getOptions(self) -> ghidra.app.plugin.core.functiongraph.mvc.FunctionGraphOptions: ...

    def hasResults(self) -> bool: ...

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

    @property
    def functionGraph(self) -> ghidra.app.plugin.core.functiongraph.graph.FunctionGraph: ...

    @property
    def options(self) -> ghidra.app.plugin.core.functiongraph.mvc.FunctionGraphOptions: ...