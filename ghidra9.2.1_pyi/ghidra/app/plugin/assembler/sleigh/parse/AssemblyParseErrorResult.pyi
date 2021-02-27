import ghidra.app.plugin.assembler.sleigh.parse
import ghidra.app.plugin.assembler.sleigh.tree
import java.lang
import java.util


class AssemblyParseErrorResult(ghidra.app.plugin.assembler.sleigh.parse.AssemblyParseResult):
    """
    An unsuccessful result from parsing
    """









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

    def describeError(self) -> unicode:
        """
        Get a description of the error
        @return a description
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def error(got: unicode, suggestions: java.util.Set) -> ghidra.app.plugin.assembler.sleigh.parse.AssemblyParseErrorResult:
        """
        Construct an error parse result
        @param got the input buffer when the error occurred
        @param suggestions a subset of strings that would have allowed parsing to proceed
        """
        ...

    def getBuffer(self) -> unicode:
        """
        Get the leftover contents of the input buffer when the error occurred
        @return
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getSuggestions(self) -> java.util.Set:
        """
        Get a set of suggested tokens that would have allowed parsing to continue
        @return the set
        """
        ...

    def hashCode(self) -> int: ...

    def isError(self) -> bool: ...

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
    def buffer(self) -> unicode: ...

    @property
    def suggestions(self) -> java.util.Set: ...
