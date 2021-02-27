import ghidra.app.plugin.assembler.sleigh.parse
import ghidra.app.plugin.assembler.sleigh.tree
import java.lang
import java.util


class AssemblyParseMachine(object, java.lang.Comparable):
    """
    A class that implements the LALR(1) parsing algorithm

     Instances of this class store a parse state. In order to work correctly, the class must be
     given a properly-constructed Action/Goto table.

     This implementation is somewhat unconventional. First, instead of strictly tokenizing and then
     parsing, each terminal is given the opportunity to match a token in the input. If none match, it
     results in a syntax error (equivalent to the token type having an empty cell in the classical
     algorithm). If more than one match, the parser branches. Also, because a single cell may also
     contain multiple actions, the parser could branch again. Thus, if a sentence is ambiguous, this
     algorithm will identify all possible parse trees, including ones where the input is tokenized
     differently than in other trees.
    """





    def __init__(self, parser: ghidra.app.plugin.assembler.sleigh.parse.AssemblyParser, input: unicode, pos: int, lastTok: ghidra.app.plugin.assembler.sleigh.tree.AssemblyParseToken, labels: java.util.Map):
        """
        Construct a new parse state
        @param parser the parser driving this machine
        @param input the full input line
        @param pos the position in the line identifying the next characters to parse
        @param labels a map of valid tokens to number for numeric terminals
        """
        ...



    @overload
    def compareTo(self, that: ghidra.app.plugin.assembler.sleigh.parse.AssemblyParseMachine) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def copy(self) -> ghidra.app.plugin.assembler.sleigh.parse.AssemblyParseMachine:
        """
        Duplicate this machine state

         This is used extensively when branching
        @return the duplicate
        """
        ...

    def equals(self, that: object) -> bool: ...

    def exhaust(self) -> java.util.Set:
        """
        Parse (or continue parsing) all possible trees from this machine state
        @return the set of all possible trees and errors
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getTree(self) -> ghidra.app.plugin.assembler.sleigh.tree.AssemblyParseBranch:
        """
        If in the accepted state, get the resulting parse tree for this machine
        @return the parse tree
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def tree(self) -> ghidra.app.plugin.assembler.sleigh.tree.AssemblyParseBranch: ...
