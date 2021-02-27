import ghidra.app.plugin.assembler.sleigh.symbol
import ghidra.app.plugin.assembler.sleigh.util
import java.lang


class TableEntry(ghidra.app.plugin.assembler.sleigh.util.TableEntryKey):
    """
    An entry in a (sparse) LR(0) transition table or LALR(1) action/goto table
    """





    def __init__(self, state: int, sym: ghidra.app.plugin.assembler.sleigh.symbol.AssemblySymbol, value: object):
        """
        Create a new table entry with the given value at the given state and symbol
        @param state the row
        @param sym the column
        @param value the value
        """
        ...



    @overload
    def compareTo(self, that: ghidra.app.plugin.assembler.sleigh.util.TableEntryKey) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, that: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getState(self) -> int:
        """
        Get the state (row) of the key in the table
        @return the state
        """
        ...

    def getSym(self) -> ghidra.app.plugin.assembler.sleigh.symbol.AssemblySymbol:
        """
        Get the symbol (column) of the entry in the table
        @return the symbol
        """
        ...

    def getValue(self) -> object:
        """
        Get the value of the entry
        @return the value
        """
        ...

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
    def value(self) -> object: ...
