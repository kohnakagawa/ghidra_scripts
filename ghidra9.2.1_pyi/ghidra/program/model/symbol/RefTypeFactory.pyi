from typing import List
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.program.model.symbol
import java.lang


class RefTypeFactory(object):
    """
    Factory class to create RefType objects.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def get(type: int) -> ghidra.program.model.symbol.RefType:
        """
        Get static instance of the specified RefType/FlowType
        @param type ref-type value
        @return ref-type instance
        @throws NoSuchElementException if ref-type is not defined
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getDataRefTypes() -> List[ghidra.program.model.symbol.RefType]: ...

    @staticmethod
    def getDefaultComputedFlowType(instr: ghidra.program.model.listing.Instruction) -> ghidra.program.model.symbol.FlowType:
        """
        Determine default computed FlowType for a specified instruction.  It is assumed
         that all computed flows utilize a register in its destination specification/computation.
        @param instr instruction
        @return FlowType or null if unable to determine
        """
        ...

    @staticmethod
    def getDefaultFlowType(instr: ghidra.program.model.listing.Instruction, toAddr: ghidra.program.model.address.Address, allowComputedFlowType: bool) -> ghidra.program.model.symbol.FlowType:
        """
        Determine default FlowType for a specified instruction and flow destination toAddr.
        @param instr instruction
        @param toAddr flow destination address
        @param allowComputedFlowType if true and an absolute flow type is not found
         a computed flow type will be returned if only one exists.
        @return FlowType or null if unable to determine
        """
        ...

    @staticmethod
    def getDefaultMemoryRefType(cu: ghidra.program.model.listing.CodeUnit, opIndex: int, toAddr: ghidra.program.model.address.Address, ignoreExistingReferences: bool) -> ghidra.program.model.symbol.RefType:
        """
        Get the default memory flow/data RefType for the specified code unit and opIndex.
        @param cu
        @param opIndex
        @param toAddr reference destination
        @param ignoreExistingReferences if true existing references will not influence default
         reference type returned.
        @return default RefType
        """
        ...

    @staticmethod
    def getDefaultRegisterRefType(cu: ghidra.program.model.listing.CodeUnit, reg: ghidra.program.model.lang.Register, opIndex: int) -> ghidra.program.model.symbol.RefType:
        """
        Get the default statck data RefType for the specified code-unit/opIndex and register
        @param cu
        @param reg
        @param opIndex
        @return default RefType
        """
        ...

    @staticmethod
    def getDefaultStackRefType(cu: ghidra.program.model.listing.CodeUnit, opIndex: int) -> ghidra.program.model.symbol.RefType:
        """
        Get the default register data RefType for the specified code-unit/opIndex and register
        @param cu the code unit to get the default stack ref type.
        @param opIndex the operand index.
        @return the default register datat refType.
        """
        ...

    @staticmethod
    def getExternalRefTypes() -> List[ghidra.program.model.symbol.RefType]: ...

    @staticmethod
    def getMemoryRefTypes() -> List[ghidra.program.model.symbol.RefType]: ...

    @staticmethod
    def getStackRefTypes() -> List[ghidra.program.model.symbol.RefType]: ...

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
