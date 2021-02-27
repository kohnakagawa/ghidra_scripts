import ghidra.app.plugin.assembler.sleigh.symbol
import java.lang


class AssemblySymbol(object, java.lang.Comparable):
    """
    A symbol in a context-free grammar

     Symbols can be either terminals or non-terminals. Non-terminals must have a defining production,
     i.e., it must appear as the left-hand side of some production in the grammar.

     Traditionally, when displayed, non-terminals should be immediately distinguishable from
     terminals. In classic CS literature, this usually means non-terminals are in CAPS, and terminals
     are in lower-case. Because the assembler doesn't control the names provided by SLEIGH, we
     surround non-terminals in [brackets].
    """





    def __init__(self, name: unicode):
        """
        Construct a new symbol with the given name
        @param name the name
        """
        ...



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
