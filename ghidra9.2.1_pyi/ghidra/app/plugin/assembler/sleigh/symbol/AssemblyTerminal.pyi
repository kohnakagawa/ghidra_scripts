import ghidra.app.plugin.assembler.sleigh.grammars
import ghidra.app.plugin.assembler.sleigh.symbol
import java.lang
import java.util


class AssemblyTerminal(ghidra.app.plugin.assembler.sleigh.symbol.AssemblySymbol):
    """
    The type of terminal for an assembly grammar

     Unlike classical parsing, each terminal provides its own tokenizer. If multiple tokenizers yield
     a token, the parser branches, possibly creating multiple, ambiguous trees.
    """





    def __init__(self, name: unicode):
        """
        Construct a terminal having the give name
        @param name
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

    def getSuggestions(self, got: unicode, labels: java.util.Map) -> java.util.Collection:
        """
        Provide a collection of strings that this terminal would have accepted
        @param got the remaining contents of the input buffer
        @param labels the program labels, if applicable
        @return a, possibly empty, collection of suggestions
        """
        ...

    def hashCode(self) -> int: ...

    def match(self, buffer: unicode, pos: int, grammar: ghidra.app.plugin.assembler.sleigh.grammars.AssemblyGrammar, labels: java.util.Map) -> java.util.Collection:
        """
        Attempt to match a token from the input buffer starting at a given position
        @param buffer the input buffer
        @param pos the cursor position in the buffer
        @param grammar the grammar containing this terminal
        @param labels the program labels, if applicable
        @return the matched token, or null
        """
        ...

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
