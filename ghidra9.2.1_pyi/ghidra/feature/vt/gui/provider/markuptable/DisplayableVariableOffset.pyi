import ghidra.feature.vt.gui.editors
import ghidra.program.model.address
import java.lang


class DisplayableVariableOffset(object, ghidra.feature.vt.gui.editors.DisplayableOffset):
    NO_OFFSET: unicode = u'No Offset'



    def __init__(self, __a0: ghidra.program.model.listing.Function, __a1: ghidra.program.model.address.Address): ...



    @overload
    def compareTo(self, __a0: ghidra.feature.vt.gui.editors.DisplayableOffset) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getAddress(self) -> ghidra.program.model.address.Address: ...

    def getClass(self) -> java.lang.Class: ...

    def getDisplayString(self) -> unicode: ...

    def getOffset(self) -> long: ...

    def getOffsetAsBigInteger(self) -> long: ...

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
    def address(self) -> ghidra.program.model.address.Address: ...

    @property
    def displayString(self) -> unicode: ...

    @property
    def offset(self) -> long: ...

    @property
    def offsetAsBigInteger(self) -> long: ...
