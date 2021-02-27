import ghidra.app.plugin.assembler.sleigh.grammars
import ghidra.app.plugin.assembler.sleigh.symbol
import ghidra.app.plugin.assembler.sleigh.tree
import java.lang
import java.util


class AssemblyNumericMapTerminal(ghidra.app.plugin.assembler.sleigh.symbol.AssemblyNumericTerminal):
    """
    A terminal that accepts only a particular set of numeric values, mapping each to another value

     This often used for non-conventional numeric encodings.
    """





    def __init__(self, name: unicode, map: java.util.Map):
        """
        Construct a terminal with the given name, accepting only the keys of a given map
        @param name the name
        @param map the map from display value to token value
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
