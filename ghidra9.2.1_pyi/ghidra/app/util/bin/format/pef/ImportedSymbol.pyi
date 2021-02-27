import ghidra.app.util.bin.format.pef
import ghidra.program.model.data
import java.lang


class ImportedSymbol(ghidra.app.util.bin.format.pef.AbstractSymbol):
    SIZEOF: int = 4







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode: ...

    def getSymbolClass(self) -> ghidra.app.util.bin.format.pef.SymbolClass: ...

    def getSymbolNameOffset(self) -> int:
        """
        The offset (in bytes) from the beginning of the loader
         string table to the null-terminated name of the symbol.
        @return offset to the null-terminated name of the symbol
        """
        ...

    def hashCode(self) -> int: ...

    def isWeak(self) -> bool:
        """
        The imported symbol does not have to
         be present at fragment preparation time in
         order for execution to continue.
        @return if the symbol is weak
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def name(self) -> unicode: ...

    @property
    def symbolClass(self) -> ghidra.app.util.bin.format.pef.SymbolClass: ...

    @property
    def symbolNameOffset(self) -> int: ...

    @property
    def weak(self) -> bool: ...
