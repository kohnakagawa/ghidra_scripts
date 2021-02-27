import ghidra.app.plugin.assembler.sleigh.grammars
import ghidra.app.plugin.assembler.sleigh.symbol
import ghidra.app.plugin.assembler.sleigh.tree
import java.io
import java.lang


class AssemblyParseTreeNode(object):
    """
    A node in a parse tree
    """





    def __init__(self, grammar: ghidra.app.plugin.assembler.sleigh.grammars.AssemblyGrammar):
        """
        Construct a node for a tree parsed by the given grammar
        @param grammar the grammar
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def generateString(self) -> unicode:
        """
        Generate the string that this node parsed
        @return the string
        """
        ...

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

    def getSym(self) -> ghidra.app.plugin.assembler.sleigh.symbol.AssemblySymbol:
        """
        Get the symbol for which this node is substituted

         For a branch, this is the LHS of the corresponding production. For a token, this is the
         terminal whose tokenizer matched it.
        @return the symbol
        """
        ...

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
    def constructor(self) -> bool: ...

    @property
    def grammar(self) -> ghidra.app.plugin.assembler.sleigh.grammars.AssemblyGrammar: ...

    @property
    def numeric(self) -> bool: ...

    @property
    def parent(self) -> ghidra.app.plugin.assembler.sleigh.tree.AssemblyParseBranch: ...

    @property
    def sym(self) -> ghidra.app.plugin.assembler.sleigh.symbol.AssemblySymbol: ...
