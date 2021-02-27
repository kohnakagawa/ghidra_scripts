from typing import List
import ghidra.app.plugin.assembler.sleigh.expr
import java.lang
import java.util


class DefaultSolverHint(java.lang.Enum, ghidra.app.plugin.assembler.sleigh.expr.SolverHint):
    GUESSING_CIRCULAR_SHIFT_AMOUNT: ghidra.app.plugin.assembler.sleigh.expr.DefaultSolverHint = GUESSING_CIRCULAR_SHIFT_AMOUNT
    GUESSING_LEFT_SHIFT_AMOUNT: ghidra.app.plugin.assembler.sleigh.expr.DefaultSolverHint = GUESSING_LEFT_SHIFT_AMOUNT
    GUESSING_REPETITION: ghidra.app.plugin.assembler.sleigh.expr.DefaultSolverHint = GUESSING_REPETITION
    GUESSING_RIGHT_SHIFT_AMOUNT: ghidra.app.plugin.assembler.sleigh.expr.DefaultSolverHint = GUESSING_RIGHT_SHIFT_AMOUNT







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDeclaringClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ordinal(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.app.plugin.assembler.sleigh.expr.DefaultSolverHint: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.plugin.assembler.sleigh.expr.DefaultSolverHint]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @staticmethod
    def with(__a0: java.util.Set, __a1: List[ghidra.app.plugin.assembler.sleigh.expr.SolverHint]) -> java.util.Set: ...
