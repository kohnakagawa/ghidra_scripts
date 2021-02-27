import ghidra.app.plugin.assembler.sleigh.grammars
import ghidra.app.plugin.assembler.sleigh.symbol
import java.lang
import java.util


class AssemblyEOI(ghidra.app.plugin.assembler.sleigh.symbol.AssemblyTerminal):
    """
    A terminal that accepts the end of input
    """

    EOI: ghidra.app.plugin.assembler.sleigh.symbol.AssemblyEOI = $







    @overload
    def compareTo(self, that: ghidra.app.plugin.assembler.sleigh.symbol.AssemblySymbol) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, that: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode:
        """
        Get the name of this symbol
        @return the name
        """
        ...

    def getSuggestions(self, got: unicode, labels: java.util.Map) -> java.util.Collection: ...

    def hashCode(self) -> int: ...

    def match(self, buffer: unicode, pos: int, grammar: ghidra.app.plugin.assembler.sleigh.grammars.AssemblyGrammar, labels: java.util.Map) -> java.util.Collection: ...

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
