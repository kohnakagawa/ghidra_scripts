import ghidra.app.plugin.assembler.sleigh.grammars
import java.io
import java.lang
import java.util


class AssemblyParser(object):
    """
    A class to encapsulate LALR(1) parsing for a given grammar

     This class constructs the Action/Goto table (and all the other trappings) of a LALR(1) parser
     and provides a #parse(String) method to parse actual sentences.

     This implementation is somewhat unconventional in that it permits ambiguous grammars. Instead of
     complaining, it produces the set of all possible parse trees. Of course, this comes at the cost
     of some efficiency.

     See Alfred V. Aho, Monica S. Lam, Ravi Sethi, Jeffrey D. Ullman, Compilers: Principles,
     Techniques,  Tools. Bostom, MA: Pearson, 2007.

     See Jackson, Stephen. LALR(1) Parsing.
     Halifax, Nova Scotia, Canada: Dalhousie University.
     http://web.cs.dal.ca/~sjackson/lalr1.html
    """

    EMPTY_LABELS: java.util.Map = {}



    def __init__(self, grammar: ghidra.app.plugin.assembler.sleigh.grammars.AssemblyGrammar):
        """
        Construct a LALR(1) parser from the given grammar
        @param grammar the grammar
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getGrammar(self) -> ghidra.app.plugin.assembler.sleigh.grammars.AssemblyGrammar:
        """
        Get the grammar used to construct this parser
        @return the grammar
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def parse(self, input: unicode) -> java.lang.Iterable:
        """
        Parse the given sentence
        @param input the sentence to parse
        @return all possible parse trees (and possible errors)
        """
        ...

    @overload
    def parse(self, input: unicode, labels: java.util.Map) -> java.util.Collection:
        """
        Parse the given sentence with the given defined labels
        @param input the sentence to parser
        @param labels a map of label to number substitutions
        @return all possible parse results (trees and errors)

         The tokenizer for numeric terminals also accepts any key in {@code labels.} In such cases,
         the resulting token is assigned the value of the label.
        """
        ...

    def printExtendedFF(self, out: java.io.PrintStream) -> None:
        """
        For debugging
        """
        ...

    def printExtendedGrammar(self, out: java.io.PrintStream) -> None:
        """
        For debugging
        """
        ...

    def printGeneralFF(self, out: java.io.PrintStream) -> None:
        """
        For debugging
        """
        ...

    def printGrammar(self, out: java.io.PrintStream) -> None:
        """
        For debugging
        """
        ...

    def printLR0States(self, out: java.io.PrintStream) -> None:
        """
        For debugging
        """
        ...

    def printLR0TransitionTable(self, out: java.io.PrintStream) -> None:
        """
        For debugging
        """
        ...

    def printMergers(self, out: java.io.PrintStream) -> None:
        """
        For debugging
        """
        ...

    def printParseTable(self, out: java.io.PrintStream) -> None:
        """
        For debugging
        """
        ...

    def printStuff(self, out: java.io.PrintStream) -> None:
        """
        For debugging
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
    def grammar(self) -> ghidra.app.plugin.assembler.sleigh.grammars.AssemblyGrammar: ...
