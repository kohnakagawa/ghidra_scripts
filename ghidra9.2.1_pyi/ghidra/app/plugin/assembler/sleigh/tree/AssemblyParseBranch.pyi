from typing import Iterator
from typing import List
import ghidra.app.plugin.assembler.sleigh.grammars
import ghidra.app.plugin.assembler.sleigh.symbol
import ghidra.app.plugin.assembler.sleigh.tree
import java.io
import java.lang
import java.util
import java.util.function


class AssemblyParseBranch(ghidra.app.plugin.assembler.sleigh.tree.AssemblyParseTreeNode, java.lang.Iterable):
    """
    A branch in a parse tree, corresponding to the application of a production
    """





    def __init__(self, grammar: ghidra.app.plugin.assembler.sleigh.grammars.AssemblyGrammar, prod: ghidra.app.plugin.assembler.sleigh.grammars.AssemblyProduction):
        """
        Construct a branch from the given grammar and production
        @param grammar the grammar containing the production
        @param prod the production applied to create this branch
        """
        ...

    def __iter__(self): ...

    def addChild(self, child: ghidra.app.plugin.assembler.sleigh.tree.AssemblyParseTreeNode) -> None:
        """
        Prepend a child to this branch
        @param child the child

         Because LR parsers produce rightmost derivations, they necessarily populate the branches
         right to left. During reduction, each child is popped from the stack, traversing them in
         reverse order. This method prepends children so that when reduction is complete, the
         children are aligned to the corresponding symbols from the RHS of the production.
        """
        ...

    def equals(self, obj: object) -> bool: ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

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

    def getProduction(self) -> ghidra.app.plugin.assembler.sleigh.grammars.AssemblyProduction:
        """
        Get the production applied to create this branch
        @return
        """
        ...

    def getSubstitution(self, i: int) -> ghidra.app.plugin.assembler.sleigh.tree.AssemblyParseTreeNode:
        """
        Get the <em>i</em>th child, corresponding to the <em>i</em>th symbol from the RHS
        @param i the position
        @return the child
        """
        ...

    def getSubstitutions(self) -> List[ghidra.app.plugin.assembler.sleigh.tree.AssemblyParseTreeNode]:
        """
        Get the list of children, indexed by corresponding symbol from the RHS
        @return
        """
        ...

    def getSym(self) -> ghidra.app.plugin.assembler.sleigh.symbol.AssemblyNonTerminal: ...

    def hashCode(self) -> int: ...

    def isConstructor(self) -> bool: ...

    def isNumeric(self) -> bool:
        """
        Check if this node yields a numeric value
        @return true if this node yields a numeric value
        """
        ...

    def iterator(self) -> Iterator[ghidra.app.plugin.assembler.sleigh.tree.AssemblyParseTreeNode]: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def print(self, out: java.io.PrintStream) -> None:
        """
        For debugging: Display this parse tree via the given stream
        @param out the stream
        """
        ...

    def spliterator(self) -> java.util.Spliterator: ...

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
    def production(self) -> ghidra.app.plugin.assembler.sleigh.grammars.AssemblyProduction: ...

    @property
    def substitutions(self) -> List[object]: ...

    @property
    def sym(self) -> ghidra.app.plugin.assembler.sleigh.symbol.AssemblyNonTerminal: ...
