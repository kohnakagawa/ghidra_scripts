import ghidra.app.plugin.assembler.sleigh.parse
import ghidra.app.plugin.assembler.sleigh.tree
import java.lang
import java.util


class AssemblyParseAcceptResult(ghidra.app.plugin.assembler.sleigh.parse.AssemblyParseResult):
    """
    A successful result from parsing
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

    def getTree(self) -> ghidra.app.plugin.assembler.sleigh.tree.AssemblyParseBranch:
        """
        Get the tree
        @return the tree
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
    def tree(self) -> ghidra.app.plugin.assembler.sleigh.tree.AssemblyParseBranch: ...
