from typing import List
import ghidra.app.plugin.processors.sleigh
import ghidra.program.model.lang
import ghidra.program.model.listing
import java.lang


class InstructionUtils(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getFormatedInstructionObjects(instr: ghidra.program.model.listing.Instruction, input: bool) -> List[unicode]:
        """
        Format instruction input or result objects
        @param instr instruction
        @param input input objects if true else result objects
        @return formatted array of strings
        """
        ...

    @staticmethod
    def getFormatedOperandObjects(instr: ghidra.program.model.listing.Instruction, opIndex: int) -> List[unicode]:
        """
        Format instruction operand objects
        @param instr instruction
        @param opIndex the operand index
        @return formatted array of strings
        """
        ...

    @staticmethod
    def getFormattedContextRegisterValueBreakout(instr: ghidra.program.model.listing.Instruction, indent: unicode) -> unicode:
        """
        Get formatted context register as list of child register values
        @param instr
        @return formatted context data
        """
        ...

    @staticmethod
    def getFormattedInstructionDetails(instruction: ghidra.program.model.listing.Instruction, debug: ghidra.app.plugin.processors.sleigh.SleighDebugLogger) -> unicode:
        """
        Get details instruction info as formatted text
        @param instruction
        @param debug SleighDebugerLogger for specified instruction or null
        @return instruction details
        """
        ...

    @staticmethod
    def getFormattedRegisterValueBits(value: ghidra.program.model.lang.RegisterValue, indent: unicode) -> unicode:
        """
        Get formatted RegisterValue as list of child register values
        @param value
        @return
        """
        ...

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
