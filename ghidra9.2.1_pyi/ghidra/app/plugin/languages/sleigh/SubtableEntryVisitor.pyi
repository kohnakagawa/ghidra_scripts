import ghidra.app.plugin.languages.sleigh
import ghidra.app.plugin.processors.sleigh
import ghidra.app.plugin.processors.sleigh.pattern
import java.lang


class SubtableEntryVisitor(ghidra.app.plugin.languages.sleigh.VisitorResults, object):
    """
    An interface for visiting constructors in a SLEIGH subtable
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

    def visit(self, pattern: ghidra.app.plugin.processors.sleigh.pattern.DisjointPattern, cons: ghidra.app.plugin.processors.sleigh.Constructor) -> int:
        """
        Callback to visit a constructor
        @param pattern the pattern corresponding to the constructor
        @param cons the constructor
        @return a value from {@link VisitorResults}
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
