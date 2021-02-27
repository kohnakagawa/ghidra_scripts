from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format.dwarf4
import ghidra.app.util.bin.format.dwarf4.expression
import java.lang


class DWARFExpression(object):
    """
    A DWARFExpression is an immutable list of DWARFExpressionOperation and some factory methods to read
     an expression from its binary representation.

     Use a DWARFExpressionEvaluator to execute a DWARFExpression.
    """









    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def exprToString(exprBytes: List[int], diea: ghidra.app.util.bin.format.dwarf4.DIEAggregate) -> unicode: ...

    def findOpByOffset(self, offset: long) -> int:
        """
        Finds the index of an {@link DWARFExpressionOperation operation} by its offset
         from the beginning of the expression.
         <p>
        @param offset
        @return -1 if there is no op at the specified offset
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getLastActiveOpIndex(self) -> int:
        """
        Returns the index of the last operation that is not a NOP.
        @return
        """
        ...

    def getOp(self, i: int) -> ghidra.app.util.bin.format.dwarf4.expression.DWARFExpressionOperation: ...

    def getOpCount(self) -> int: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    @staticmethod
    def read(reader: ghidra.app.util.bin.BinaryReader, addrSize: int, dwarf_format: int) -> ghidra.app.util.bin.format.dwarf4.expression.DWARFExpression: ...

    @overload
    @staticmethod
    def read(exprBytes: List[int], addrSize: int, isLittleEndian: bool, dwarf_format: int) -> ghidra.app.util.bin.format.dwarf4.expression.DWARFExpression: ...

    @overload
    def toString(self) -> unicode: ...

    @overload
    def toString(self, caretPosition: int, newlines: bool, offsets: bool) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def lastActiveOpIndex(self) -> int: ...

    @property
    def opCount(self) -> int: ...
