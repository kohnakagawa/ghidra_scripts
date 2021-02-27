from typing import List
import ghidra.app.plugin.assembler.sleigh.expr
import java.lang
import java.util


class SolverHint(object):
    """
    A type for solver hints

     Hints inform "sub-"solvers of the techniques already being applied by the calling solvers. This
     helps prevent situations where, e.g., two multiplication solvers (applied to repeated or nested
     multiplication) both attempt to synthesize new goals for repetition. This sort of expression is
     common when decoding immediates in the AArch64 specification.

     Using an interface implemented by an enumeration (instead of just using the enumeration directly)
     eases expansion by extension without modifying the core code.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

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

    @staticmethod
    def with(set: java.util.Set, plus: List[ghidra.app.plugin.assembler.sleigh.expr.SolverHint]) -> java.util.Set: ...
