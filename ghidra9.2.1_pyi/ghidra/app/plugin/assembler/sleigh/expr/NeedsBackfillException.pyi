from typing import List
import ghidra.app.plugin.assembler.sleigh.expr
import java.io
import java.lang


class NeedsBackfillException(ghidra.app.plugin.assembler.sleigh.expr.SolverException):
    """
    An exception to indicate that the solution of an expression is not yet known

     Furthermore, it cannot be determined whether or not the expression is even solvable. When this
     exception is thrown, a backfill record is placed on the encoded resolution indicating that
     resolver must attempt to solve the expression again, once the encoding is otherwise complete.
     This is needed, most notably, when an encoding depends on the address of the next
     instruction, because the length of the current instruction is not known until resolution has
     finished.

     Backfill becomes a possibility when an expression depends on a symbol that is not (yet) defined.
     Thus, as a matter of good record keeping, the exception takes the name of the missing symbol.
    """





    def __init__(self, symbol: unicode):
        """
        Construct a backfill exception, resulting from the given missing symbol name
        @param symbol the missing symbol name
        """
        ...



    def addSuppressed(self, __a0: java.lang.Throwable) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def fillInStackTrace(self) -> java.lang.Throwable: ...

    def getCause(self) -> java.lang.Throwable: ...

    def getClass(self) -> java.lang.Class: ...

    def getLocalizedMessage(self) -> unicode: ...

    def getMessage(self) -> unicode: ...

    def getStackTrace(self) -> List[java.lang.StackTraceElement]: ...

    def getSuppressed(self) -> List[java.lang.Throwable]: ...

    def getSymbol(self) -> unicode:
        """
        Retrieve the missing symbol name from the original solution attempt
        @return the missing symbol name
        """
        ...

    def hashCode(self) -> int: ...

    def initCause(self, __a0: java.lang.Throwable) -> java.lang.Throwable: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def printStackTrace(self) -> None: ...

    @overload
    def printStackTrace(self, __a0: java.io.PrintStream) -> None: ...

    @overload
    def printStackTrace(self, __a0: java.io.PrintWriter) -> None: ...

    def setStackTrace(self, __a0: List[java.lang.StackTraceElement]) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def symbol(self) -> unicode: ...
