from typing import List
import ghidra.app.util.bin.format.dwarf4.expression
import java.lang


class DWARFExpressionOperandType(java.lang.Enum):
    ADDR: ghidra.app.util.bin.format.dwarf4.expression.DWARFExpressionOperandType = ADDR
    DWARF_INT: ghidra.app.util.bin.format.dwarf4.expression.DWARFExpressionOperandType = DWARF_INT
    SIZED_BLOB: ghidra.app.util.bin.format.dwarf4.expression.DWARFExpressionOperandType = SIZED_BLOB
    S_BYTE: ghidra.app.util.bin.format.dwarf4.expression.DWARFExpressionOperandType = S_BYTE
    S_INT: ghidra.app.util.bin.format.dwarf4.expression.DWARFExpressionOperandType = S_INT
    S_LEB128: ghidra.app.util.bin.format.dwarf4.expression.DWARFExpressionOperandType = S_LEB128
    S_LONG: ghidra.app.util.bin.format.dwarf4.expression.DWARFExpressionOperandType = S_LONG
    S_SHORT: ghidra.app.util.bin.format.dwarf4.expression.DWARFExpressionOperandType = S_SHORT
    U_BYTE: ghidra.app.util.bin.format.dwarf4.expression.DWARFExpressionOperandType = U_BYTE
    U_INT: ghidra.app.util.bin.format.dwarf4.expression.DWARFExpressionOperandType = U_INT
    U_LEB128: ghidra.app.util.bin.format.dwarf4.expression.DWARFExpressionOperandType = U_LEB128
    U_LONG: ghidra.app.util.bin.format.dwarf4.expression.DWARFExpressionOperandType = U_LONG
    U_SHORT: ghidra.app.util.bin.format.dwarf4.expression.DWARFExpressionOperandType = U_SHORT







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
    def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.dwarf4.expression.DWARFExpressionOperandType: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def valueToString(__a0: long, __a1: ghidra.app.util.bin.format.dwarf4.expression.DWARFExpressionOperandType) -> unicode: ...

    @staticmethod
    def values() -> List[ghidra.app.util.bin.format.dwarf4.expression.DWARFExpressionOperandType]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
