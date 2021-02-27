from typing import Iterator
from typing import List
import ghidra.app.plugin.assembler.sleigh.grammars
import ghidra.app.plugin.assembler.sleigh.symbol
import ghidra.app.plugin.processors.sleigh
import ghidra.app.plugin.processors.sleigh.pattern
import java.io
import java.lang
import java.util
import java.util.function


class AssemblyGrammar(ghidra.app.plugin.assembler.sleigh.grammars.AbstractAssemblyGrammar):
    """
    Defines a context free grammar, used to parse mnemonic assembly instructions

     This stores the CFG and the associated semantics for each production. It also has mechanisms for
     tracking "purely recursive" productions. These are productions of the form I = I, and they
     necessarily create ambiguity. Thus, when constructing a parser, it is useful to identify them
     early.
    """





    def __init__(self): ...

    def __iter__(self): ...

    @overload
    def addProduction(self, prod: ghidra.app.plugin.assembler.sleigh.grammars.AssemblyProduction) -> None: ...

    @overload
    def addProduction(self, __a0: ghidra.app.plugin.assembler.sleigh.grammars.AbstractAssemblyProduction) -> None: ...

    @overload
    def addProduction(self, __a0: ghidra.app.plugin.assembler.sleigh.symbol.AssemblyNonTerminal, __a1: ghidra.app.plugin.assembler.sleigh.grammars.AssemblySentential) -> None: ...

    @overload
    def addProduction(self, __a0: ghidra.app.plugin.assembler.sleigh.symbol.AssemblyNonTerminal, __a1: ghidra.app.plugin.assembler.sleigh.grammars.AssemblySentential, __a2: ghidra.app.plugin.processors.sleigh.pattern.DisjointPattern, __a3: ghidra.app.plugin.processors.sleigh.Constructor, __a4: List[object]) -> None: ...

    def combine(self, that: ghidra.app.plugin.assembler.sleigh.grammars.AbstractAssemblyGrammar) -> None: ...

    def contains(self, name: unicode) -> bool:
        """
        Check if the grammar contains any symbol with the given name
        @param name the name to find
        @return true iff a terminal or non-terminal has the given name
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def getNonTerminal(self, name: unicode) -> NT:
        """
        Get the named non-terminal
        @param name the name of the desired non-terminal
        @return the non-terminal, or null if it is not in this grammar
        """
        ...

    def getPureRecursion(self, lhs: ghidra.app.plugin.assembler.sleigh.symbol.AssemblyNonTerminal) -> ghidra.app.plugin.assembler.sleigh.grammars.AssemblyProduction:
        """
        Obtain, if present, the purely recursive production having the given LHS
        @param lhs the left-hand side
        @return the desired production, or null
        """
        ...

    def getPureRecursive(self) -> java.util.Collection:
        """
        Get all productions in the grammar that are purely recursive
        @return
        """
        ...

    def getSemantics(self, prod: ghidra.app.plugin.assembler.sleigh.grammars.AssemblyProduction) -> java.util.Collection:
        """
        Get the semantics associated with a given production
        @param prod the production
        @return all semantics associated with the given production
        """
        ...

    def getStart(self) -> NT:
        """
        Get the start symbol for the grammar
        @return the start symbol
        """
        ...

    def getStartName(self) -> unicode:
        """
        Get the name of the start symbol for the grammar
        @return the name of the start symbol
        """
        ...

    def getTerminal(self, name: unicode) -> ghidra.app.plugin.assembler.sleigh.symbol.AssemblyTerminal:
        """
        Get the named terminal
        @param name the name of the desired terminal
        @return the terminal, or null if it is not in this grammar
        """
        ...

    def hashCode(self) -> int: ...

    def iterator(self) -> Iterator[P]:
        """
        Traverse the productions
        """
        ...

    def nonTerminals(self) -> java.util.Collection:
        """
        Get the non-terminals
        @return
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def print(self, out: java.io.PrintStream) -> None:
        """
        Print the productions of this grammar to the given stream
        @param out the stream
        """
        ...

    @overload
    def productionsOf(self, name: unicode) -> java.util.Collection:
        """
        Get all productions where the left-hand side non-terminal has the given name
        @param name the name of the non-terminal
        @return all productions "defining" the named non-terminal
        """
        ...

    @overload
    def productionsOf(self, nt: ghidra.app.plugin.assembler.sleigh.symbol.AssemblyNonTerminal) -> java.util.Collection:
        """
        Get all productions where the left-hand side is the given non-terminal
        @param nt the non-terminal whose defining productions to find
        @return all productions "defining" the given non-terminal
        """
        ...

    def setStart(self, nt: ghidra.app.plugin.assembler.sleigh.symbol.AssemblyNonTerminal) -> None:
        """
        Change the start symbol for the grammar
        @param nt the new start symbol
        """
        ...

    def setStartName(self, startName: unicode) -> None:
        """
        Change the start symbol for the grammar
        @param startName the name of the new start symbol
        """
        ...

    def spliterator(self) -> java.util.Spliterator: ...

    def terminals(self) -> java.util.Collection:
        """
        Get the terminals
        @return
        """
        ...

    def toString(self) -> unicode: ...

    def verify(self) -> None:
        """
        Check that the grammar is consistent

         The grammar is consistent if every non-terminal appearing in the grammar, also appears as
         the left-hand side of some production. If not, such non-terminals are said to be undefined.
        @throws AssemblyGrammarException the grammar is inconsistent, i.e., contains undefined
                                          non-terminals.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def pureRecursive(self) -> java.util.Collection: ...
