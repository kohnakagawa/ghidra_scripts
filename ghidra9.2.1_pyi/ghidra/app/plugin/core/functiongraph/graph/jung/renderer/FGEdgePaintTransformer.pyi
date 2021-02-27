import com.google.common.base
import ghidra.app.plugin.core.functiongraph.graph
import java.awt
import java.lang


class FGEdgePaintTransformer(object, com.google.common.base.Function):




    def __init__(self, __a0: ghidra.app.plugin.core.functiongraph.mvc.FunctionGraphOptions): ...



    @overload
    def apply(self, __a0: ghidra.app.plugin.core.functiongraph.graph.FGEdge) -> java.awt.Paint: ...

    @overload
    def apply(self, __a0: object) -> object: ...

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
