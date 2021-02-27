from typing import List
import ghidra.app.util.bin.format.pdb2.pdbreader
import ghidra.app.util.bin.format.pdb2.pdbreader.symbol
import java.lang


class InstructionAnnotation(ghidra.app.util.bin.format.pdb2.pdbreader.AbstractParsableItem):





    class Opcode(java.lang.Enum):
        CHANGE_CODE_LENGTH: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.InstructionAnnotation.Opcode = CodeLength
        CHANGE_CODE_LENGTH_AND_CODE_OFFSET: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.InstructionAnnotation.Opcode = CodeLengthAndCodeOffset
        CHANGE_CODE_OFFSET: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.InstructionAnnotation.Opcode = CodeOffset
        CHANGE_CODE_OFFSET_AND_LINE_OFFSET: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.InstructionAnnotation.Opcode = CodeOffsetAndLineOffset
        CHANGE_CODE_OFFSET_BASE: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.InstructionAnnotation.Opcode = CodeOffsetBase
        CHANGE_COLUMN_END: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.InstructionAnnotation.Opcode = ColumnEnd
        CHANGE_COLUMN_END_DELTA: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.InstructionAnnotation.Opcode = ColumnEndDelta
        CHANGE_COLUMN_START: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.InstructionAnnotation.Opcode = ColumnStart
        CHANGE_FILE: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.InstructionAnnotation.Opcode = File
        CHANGE_LINE_END_DELTA: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.InstructionAnnotation.Opcode = LineEndDelta
        CHANGE_LINE_OFFSET: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.InstructionAnnotation.Opcode = LineOffset
        CHANGE_RANGE_KIND: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.InstructionAnnotation.Opcode = RangeKind
        CODE_OFFSET: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.InstructionAnnotation.Opcode = Offset
        INVALID: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.InstructionAnnotation.Opcode = Illegal
        label: unicode
        value: int







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        @staticmethod
        def fromValue(__a0: int) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.InstructionAnnotation.Opcode: ...

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
        def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.InstructionAnnotation.Opcode: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.app.util.bin.format.pdb2.pdbreader.symbol.InstructionAnnotation.Opcode]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...



    def __init__(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.PdbByteReader): ...



    def emit(self, __a0: java.lang.StringBuilder) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getInstructionCode(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.InstructionAnnotation.Opcode: ...

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

    @property
    def instructionCode(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.InstructionAnnotation.Opcode: ...
