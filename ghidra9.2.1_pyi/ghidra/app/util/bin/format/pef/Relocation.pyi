import ghidra.app.util.bin
import ghidra.app.util.bin.format.pef
import ghidra.app.util.importer
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class Relocation(object, ghidra.app.util.bin.StructConverter):
    """
    The high-order 7 bits for the currently defined relocation opcode values.

     Binary values indicated by "x" are "don't care"
     operands. For example, any combination of the high-order 7 bits that starts
     with two zero bits (00) indicates the RelocBySectDWithSkip instruction.

     Relocation instructions are stored in 2-byte relocation blocks. Most instructions
     take up one block that combines an opcode and related arguments. Instructions
     that are larger than 2 bytes have an opcode and some of the operands in the
     first 2-byte block, with other operands in the following 2-byte blocks. The
     opcode occupies the upper (higher-order) bits of the block that contains it.
     Relocation instructions can be decoded from the high-order 7 bits of their first
     block.

     All currently defined relocation instructions relocate locations as words
     (that is, 4-byte values).
    """

    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    POINTER: ghidra.program.model.data.DataType = pointer
    QWORD: ghidra.program.model.data.DataType = qword
    STRING: ghidra.program.model.data.DataType = string
    UTF16: ghidra.program.model.data.DataType = unicode
    UTF8: ghidra.program.model.data.DataType = string-utf8
    VOID: ghidra.program.model.data.DataType = void
    WORD: ghidra.program.model.data.DataType = word



    def __init__(self): ...



    def apply(self, importState: ghidra.app.util.bin.format.pef.ImportStateCache, relocState: ghidra.app.util.bin.format.pef.RelocationState, header: ghidra.app.util.bin.format.pef.ContainerHeader, program: ghidra.program.model.listing.Program, log: ghidra.app.util.importer.MessageLog, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getOpcode(self) -> int: ...

    def getSizeInBytes(self) -> int: ...

    def hashCode(self) -> int: ...

    def isMatch(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def match(self) -> bool: ...

    @property
    def opcode(self) -> int: ...

    @property
    def sizeInBytes(self) -> int: ...
