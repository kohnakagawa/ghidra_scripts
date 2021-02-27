from typing import Iterator
import ghidra.app.plugin.assembler.sleigh.grammars
import ghidra.app.plugin.assembler.sleigh.symbol
import java.io
import java.lang
import java.util
import java.util.function


class AbstractAssemblyGrammar(object, java.lang.Iterable):
    """
    Defines a context-free grammar, usually for the purpose of parsing mnemonic assembly instructions

     As in classic computer science, a CFG consists of productions of non-terminals and terminals.
     The left-hand side of the a production must be a single non-terminal, but the right-hand side
     may be any string of symbols. To avoid overloading the term "String," here we call it a
     "Sentential."

     To define a grammar, simply construct an appropriate subclass (probably AssemblyGrammar)
     and call #addProduction(AbstractAssemblyProduction) or
     #addProduction(AssemblyNonTerminal, AssemblySentential). The grammar object will collect
     the non-terminals and terminals.

     By default, the start symbol is taken from the left-hand side of the first production added to
     the grammar.
    """





    def __init__(self): ...

    def __iter__(self): ...

    @overload
    def addProduction(self, __a0: ghidra.app.plugin.assembler.sleigh.grammars.AbstractAssemblyProduction) -> None: ...

    @overload
    def addProduction(self, __a0: ghidra.app.plugin.assembler.sleigh.symbol.AssemblyNonTerminal, __a1: ghidra.app.plugin.assembler.sleigh.grammars.AssemblySentential) -> None: ...

    def combine(self, that: ghidra.app.plugin.assembler.sleigh.grammars.AbstractAssemblyGrammar) -> None:
        """
        Add all the productions of a given grammar to this one
        @param that the grammar whose productions to add
        """
        ...

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
    def start(self) -> ghidra.app.plugin.assembler.sleigh.symbol.AssemblyNonTerminal: ...

    @start.setter
    def start(self, value: ghidra.app.plugin.assembler.sleigh.symbol.AssemblyNonTerminal) -> None: ...

    @property
    def startName(self) -> unicode: ...

    @startName.setter
    def startName(self, value: unicode) -> None: ...
