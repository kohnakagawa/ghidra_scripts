import ghidra.app.plugin.languages.sleigh
import ghidra.app.plugin.processors.sleigh
import ghidra.app.plugin.processors.sleigh.pattern
import ghidra.app.plugin.processors.sleigh.symbol
import ghidra.app.plugin.processors.sleigh.template
import java.lang


class PcodeOpEntryVisitor(ghidra.app.plugin.languages.sleigh.VisitorResults, object):
    """
    An interface for visiting Pcode operations in a SLEIGH language
    """

    CONTINUE: int = 0
    FINISHED: int = 1
    TERMINATE: int = 2







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    def visit(self, subtable: ghidra.app.plugin.processors.sleigh.symbol.SubtableSymbol, pattern: ghidra.app.plugin.processors.sleigh.pattern.DisjointPattern, cons: ghidra.app.plugin.processors.sleigh.Constructor, op: ghidra.app.plugin.processors.sleigh.template.OpTpl) -> int:
        """
        Callback to visit a Pcode operation
        @param subtable the table containing the constructor
        @param pattern the pattern corresponding to the constructor
        @param cons the constructor generating the Pcode operation
        @param op the Pcode operation
        @return a value from {@link VisitorResults}
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
