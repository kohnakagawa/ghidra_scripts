import ghidra.app.plugin.assembler.sleigh.symbol
import java.io
import java.lang
import java.util


class AssemblyFirstFollow(object):
    """
    A class to compute the first and follow of every non-terminal in a grammar

     See Alfred V. Aho, Monica S. Lam, Ravi Sethi, Jeffrey D. Ullman, Compilers: Principles,
     Techniques,  Tools. Bostom, MA: Pearson, 2007, pp. 220-2.
    """





    def __init__(self, grammar: ghidra.app.plugin.assembler.sleigh.grammars.AbstractAssemblyGrammar):
        """
        Compute the first and follow sets for every non-terminal in the given grammar
        @param grammar the grammar
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFirst(self, nt: ghidra.app.plugin.assembler.sleigh.symbol.AssemblyNonTerminal) -> java.util.Collection:
        """
        Get the first set for a given non-terminal

         That is the set of all terminals, which through some derivation from the given non-terminal,
         can appear first in a sentential form.
        @param nt the non-terminal
        @return the set
        """
        ...

    def getFollow(self, nt: ghidra.app.plugin.assembler.sleigh.symbol.AssemblyNonTerminal) -> java.util.Collection:
        """
        Get the follow set for a given non-terminal

         That is the set of all terminals, which through some derivation from the start symbol, can
         appear immediately after the given non-terminal in a sentential form.
        @param nt the non-terminal
        @return the set
        """
        ...

    def getNullable(self) -> java.util.Collection:
        """
        Get the nullable set

         That is the set of all non-terminals, which through some derivation, can produce epsilon.
        @return the set
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def print(self, out: java.io.PrintStream) -> None:
        """
        For debugging, print out the computed sets to the given stream
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
    def nullable(self) -> java.util.Collection: ...
