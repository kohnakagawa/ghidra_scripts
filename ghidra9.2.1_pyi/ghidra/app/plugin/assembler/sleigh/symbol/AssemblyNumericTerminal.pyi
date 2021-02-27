import ghidra.app.plugin.assembler.sleigh.grammars
import ghidra.app.plugin.assembler.sleigh.symbol
import ghidra.app.plugin.assembler.sleigh.tree
import java.lang
import java.util


class AssemblyNumericTerminal(ghidra.app.plugin.assembler.sleigh.symbol.AssemblyTerminal):
    """
    A terminal that accepts any numeric value or program label

     The literal may take any form accepted by UNIX strtol() with base=0. By default, the literal is
     interpreted in base 10, but it may be prefixed such that it's interpreted in an alternative
     base. With the prefix '0x', it is interpreted in hexadecimal. With the prefix '0', it is
     interpreted in octal.
    """

    PREFIX_HEX: unicode = u'0x'
    PREFIX_OCT: unicode = u'0'



    def __init__(self, name: unicode, bitsize: int):
        """
        Construct a terminal with the given name, accepting any numeric value or program label
        @param name the name
        """
        ...



    @overload
    def compareTo(self, that: ghidra.app.plugin.assembler.sleigh.symbol.AssemblySymbol) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, that: object) -> bool: ...

    def getBitSize(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode:
        """
        Get the name of this symbol
        @return the name
        """
        ...

    def getSuggestions(self, got: unicode, labels: java.util.Map) -> java.util.Collection: ...

    def hashCode(self) -> int: ...

    @overload
    def match(self, buffer: unicode) -> ghidra.app.plugin.assembler.sleigh.tree.AssemblyParseNumericToken:
        """
        This is only a convenience for testing

         Please use {@link #match(String, int, AssemblyGrammar, Map) match(String, int, AssemblyGrammar, Map&lt;String, Long&gt;)}.
        @param buffer the input buffer
        @return the parsed token
        """
        ...

    @overload
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

    @property
    def bitSize(self) -> int: ...
