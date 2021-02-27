import docking.widgets.table
import ghidra.feature.vt.api.util
import ghidra.program.model.listing
import ghidra.util.classfinder
import java.lang


class Stringable(object, ghidra.util.classfinder.ExtensionPoint, docking.widgets.table.DisplayStringProvider):
    DELIMITER: unicode = u'\t'
    DOUBLE_DELIMITER: unicode = u'\n'







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDisplayString(self) -> unicode: ...

    @staticmethod
    def getString(__a0: ghidra.feature.vt.api.util.Stringable, __a1: ghidra.program.model.listing.Program) -> unicode: ...

    @staticmethod
    def getStringable(__a0: unicode, __a1: ghidra.program.model.listing.Program) -> ghidra.feature.vt.api.util.Stringable: ...

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
