from typing import List
import ghidra.app.util
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.lang
import ghidra.program.model.listing
import java.lang


class PseudoDisassembler(object):
    """
    PseudoDisassembler.java

     Useful for disassembling and getting an Instruction or creating Data
     at a location in memory when you don't want the program to be changed.

     The Instructions or Data that area created are PseudoInstruction's and
     PseudoData's.  They act like regular instructions in most respects, but
     they don't exist in the program.  No references, symbols, are created or
     will be saved when the program is saved.

     You do not need to have an open transaction on the program to use the
     PseudoDisassembler.

     The PseudoDisassembler can also be used to check if something is a valid
     subroutine.  The algorithm it uses could definitely use some tuning, but
     it generally works well.
    """





    def __init__(self, program: ghidra.program.model.listing.Program):
        """
        Create a pseudo disassembler for the given program.
        """
        ...



    def applyDataType(self, addr: ghidra.program.model.address.Address, dt: ghidra.program.model.data.DataType) -> ghidra.app.util.PseudoData:
        """
        Apply a dataType to the program at the given address.  The program is
         not affected.  A PseudoData item that acts like a Data item retrieved from
         a program is returned.  This is useful if you have a datatype and you
         want to use it to get values from the program at a given address.
        @param addr location to get a PseudoData item for
        @param dt the data type to be applied
        @return PsuedoData that acts like Data
        """
        ...

    def checkValidSubroutine(self, entryPoint: ghidra.program.model.address.Address, procContext: ghidra.app.util.PseudoDisassemblerContext, allowExistingInstructions: bool, mustTerminate: bool) -> bool: ...

    @overload
    def disassemble(self, addr: ghidra.program.model.address.Address) -> ghidra.app.util.PseudoInstruction:
        """
        Disassemble a single instruction.  The program is not affected.
        @param addr location to disassemble
        @return a PseudoInstruction
        @throws InsufficientBytesException
        @throws UnknownInstructionException
        @throws UnknownContextException
        """
        ...

    @overload
    def disassemble(self, addr: ghidra.program.model.address.Address, bytes: List[int]) -> ghidra.app.util.PseudoInstruction:
        """
        Disassemble a location in memory with the given set of bytes.
         Useful when the address has no actual bytes defined, or you want to use
         your own bytes instead of what is in the program at the address.
        @param addr address to disassemble
        @param bytes bytes to use instead of those currently defined in program
        @return PseudoInstruction.
        @throws InsufficientBytesException
        @throws UnknownInstructionException
        @throws UnknownContextException
        """
        ...

    @overload
    def disassemble(self, addr: ghidra.program.model.address.Address, disassemblerContext: ghidra.app.util.PseudoDisassemblerContext, isInDelaySlot: bool) -> ghidra.app.util.PseudoInstruction:
        """
        Disassemble a single instruction.  The program is not affected.
        @param addr
        @param disassemblerContext
        @param isInDelaySlot
        @return
        @throws InsufficientBytesException
        @throws UnknownInstructionException
        @throws UnknownContextException
        """
        ...

    @overload
    def disassemble(self, addr: ghidra.program.model.address.Address, bytes: List[int], disassemblerContext: ghidra.app.util.PseudoDisassemblerContext) -> ghidra.app.util.PseudoInstruction:
        """
        Disassemble a location in memory with the given set of bytes.
         Useful when the address has no actual bytes defined, or you want to use
         your own bytes instead of what is in the program at the address.
        @param addr address to disassemble
        @param bytes bytes to use instead of those currently defined in program
        @param disassemblerContext the disassembler context to use.
        @return PseudoInstruction.
        @throws InsufficientBytesException
        @throws UnknownInstructionException
        @throws UnknownContextException
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    @overload
    def followSubFlows(self, entryPoint: ghidra.program.model.address.Address, maxInstr: int, processor: ghidra.app.util.PseudoFlowProcessor) -> ghidra.program.model.address.AddressSet:
        """
        Process a subroutine using the processor function.
         The process function can control what flows are followed and when to stop.
        @param entryPoint start address
        @param processor processor to use
        @return the address set of instructions that were followed
        """
        ...

    @overload
    def followSubFlows(self, entryPoint: ghidra.program.model.address.Address, procContext: ghidra.app.util.PseudoDisassemblerContext, maxInstr: int, processor: ghidra.app.util.PseudoFlowProcessor) -> ghidra.program.model.address.AddressSet:
        """
        Process a subroutine using the processor function.
         The process function can control what flows are followed and when to stop.
        @param entryPoint start address
        @param processor processor to use
        @return the address set of instructions that were followed
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getIndirectAddr(self, toAddr: ghidra.program.model.address.Address) -> ghidra.program.model.address.Address:
        """
        Interpret the bytes at a location in memory as an address
         and return the address.  This routine assumes that the bytes
         needed to create the address are the same size as the bytes
         needed to represent the toAddr.  So this is somewhat generic.
        @param toAddr location of the bytes in memory
        @return the address value
        """
        ...

    @staticmethod
    def getNormalizedDisassemblyAddress(program: ghidra.program.model.listing.Program, addr: ghidra.program.model.address.Address) -> ghidra.program.model.address.Address:
        """
        Get an address that can be used for disassembly.  Useful for some processors where
         pointers to code have 1 added to them for different modes such as Thumb mode for ARM.
        @param program to get address from
        @param addr to be normallized/aligned for disassembly
        @return the normalized/aligned address for disassembly
        """
        ...

    @staticmethod
    def getTargetContextRegisterValueForDisassembly(program: ghidra.program.model.listing.Program, addr: ghidra.program.model.address.Address) -> ghidra.program.model.lang.RegisterValue:
        """
        @return RegisterValue setting for the context register to disassemble correctly at the given address
                 or null, if no setting is needed.
        """
        ...

    @staticmethod
    def hasLowBitCodeModeInAddrValues(program: ghidra.program.model.listing.Program) -> bool:
        """
        @return true if program has uses the low bit of an address to change Instruction Set mode
        """
        ...

    def hashCode(self) -> int: ...

    @overload
    def isValidCode(self, entryPoint: ghidra.program.model.address.Address) -> bool:
        """
        Check that this entry point leads to valid code:
         <ul>
         <li> May have multiple entries into the body of the code.
         <li>The intent is that it be valid code, not nice code.
         <li>Hit no bad instructions.
         <li>It should return.
         </ul>
        @param entryPoint
        @return true if the entry point leads to valid code
        """
        ...

    @overload
    def isValidCode(self, entryPoint: ghidra.program.model.address.Address, context: ghidra.app.util.PseudoDisassemblerContext) -> bool:
        """
        Check that this entry point leads to valid code:
         <ul>
         <li> May have multiple entries into the body of the code.
         <li>The intent is that it be valid code, not nice code.
         <li>Hit no bad instructions.
         <li>It should return.
         </ul>
        @param entryPoint location to test for valid code
        @param context disassembly context for program
        @return true if the entry point leads to valid code
        """
        ...

    @overload
    def isValidSubroutine(self, entryPoint: ghidra.program.model.address.Address) -> bool:
        """
        Check that this entry point leads to a well behaved subroutine:
         <ul>
         <li>It should return.</li>
         <li>Hit no bad instructions.</li>
         <li>Have only one entry point.</li>
         <li>Not overlap any existing data or instructions.</li>
         </ul>
        @param entryPoint entry point to check
        @return true if entry point leads to a well behaved subroutine
        """
        ...

    @overload
    def isValidSubroutine(self, entryPoint: ghidra.program.model.address.Address, allowExistingCode: bool) -> bool:
        """
        Check that this entry point leads to a well behaved subroutine, allow it
         to fall into existing code.
         <ul>
         <li>It should return.</li>
         <li>Hit no bad instructions.</li>
         <li>Have only one entry point.</li>
         <li>Not overlap any existing data or cause offcut references.</li>
         </ul>
        @param entryPoint entry point to check
        @param allowExistingCode true allows this subroutine to flow into existing instructions.
        @return true if entry point leads to a well behaved subroutine
        """
        ...

    @overload
    def isValidSubroutine(self, entryPoint: ghidra.program.model.address.Address, allowExistingCode: bool, mustTerminate: bool) -> bool:
        """
        Check that this entry point leads to a well behaved subroutine, allow it
         to fall into existing code.
         <ul>
         <li>Hit no bad instructions.</li>
         <li>Have only one entry point.</li>
         <li>Not overlap any existing data or cause offcut references.</li>
         </ul>
        @param entryPoint entry point to check
        @param allowExistingCode true allows this subroutine to flow into existing instructions.
        @param mustTerminate true if the subroutine must terminate
        @return true if entry point leads to a well behaved subroutine
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setMaxInstructions(self, maxNumInstructions: int) -> None:
        """
        Set the maximum number of instructions to check
        @param maxNumInstructions - maximum number of instructions to check before returning
        """
        ...

    def setRespectExecuteFlag(self, respect: bool) -> None:
        """
        Set flag to respect Execute bit on memory if present on any memory
        @param respect - true, respect execute bit on memory blocks
        """
        ...

    @overload
    def setTargeContextForDisassembly(self, procContext: ghidra.app.util.PseudoDisassemblerContext, addr: ghidra.program.model.address.Address) -> ghidra.program.model.address.Address:
        """
        In order to check a location to see if it disassembles from an address reference, the
         address is checked for low-bit code switch behavior.  If it does switch, the context
         is changed.
        @param procContext context to change
        @param addr destination address that will be disassembled (possible pseudo disassembled)
        @return the correct disassembly location if the address needed to be adjusted.
        """
        ...

    @overload
    @staticmethod
    def setTargeContextForDisassembly(program: ghidra.program.model.listing.Program, addr: ghidra.program.model.address.Address) -> ghidra.program.model.address.Address:
        """
        If this processor uses the low bit of an address to change to a new Instruction Set mode
           Check the low bit and change the instruction state at the address.
        @param program
        @param addr the raw address
        @return the correct address to disassemble at if it needs to be aligned
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def maxInstructions(self) -> None: ...  # No getter available.

    @maxInstructions.setter
    def maxInstructions(self, value: int) -> None: ...

    @property
    def respectExecuteFlag(self) -> None: ...  # No getter available.

    @respectExecuteFlag.setter
    def respectExecuteFlag(self, value: bool) -> None: ...
