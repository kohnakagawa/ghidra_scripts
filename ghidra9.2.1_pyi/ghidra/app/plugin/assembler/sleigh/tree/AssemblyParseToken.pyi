import ghidra.app.plugin.assembler.sleigh.grammars
import ghidra.app.plugin.assembler.sleigh.symbol
import ghidra.app.plugin.assembler.sleigh.tree
import java.io
import java.lang


class AssemblyParseToken(ghidra.app.plugin.assembler.sleigh.tree.AssemblyParseTreeNode):
    """
    A string token
    """





    def __init__(self, grammar: ghidra.app.plugin.assembler.sleigh.grammars.AssemblyGrammar, term: ghidra.app.plugin.assembler.sleigh.symbol.AssemblyTerminal, str: unicode):
        """
        Construct a new token having the given string value
        @param grammar the grammar containing the terminal
        @param term the terminal that matched this token
        @param str the portion of the input comprising this token
        """
        ...



    def equals(self, obj: object) -> bool: ...

    def generateString(self) -> unicode: ...

    def getClass(self) -> java.lang.Class: ...

    def getGrammar(self) -> ghidra.app.plugin.assembler.sleigh.grammars.AssemblyGrammar:
        """
        Get the grammar used to parse the tree
        @return the grammar
        """
        ...

    def getParent(self) -> ghidra.app.plugin.assembler.sleigh.tree.AssemblyParseBranch:
        """
        Get the branch which contains this node
        @return
        """
        ...

    def getString(self) -> unicode:
        """
        Get the portion of the input comprising the token
        @return the string value
        """
        ...

    def getSym(self) -> ghidra.app.plugin.assembler.sleigh.symbol.AssemblyTerminal: ...

    def hashCode(self) -> int: ...

    def isConstructor(self) -> bool:
        """
        Check if this node yields a subconstructor resolution
        @return true if this node yields a subconstructor resolution
        """
        ...

    def isNumeric(self) -> bool:
        """
        Check if this node yields a numeric value
        @return true if this node yields a numeric value
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def print(self, out: java.io.PrintStream) -> None:
        """
        For debugging: Display this parse tree via the given stream
        @param out the stream
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
    def string(self) -> unicode: ...

    @property
    def sym(self) -> ghidra.app.plugin.assembler.sleigh.symbol.AssemblyTerminal: ...
