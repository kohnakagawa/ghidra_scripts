from typing import List
import ghidra.app.util.bin.format.dwarf.line
import java.lang


class StatementProgramPrologue(object):
    PRE_PROLOGUE_LEN: int = 10
    TOTAL_LENGTH_FIELD_LEN: int = 4



    def __init__(self, reader: ghidra.app.util.bin.BinaryReader): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDirectoryByIndex(self, directoryIndex: ghidra.app.util.bin.format.dwarf.line.LEB128) -> unicode:
        """
        The directory index represents an entry in the
         include directories section. If the directoryIndex
         is LEB128(0), then the file was found in the current
         directory.
        @param directoryIndex the directory index
        @return the directory or current directory
        """
        ...

    def getFileNameByIndex(self, fileIndex: int) -> ghidra.app.util.bin.format.dwarf.line.FileEntry:
        """
        Returns the file entry at the given index.
        @param fileIndex the file index
        @return the file entry at the given index
        """
        ...

    def getFileNames(self) -> List[ghidra.app.util.bin.format.dwarf.line.FileEntry]:
        """
        @return an entry for each source file that contributed to the statement
        """
        ...

    def getIncludeDirectories(self) -> List[unicode]:
        """
        @return each path that was searched for included source files
        """
        ...

    def getLineBase(self) -> int:
        """
        Returns the line base value.
         This parameter affects the meaning of the special opcodes. See below.
        @return the line base value
        """
        ...

    def getLineRange(self) -> int:
        """
        Returns the line range value.
         This parameter affects the meaning of the special opcodes. See below.
        @return the line range value
        """
        ...

    def getMinimumInstructionLength(self) -> int:
        """
        Returns the size in bytes of the smallest target machine instruction.
         Statement program opcodes that alter the address register first
         multiply their operands by this value.
        @return the size in bytes of the smallest target machine instruction
        """
        ...

    def getOpcodeBase(self) -> int:
        """
        Returns the number assigned to the first special opcode.
        @return the number assigned to the first special opcode
        """
        ...

    def getPrologueLength(self) -> int:
        """
        Returns the number of bytes following the prologue_length field to the
         beginning of the first byte of the statement program itself.
        @return the number of bytes following the prologue_length
        """
        ...

    def getStandardOpcodeLengths(self) -> List[int]:
        """
        return the array for each of the standard opcodes
        @return the array for each of the standard opcodes
        """
        ...

    def getTotalLength(self) -> int:
        """
        Returns the size in bytes of the statement information for this
         compilation unit (not including the total_length field itself).
        @return size in bytes of the statement information
        """
        ...

    def getVersion(self) -> int:
        """
        Returns the version identifier for the statement information format.
        @return the version identifier for the statement information format
        """
        ...

    def hashCode(self) -> int: ...

    def isDefaultIsStatement(self) -> bool:
        """
        Returns the initial value of the is_stmt register.
        @return the initial value of the is_stmt register
        """
        ...

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
    def defaultIsStatement(self) -> bool: ...

    @property
    def fileNames(self) -> List[object]: ...

    @property
    def includeDirectories(self) -> List[object]: ...

    @property
    def lineBase(self) -> int: ...

    @property
    def lineRange(self) -> int: ...

    @property
    def minimumInstructionLength(self) -> int: ...

    @property
    def opcodeBase(self) -> int: ...

    @property
    def prologueLength(self) -> int: ...

    @property
    def standardOpcodeLengths(self) -> List[int]: ...

    @property
    def totalLength(self) -> int: ...

    @property
    def version(self) -> int: ...
