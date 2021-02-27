from typing import List
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.lang.InstructionError
import ghidra.program.model.listing
import java.lang


class InstructionError(object):





    class InstructionErrorType(java.lang.Enum):
        DATA_CONFLICT: ghidra.program.model.lang.InstructionError.InstructionErrorType = DATA_CONFLICT
        DUPLICATE: ghidra.program.model.lang.InstructionError.InstructionErrorType = DUPLICATE
        FLOW_ALIGNMENT: ghidra.program.model.lang.InstructionError.InstructionErrorType = FLOW_ALIGNMENT
        INSTRUCTION_CONFLICT: ghidra.program.model.lang.InstructionError.InstructionErrorType = INSTRUCTION_CONFLICT
        MEMORY: ghidra.program.model.lang.InstructionError.InstructionErrorType = MEMORY
        OFFCUT_INSTRUCTION: ghidra.program.model.lang.InstructionError.InstructionErrorType = OFFCUT_INSTRUCTION
        PARSE: ghidra.program.model.lang.InstructionError.InstructionErrorType = PARSE
        isConflict: bool







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
        def valueOf(__a0: unicode) -> ghidra.program.model.lang.InstructionError.InstructionErrorType: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.program.model.lang.InstructionError.InstructionErrorType]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...







    @staticmethod
    def dumpInstructionDifference(newInst: ghidra.program.model.listing.Instruction, existingInstr: ghidra.program.model.listing.Instruction) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getConflictAddress(self) -> ghidra.program.model.address.Address:
        """
        @return address of another code unit which conflicts
         with intended instruction (required for CODE_UNIT
         and DUPLCIATE errors, null for others)
        """
        ...

    def getConflictMessage(self) -> unicode:
        """
        @return instruction error message
        """
        ...

    def getFlowFromAddress(self) -> ghidra.program.model.address.Address:
        """
        @return flow-from address if know else null
        """
        ...

    def getInstructionAddress(self) -> ghidra.program.model.address.Address:
        """
        @return address of new intended instruction which failed to be created (never null)
        """
        ...

    def getInstructionBlock(self) -> ghidra.program.model.lang.InstructionBlock:
        """
        @return instruction block which corresponds to this error
        """
        ...

    def getInstructionErrorType(self) -> ghidra.program.model.lang.InstructionError.InstructionErrorType:
        """
        @return type of instruction error
        """
        ...

    def getParseContextValue(self) -> ghidra.program.model.lang.RegisterValue:
        """
        @return disassembler context at intended instruction
         address (required for PARSE error, null for others)
        """
        ...

    def hashCode(self) -> int: ...

    def isInstructionConflict(self) -> bool: ...

    def isOffcutError(self) -> bool: ...

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
    def conflictAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def conflictMessage(self) -> unicode: ...

    @property
    def flowFromAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def instructionAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def instructionBlock(self) -> ghidra.program.model.lang.InstructionBlock: ...

    @property
    def instructionConflict(self) -> bool: ...

    @property
    def instructionErrorType(self) -> ghidra.program.model.lang.InstructionError.InstructionErrorType: ...

    @property
    def offcutError(self) -> bool: ...

    @property
    def parseContextValue(self) -> ghidra.program.model.lang.RegisterValue: ...
