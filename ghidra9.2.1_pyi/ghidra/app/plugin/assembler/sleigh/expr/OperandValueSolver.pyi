import ghidra.app.plugin.assembler.sleigh.expr
import ghidra.app.plugin.assembler.sleigh.sem
import ghidra.app.plugin.processors.sleigh.expression
import java.lang
import java.util


class OperandValueSolver(ghidra.app.plugin.assembler.sleigh.expr.AbstractExpressionSolver):
    """
    Solves expressions of an operand value

     These are a sort of named sub-expression, but they may also specify a shift in encoding.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    def getInstructionLength(self, ov: ghidra.app.plugin.processors.sleigh.expression.OperandValue, res: java.util.Map) -> int: ...

    @overload
    def getInstructionLength(self, __a0: ghidra.app.plugin.processors.sleigh.expression.PatternExpression, __a1: java.util.Map) -> int: ...

    @overload
    def getValue(self, ov: ghidra.app.plugin.processors.sleigh.expression.OperandValue, vals: java.util.Map, res: java.util.Map, cur: ghidra.app.plugin.assembler.sleigh.sem.AssemblyResolvedConstructor) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong: ...

    @overload
    def getValue(self, __a0: ghidra.app.plugin.processors.sleigh.expression.PatternExpression, __a1: java.util.Map, __a2: java.util.Map, __a3: ghidra.app.plugin.assembler.sleigh.sem.AssemblyResolvedConstructor) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def solve(self, ov: ghidra.app.plugin.processors.sleigh.expression.OperandValue, goal: ghidra.app.plugin.assembler.sleigh.expr.MaskedLong, vals: java.util.Map, res: java.util.Map, cur: ghidra.app.plugin.assembler.sleigh.sem.AssemblyResolvedConstructor, hints: java.util.Set, description: unicode) -> ghidra.app.plugin.assembler.sleigh.sem.AssemblyResolution: ...

    @overload
    def solve(self, __a0: ghidra.app.plugin.processors.sleigh.expression.PatternExpression, __a1: ghidra.app.plugin.assembler.sleigh.expr.MaskedLong, __a2: java.util.Map, __a3: java.util.Map, __a4: ghidra.app.plugin.assembler.sleigh.sem.AssemblyResolvedConstructor, __a5: java.util.Set, __a6: unicode) -> ghidra.app.plugin.assembler.sleigh.sem.AssemblyResolution: ...

    def toString(self) -> unicode: ...

    @overload
    def valueForResolution(self, ov: ghidra.app.plugin.processors.sleigh.expression.OperandValue, rc: ghidra.app.plugin.assembler.sleigh.sem.AssemblyResolvedConstructor) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong: ...

    @overload
    def valueForResolution(self, __a0: ghidra.app.plugin.processors.sleigh.expression.PatternExpression, __a1: ghidra.app.plugin.assembler.sleigh.sem.AssemblyResolvedConstructor) -> ghidra.app.plugin.assembler.sleigh.expr.MaskedLong: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
