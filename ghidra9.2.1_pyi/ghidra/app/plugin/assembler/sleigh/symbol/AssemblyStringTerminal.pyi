import ghidra.app.plugin.assembler.sleigh.grammars
import ghidra.app.plugin.assembler.sleigh.symbol
import java.lang
import java.util


class AssemblyStringTerminal(ghidra.app.plugin.assembler.sleigh.symbol.AssemblyTerminal):
    """
    A terminal that accepts only a particular string
    """





    def __init__(self, str: unicode):
        """
        Construct a terminal that accepts only the given string
        @param str the string to accept
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

    def getSuggestions(self, got: unicode, labels: java.util.Map) -> java.util.Collection: ...

    def hashCode(self) -> int: ...

    def match(self, buffer: unicode, pos: int, grammar: ghidra.app.plugin.assembler.sleigh.grammars.AssemblyGrammar, labels: java.util.Map) -> java.util.Collection: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def takesOperandIndex(self) -> bool: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
