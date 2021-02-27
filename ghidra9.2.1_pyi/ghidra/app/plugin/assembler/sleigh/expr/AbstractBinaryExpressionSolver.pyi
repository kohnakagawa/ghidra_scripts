import ghidra.app.plugin.assembler.sleigh.expr
import ghidra.app.plugin.assembler.sleigh.sem
import ghidra.app.plugin.processors.sleigh.expression
import java.lang
import java.util


class AbstractBinaryExpressionSolver(ghidra.app.plugin.assembler.sleigh.expr.AbstractExpressionSolver):
    """
    A solver that handles expressions of the form A [OP] B
    """





    def __init__(self, tcls: java.lang.Class): ...



    def compute(self, lval: ghidra.app.plugin.assembler.sleigh.expr.MaskedLong, rval: ghidra.app.plugin.assembler.sleigh.expr.MaskedLong) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Compute the result of applying the operator to the two given values
        @param lval the left-hand-side value
        @param rval the right-hand-side value
        @return the result
        """
        ...

    def computeLeft(self, rval: ghidra.app.plugin.assembler.sleigh.expr.MaskedLong, goal: ghidra.app.plugin.assembler.sleigh.expr.MaskedLong) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Compute the left-hand-side value given that the result and the right are known
        @param rval the right-hand-side value
        @param goal the result
        @return the left-hand-side value solution
        @throws SolverException if the expression cannot be solved
        """
        ...

    def computeRight(self, lval: ghidra.app.plugin.assembler.sleigh.expr.MaskedLong, goal: ghidra.app.plugin.assembler.sleigh.expr.MaskedLong) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong:
        """
        Compute the right-hand-side value given that the result and the left are known

         NOTE: Assumes commutativity by default
        @param lval the left-hand-side value
        @param goal the result
        @return the right-hand-side value solution
        @throws SolverException if the expression cannot be solved
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    def getInstructionLength(self, __a0: ghidra.app.plugin.processors.sleigh.expression.BinaryExpression, __a1: java.util.Map) -> int: ...

    @overload
    def getInstructionLength(self, __a0: ghidra.app.plugin.processors.sleigh.expression.PatternExpression, __a1: java.util.Map) -> int: ...

    @overload
    def getValue(self, __a0: ghidra.app.plugin.processors.sleigh.expression.BinaryExpression, __a1: java.util.Map, __a2: java.util.Map, __a3: ghidra.app.plugin.assembler.sleigh.sem.AssemblyResolvedConstructor) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong: ...

    @overload
    def getValue(self, __a0: ghidra.app.plugin.processors.sleigh.expression.PatternExpression, __a1: java.util.Map, __a2: java.util.Map, __a3: ghidra.app.plugin.assembler.sleigh.sem.AssemblyResolvedConstructor) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def solve(self, __a0: ghidra.app.plugin.processors.sleigh.expression.BinaryExpression, __a1: ghidra.app.plugin.assembler.sleigh.expr.MaskedLong, __a2: java.util.Map, __a3: java.util.Map, __a4: ghidra.app.plugin.assembler.sleigh.sem.AssemblyResolvedConstructor, __a5: java.util.Set, __a6: unicode) -> ghidra.app.plugin.assembler.sleigh.sem.AssemblyResolution: ...

    @overload
    def solve(self, __a0: ghidra.app.plugin.processors.sleigh.expression.PatternExpression, __a1: ghidra.app.plugin.assembler.sleigh.expr.MaskedLong, __a2: java.util.Map, __a3: java.util.Map, __a4: ghidra.app.plugin.assembler.sleigh.sem.AssemblyResolvedConstructor, __a5: java.util.Set, __a6: unicode) -> ghidra.app.plugin.assembler.sleigh.sem.AssemblyResolution: ...

    def toString(self) -> unicode: ...

    @overload
    def valueForResolution(self, __a0: ghidra.app.plugin.processors.sleigh.expression.BinaryExpression, __a1: ghidra.app.plugin.assembler.sleigh.sem.AssemblyResolvedConstructor) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong: ...

    @overload
    def valueForResolution(self, __a0: ghidra.app.plugin.processors.sleigh.expression.PatternExpression, __a1: ghidra.app.plugin.assembler.sleigh.sem.AssemblyResolvedConstructor) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
