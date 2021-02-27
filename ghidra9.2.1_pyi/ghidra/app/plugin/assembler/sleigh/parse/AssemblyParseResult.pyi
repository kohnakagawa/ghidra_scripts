import ghidra.app.plugin.assembler.sleigh.parse
import ghidra.app.plugin.assembler.sleigh.tree
import java.lang
import java.util


class AssemblyParseResult(object, java.lang.Comparable):
    """
    A result of parsing a sentence

     If the sentence was accepted, this yields a parse tree. If not, this describes the error and
     provides suggestions to correct the error.
    """





    def __init__(self): ...



    @staticmethod
    def accept(tree: ghidra.app.plugin.assembler.sleigh.tree.AssemblyParseBranch) -> ghidra.app.plugin.assembler.sleigh.parse.AssemblyParseAcceptResult:
        """
        Construct a successful parse result
        @param tree the tree output by the parser
        """
        ...

    @overload
    def compareTo(self, that: ghidra.app.plugin.assembler.sleigh.parse.AssemblyParseResult) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def error(got: unicode, suggestions: java.util.Set) -> ghidra.app.plugin.assembler.sleigh.parse.AssemblyParseErrorResult:
        """
        Construct an error parse result
        @param got the input buffer when the error occurred
        @param suggestions a subset of strings that would have allowed parsing to proceed
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isError(self) -> bool:
        """
        Check if the parse result is successful or an error
        @return true if the result describes an error
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
