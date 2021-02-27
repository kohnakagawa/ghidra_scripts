import ghidra.app.plugin.core.functioncompare
import ghidra.program.model.listing
import java.lang
import java.util


class FunctionComparison(object, java.lang.Comparable):




    def __init__(self): ...



    def addTarget(self, __a0: ghidra.program.model.listing.Function) -> None: ...

    def addTargets(self, __a0: java.util.Set) -> None: ...

    def clearTargets(self) -> None: ...

    @overload
    def compareTo(self, __a0: ghidra.app.plugin.core.functioncompare.FunctionComparison) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getSource(self) -> ghidra.program.model.listing.Function: ...

    def getTargets(self) -> java.util.Set: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeTarget(self, __a0: ghidra.program.model.listing.Function) -> None: ...

    def setSource(self, __a0: ghidra.program.model.listing.Function) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def source(self) -> ghidra.program.model.listing.Function: ...

    @source.setter
    def source(self, value: ghidra.program.model.listing.Function) -> None: ...

    @property
    def targets(self) -> java.util.Set: ...
