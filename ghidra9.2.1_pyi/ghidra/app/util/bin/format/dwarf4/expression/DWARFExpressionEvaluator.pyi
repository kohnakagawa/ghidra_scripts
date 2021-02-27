from typing import List
import ghidra.app.util.bin.format.dwarf4
import ghidra.app.util.bin.format.dwarf4.expression
import ghidra.program.model.lang
import java.lang


class DWARFExpressionEvaluator(object):
    """
    Evaluates a subset of DWARF expression opcodes.

     Limitations:
     Can not access memory during evaluation of expressions.
     Some opcodes must be the last operation in the expression (deref, regX)
     Can only specify offset from register for framebase and stack relative

     Result can be a numeric value (ie. static address) or a register 'name' or a stack based offset.

    """





    def __init__(self, pointerSize: int, isLittleEndian: bool, dwarfFormat: int, registerMappings: ghidra.app.util.bin.format.dwarf4.next.DWARFRegisterMappings): ...



    @staticmethod
    def create(die: ghidra.app.util.bin.format.dwarf4.DebugInfoEntry) -> ghidra.app.util.bin.format.dwarf4.expression.DWARFExpressionEvaluator: ...

    def equals(self, __a0: object) -> bool: ...

    @overload
    def evaluate(self, exprBytes: List[int]) -> ghidra.app.util.bin.format.dwarf4.expression.DWARFExpressionResult: ...

    @overload
    def evaluate(self, _expr: ghidra.app.util.bin.format.dwarf4.expression.DWARFExpression) -> ghidra.app.util.bin.format.dwarf4.expression.DWARFExpressionResult: ...

    @overload
    def evaluate(self, _expr: ghidra.app.util.bin.format.dwarf4.expression.DWARFExpression, stackArgs: List[long]) -> ghidra.app.util.bin.format.dwarf4.expression.DWARFExpressionResult:
        """
        @param _expr
        @param stackArgs - pushed 0..N, so stackArgs[0] will be deepest, stackArgs[N] will be topmost.
        @return
        @throws DWARFExpressionException
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getLastRegister(self) -> ghidra.program.model.lang.Register: ...

    def getMaxStepCount(self) -> int: ...

    def getRawLastRegister(self) -> int: ...

    def getStackAsString(self) -> unicode: ...

    def getTerminalRegister(self) -> ghidra.program.model.lang.Register:
        """
        Returns the {@link Register register} that holds the contents of the object that the
         {@link DWARFExpression expression} points to.
         <p>
         Note, you should check {@link #isDeref()} to see if the register is just a pointer
         to the object instead of the object itself.
         <p>
        @return
        """
        ...

    def hashCode(self) -> int: ...

    def isDeref(self) -> bool: ...

    def isDwarfStackValue(self) -> bool: ...

    def isRegisterLocation(self) -> bool: ...

    def isStackRelative(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def peek(self) -> long: ...

    def pop(self) -> long: ...

    def push(self, l: long) -> None: ...

    def readExpr(self, exprBytes: List[int]) -> ghidra.app.util.bin.format.dwarf4.expression.DWARFExpression: ...

    def setFrameBase(self, fb: long) -> None: ...

    def setMaxStepCount(self, maxStepCount: int) -> None: ...

    def toString(self) -> unicode: ...

    def useUnknownRegister(self) -> bool: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def deref(self) -> bool: ...

    @property
    def dwarfStackValue(self) -> bool: ...

    @property
    def frameBase(self) -> None: ...  # No getter available.

    @frameBase.setter
    def frameBase(self, value: long) -> None: ...

    @property
    def lastRegister(self) -> ghidra.program.model.lang.Register: ...

    @property
    def maxStepCount(self) -> int: ...

    @maxStepCount.setter
    def maxStepCount(self, value: int) -> None: ...

    @property
    def rawLastRegister(self) -> int: ...

    @property
    def registerLocation(self) -> bool: ...

    @property
    def stackAsString(self) -> unicode: ...

    @property
    def stackRelative(self) -> bool: ...

    @property
    def terminalRegister(self) -> ghidra.program.model.lang.Register: ...
