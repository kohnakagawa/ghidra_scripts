import ghidra.app.plugin.assembler.sleigh.symbol
import java.lang


class AssemblyExtendedNonTerminal(ghidra.app.plugin.assembler.sleigh.symbol.AssemblyNonTerminal):
    """
    The type of non-terminal for an "extended grammar"
    """





    def __init__(self, start: int, nt: ghidra.app.plugin.assembler.sleigh.symbol.AssemblyNonTerminal, end: int):
        """
        Construct a new extended non terminal, derived from the given non-terminal
        @param start the start state for the extended non-terminal
        @param nt the non-terminal from which the extended non-terminal is derived
        @param end the end state for the extended non-terminal
        """
        ...



    @overload
    def compareTo(self, that: ghidra.app.plugin.assembler.sleigh.symbol.AssemblySymbol) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, that: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def takesOperandIndex(self) -> bool:
        """
        Check if this symbol consumes an operand index of its constructor
        @return true if the symbol represents an operand
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def name(self) -> unicode: ...
