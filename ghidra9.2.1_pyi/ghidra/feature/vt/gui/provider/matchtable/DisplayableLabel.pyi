import docking.widgets.table
import ghidra.feature.vt.gui.provider.matchtable
import ghidra.program.model.symbol
import java.lang


class DisplayableLabel(object, docking.widgets.table.DisplayStringProvider, java.lang.Comparable):




    def __init__(self, __a0: ghidra.program.model.symbol.Symbol): ...



    @overload
    def compareTo(self, __a0: ghidra.feature.vt.gui.provider.matchtable.DisplayableLabel) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDisplayString(self) -> unicode: ...

    def getSymbol(self) -> ghidra.program.model.symbol.Symbol: ...

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
    def displayString(self) -> unicode: ...

    @property
    def symbol(self) -> ghidra.program.model.symbol.Symbol: ...