from typing import List
import ghidra.app.plugin.processors.sleigh
import ghidra.app.plugin.processors.sleigh.pattern
import ghidra.app.plugin.processors.sleigh.symbol
import java.lang


class SleighDebugLogger(object):
    """
    SleighDebugLogger provides the ability to obtain detailed instruction
     parse details.
    """






    class SleighDebugMode(java.lang.Enum):
        MASKS_ONLY: ghidra.app.plugin.processors.sleigh.SleighDebugLogger.SleighDebugMode = MASKS_ONLY
        VERBOSE: ghidra.app.plugin.processors.sleigh.SleighDebugLogger.SleighDebugMode = VERBOSE







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
        def valueOf(__a0: unicode) -> ghidra.app.plugin.processors.sleigh.SleighDebugLogger.SleighDebugMode: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.app.plugin.processors.sleigh.SleighDebugLogger.SleighDebugMode]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...



    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, start: ghidra.program.model.address.Address, mode: ghidra.app.plugin.processors.sleigh.SleighDebugLogger.SleighDebugMode):
        """
        Performs a parse debug at the specified memory location within program.
        @param program the program the memory location is found in
        @param start the start address of the memory location
        @param mode the sleigh debug mode
        @throws IllegalArgumentException if program language provider is not Sleigh
        """
        ...

    @overload
    def __init__(self, buf: ghidra.program.model.mem.MemBuffer, context: ghidra.program.model.lang.ProcessorContextView, language: ghidra.program.model.lang.Language, mode: ghidra.app.plugin.processors.sleigh.SleighDebugLogger.SleighDebugMode):
        """
        Performs a parse debug at the specified memory location within program.
        @param buf the memory buffer
        @param context the processor context
        @param language the sleigh language
        @param mode the sleigh debug mode
        @throws IllegalArgumentException if program language provider is not Sleigh
        """
        ...



    def addContextPattern(self, maskvalue: ghidra.app.plugin.processors.sleigh.pattern.PatternBlock) -> None:
        """
        Add instruction context pattern to the current pattern group.
        @param maskvalue pattern mask/value
        """
        ...

    def addInstructionPattern(self, offset: int, maskvalue: ghidra.app.plugin.processors.sleigh.pattern.PatternBlock) -> None:
        """
        Add instruction bit pattern to the current pattern group.
        @param offset base offset at which the specified maskvalue
         can be applied.
        @param maskvalue pattern mask/value
        """
        ...

    @overload
    def append(self, str: unicode) -> None:
        """
        Append message string to log buffer.
         NOTE: Method has no affect unless constructed with VERBOSE logging mode.
        @param str message string
        """
        ...

    @overload
    def append(self, value: int, startbit: int, bitcount: int) -> None:
        """
        Append a binary formatted integer value with the specified range of bits
         bracketed to the log.  A -1 value for both startbit and bitcount disable the
         bit range bracketing.
         NOTE: Method has no affect unless constructed with VERBOSE logging mode.
        @param value integer value
        @param startbit identifies the first most-significant bit within the
         bracketed range (left-most value bit is bit-0, right-most value bit is bit-31)
        @param bitcount number of bits included within range
        """
        ...

    @overload
    def append(self, value: List[int], startbit: int, bitcount: int) -> None:
        """
        Append a binary formatted integer array with the specified range of bits
         bracketed to the log.  A -1 value for both startbit and bitcount disable the
         bit range bracketing.
         NOTE: Method has no affect unless constructed with VERBOSE logging mode.
        @param value integer array
        @param startbit identifies the first most-significant bit within the
         {@literal bracketed range (left-most value[0] bit is bit-0, right-most value[n] bit is bit-<32(n+1)-1> ).}
        @param bitcount number of bits included within range
        """
        ...

    @overload
    def append(self, value: List[int], startbit: int, bitcount: int) -> None:
        """
        Append a binary formatted integer array with the specified range of bits
         bracketed to the log.  A -1 value for both startbit and bitcount disable the
         bit range bracketing.
         NOTE: Method has no affect unless constructed with VERBOSE logging mode.
        @param value integer array
        @param startbit identifies the first most-significant bit within the
         {@literal bracketed range (left-most value[0] bit is bit-0, right-most value[n] bit is bit-<32(n+1)-1> ).}
        @param bitcount number of bits included within range
        """
        ...

    @overload
    def dropIndent(self) -> None:
        """
        Shift log indent left
        """
        ...

    @overload
    def dropIndent(self, levels: int) -> None: ...

    def dumpContextPattern(self, maskvec: List[int], valvec: List[int], byteOffset: int, pos: ghidra.app.plugin.processors.sleigh.SleighParserContext) -> None:
        """
        Dump context pattern details.
         NOTE: Method has no affect unless constructed with VERBOSE logging mode.
        @param maskvec
        @param valvec
        @param byteOffset
        @param pos
        """
        ...

    def dumpContextSet(self, pos: ghidra.app.plugin.processors.sleigh.SleighParserContext, num: int, value: int, mask: int) -> None:
        """
        Dump transient context setting details.
         NOTE: Method has no affect unless constructed with VERBOSE logging mode.
        @param pos instruction context
        @param num 4-byte offset within base context register for mask and value
        @param value 4-byte context value
        @param mask 4-byte context mask
        """
        ...

    def dumpGlobalSet(self, pos: ghidra.app.plugin.processors.sleigh.SleighParserContext, state: ghidra.app.plugin.processors.sleigh.ConstructState, sym: ghidra.app.plugin.processors.sleigh.symbol.TripleSymbol, num: int, mask: int, value: int) -> None:
        """
        Dump globalset details.  The target address is currently not included in the log.
         NOTE: Method has no affect unless constructed with VERBOSE logging mode.
        @param pos
        @param state
        @param sym
        @param num
        @param mask
        @param value
        @throws MemoryAccessException
        """
        ...

    def endPatternGroup(self, commit: bool) -> None:
        """
        Terminate the current pattern group
        @param commit if false group will be discarded, if true group will be retained
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getConstructorLineNumbers(self) -> List[unicode]:
        """
        Get list of constructor names with line numbers.
         Any debug mode may be used.
        @return list
        """
        ...

    @staticmethod
    def getFormattedBytes(value: List[int]) -> unicode:
        """
        Convenience method for formatting bytes as a bit sequence
        @param value byte array
        @return binary formatted bytes
        """
        ...

    def getFormattedInstructionMask(self, opIndex: int) -> unicode:
        """
        Return general/operand bit mask formatted as a String
        @param opIndex operand index or -1 for mnemonic mask
        @return bit mask string
        """
        ...

    def getFormattedMaskedValue(self, opIndex: int) -> unicode:
        """
        Return general/operand bit values formatted as a String
        @param opIndex operand index or -1 for mnemonic bit values
        @return bit value string
        """
        ...

    def getInstructionMask(self) -> List[int]:
        """
        Returns the instruction bit mask which identifies those bits used to uniquely identify
         the instruction (includes addressing modes, generally excludes register selector bits
         associated with attaches or immediate values used in for semantic values only).
        @throws IllegalStateException if prototype parse failed
        @see #getFormattedInstructionMask(int) getFormattedInstructionMask(-1)
        """
        ...

    def getMaskedBytes(self, mask: List[int]) -> List[int]:
        """
        Apply an appropriate mask for the resulting instruction bytes
         to obtain the corresponding masked bytes.
        @param mask instruction, operand or similarly sized mask
        @return masked instruction bytes
        """
        ...

    def getNumOperands(self) -> int:
        """
        Get the number of operands for the resulting prototype
        @return operand count
        @throws IllegalStateException if prototype parse failed
        """
        ...

    def getOperandValueMask(self, opIndex: int) -> List[int]:
        """
        Get the byte value mask corresponding to the specified operand.
        @param opIndex operand index within the instruction representation
        @return byte mask or null if operand does not have a corresponding sub-constructor or attach
        @throws IllegalStateException if prototype parse failed
        @throws IndexOutOfBoundsException if opIndex is not a valid operand index
        """
        ...

    def hashCode(self) -> int: ...

    @overload
    def indent(self) -> None:
        """
        Shift log indent right
        """
        ...

    @overload
    def indent(self, levels: int) -> None: ...

    def isVerboseEnabled(self) -> bool:
        """
        @return true if constructed for verbose logging
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def parseFailed(self) -> bool:
        """
        @return true if a parse error was detected, otherwise false is returned.
         The methods getMaskedBytes() and getInstructionMask() should
         only be invoked if this method returns false.
        """
        ...

    def startPatternGroup(self, name: unicode) -> None:
        """
        Start new pattern group for a specific sub-table.
         A null can correspond to a top-level constructor or
         low level complex pattern (AND, OR).  All committed unnamed groups
         with the same parent group will be combined.
        @param name group name or null for unnamed group
        """
        ...

    def toString(self) -> unicode:
        """
        Return log text
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def constructorLineNumbers(self) -> List[object]: ...

    @property
    def instructionMask(self) -> List[int]: ...

    @property
    def numOperands(self) -> int: ...

    @property
    def verboseEnabled(self) -> bool: ...
