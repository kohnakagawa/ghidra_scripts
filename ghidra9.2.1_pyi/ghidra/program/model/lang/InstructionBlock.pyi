from typing import Iterator
from typing import List
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.lang.InstructionError
import ghidra.program.model.listing
import java.lang
import java.util
import java.util.function


class InstructionBlock(object, java.lang.Iterable):
    """
    Represents a block of instructions.  Used as part of an InstructionSet to be added to the
     program.
    """





    def __init__(self, startAddr: ghidra.program.model.address.Address): ...

    def __iter__(self): ...

    def addBlockFlow(self, blockFlow: ghidra.program.model.lang.InstructionBlockFlow) -> None:
        """
        Add a block flow specified by a InstructionBlockFlow object.  These flows include all
         calls, branches and fall-throughs and may span across multiple InstructionSets and are
         not used by the block flow iterator within the associated InstructionSet.
        @param blockFlow block flow
        """
        ...

    def addBranchFlow(self, destinationAddress: ghidra.program.model.address.Address) -> None:
        """
        Adds a branch type flow to this instruction block and is used by the block flow
         iterator of the associated InstructionSet.
        @param destinationAddress the destination of a branch type flow from this instruction block.
        """
        ...

    def addInstruction(self, instruction: ghidra.program.model.listing.Instruction) -> None:
        """
        Adds an instruction to this block.  If the block in not empty, the newly added instruction
         must be directly after the current block maximum address.  In other words, all instructions
         int the block must be consecutive.
        @param instruction the instruction to add to this block.
        @throws IllegalArgumentException if the new instruction does not immediately follow the
         last instruction added.
        """
        ...

    def clearConflict(self) -> None:
        """
        Clears any conflict associated with this block.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def findFirstIntersectingInstruction(self, min: ghidra.program.model.address.Address, max: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Instruction:
        """
        Find the first instruction within this block which intersects the specified range.
         This method should be used sparingly since it uses a brute-force search.
        @param min the minimum intersection address
        @param max the maximum intersection address
        @return instruction within this block which intersects the specified range or null
         if not found
        """
        ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    def getBlockFlows(self) -> List[ghidra.program.model.lang.InstructionBlockFlow]:
        """
        Returns a list of all block flows that were added to this instruction block as
         a list of InstructionBlockFlow objects.  NOTE: These flows may not be contained
         within the associated InstructionSet.
        @return a list of all flows that were added to this instruction block.
        """
        ...

    def getBranchFlows(self) -> List[ghidra.program.model.address.Address]:
        """
        Returns a list of all the branch flows that were added to this instruction block
         and flow to other blocks within the associated InstructionSet.
        @return a list of all the branch flows that were added to this instruction block.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getFallThrough(self) -> ghidra.program.model.address.Address:
        """
        Returns the fallthrough address.  Null is returned if there is no fall through.
        @return the fallthrough address.
        """
        ...

    def getFlowFromAddress(self) -> ghidra.program.model.address.Address: ...

    def getInstructionAt(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Instruction:
        """
        Returns the instruction at the specified address within this block
        @param address
        @return instruction at the specified address within this block or null if not found
        """
        ...

    def getInstructionConflict(self) -> ghidra.program.model.lang.InstructionError:
        """
        Returns the current conflict associated with this block.
        @return the current conflict associated with this block.
        """
        ...

    def getInstructionCount(self) -> int:
        """
        @return number of instructions contained within this block
        """
        ...

    def getInstructionsAddedCount(self) -> int:
        """
        @return number of instructions which were added to the program
         successfully.
        """
        ...

    def getLastInstructionAddress(self) -> ghidra.program.model.address.Address:
        """
        @return address of last instruction contained within this block
        """
        ...

    def getMaxAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the maximum address of the block, or null if the block is empty;
        @return the maximum address of the block.
        """
        ...

    def getStartAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the minimum/start address of the block;
        @return the minimum/start address of the block
        """
        ...

    def hasInstructionError(self) -> bool: ...

    def hashCode(self) -> int: ...

    def isEmpty(self) -> bool:
        """
        @return true if no instructions exist within this block
        """
        ...

    def isFlowStart(self) -> bool:
        """
        @return true if this block should be treated as the start of a new
         flow when added to a InstructionSet.
        """
        ...

    def iterator(self) -> Iterator[ghidra.program.model.listing.Instruction]:
        """
        Returns an iterator over all the instructions in this block.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setCodeUnitConflict(self, codeUnitAddr: ghidra.program.model.address.Address, newInstrAddr: ghidra.program.model.address.Address, flowFromAddr: ghidra.program.model.address.Address, isInstruction: bool, isOffcut: bool) -> None:
        """
        Set offcut-instruction or data CODE_UNIT conflict
        @param codeUnitAddr existing instruction/data address
        @param newInstrAddr new disassembled instruction address
        @param flowFromAddr flow-from address
        @param isInstruction true if conflict is due to offcut-instruction, otherwise data is assumed
        @param isOffcut true if conflict due to offcut instruction
        """
        ...

    def setFallThrough(self, fallthroughAddress: ghidra.program.model.address.Address) -> None:
        """
        Sets the fall through address for this block and is used by the block flow
         iterator of the associated InstructionSet.  The fallthrough should not be
         set if it is added as a block flow.
        @param fallthroughAddress the address of the fallthrough
        """
        ...

    def setFlowFromAddress(self, flowFrom: ghidra.program.model.address.Address) -> None: ...

    def setInconsistentPrototypeConflict(self, instrAddr: ghidra.program.model.address.Address, flowFromAddr: ghidra.program.model.address.Address) -> None:
        """
        Set inconsistent instruction prototype CODE_UNIT conflict
        @param instrAddr instruction addr where inconsistent prototype exists
        @param flowFromAddr flow-from address
        """
        ...

    def setInstructionError(self, type: ghidra.program.model.lang.InstructionError.InstructionErrorType, intendedInstructionAddress: ghidra.program.model.address.Address, conflictAddress: ghidra.program.model.address.Address, flowFromAddress: ghidra.program.model.address.Address, message: unicode) -> None:
        """
        Sets this block to have an instruction error.
        @param type The type of error/conflict.
        @param intendedInstructionAddress address of intended instruction which failed to be created
        @param conflictAddress the address of the exiting code unit that is preventing the instruction in this
         block to be laid down (required for CODE_UNIT or DUPLCIATE conflict error).
        @param flowFromAddress the flow-from instruction address or null if unknown
        @param message - A message that describes the conflict to a user.
        """
        ...

    def setInstructionMemoryError(self, instrAddr: ghidra.program.model.address.Address, flowFromAddr: ghidra.program.model.address.Address, errorMsg: unicode) -> None:
        """
        Set instruction memory error
        @param instrAddr instruction address
        @param flowFromAddr flow-from address
        @param errorMsg
        """
        ...

    def setInstructionsAddedCount(self, count: int) -> None:
        """
        Set the number of instructions which were added to the program
        @param count
        """
        ...

    def setParseConflict(self, conflictAddress: ghidra.program.model.address.Address, contextValue: ghidra.program.model.lang.RegisterValue, flowFromAddress: ghidra.program.model.address.Address, message: unicode) -> None:
        """
        Sets this block to have a PARSE conflict which means that the instruction parse failed
         at the specified conflictAddress using the specified contextValue.
        @param conflictAddress the address of the exiting code unit that is preventing the instruction in this
         block to be laid down.
        @param contextValue the context-register value used during the failed parse attempt
        @param flowFromAddress the flow-from instruction address or null
        @param message - A message that describes the conflict to a user.
        """
        ...

    def setStartOfFlow(self, isStart: bool) -> None:
        """
        Allows the block to be tagged as start of flow to force
         InstructionSet iterator to treat as a flow start.
         This method should not be used after this block has
         been added to an InstructionSet
        @param isStart
        """
        ...

    def spliterator(self) -> java.util.Spliterator: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def blockFlows(self) -> List[object]: ...

    @property
    def branchFlows(self) -> List[object]: ...

    @property
    def empty(self) -> bool: ...

    @property
    def fallThrough(self) -> ghidra.program.model.address.Address: ...

    @fallThrough.setter
    def fallThrough(self, value: ghidra.program.model.address.Address) -> None: ...

    @property
    def flowFromAddress(self) -> ghidra.program.model.address.Address: ...

    @flowFromAddress.setter
    def flowFromAddress(self, value: ghidra.program.model.address.Address) -> None: ...

    @property
    def flowStart(self) -> bool: ...

    @property
    def instructionConflict(self) -> ghidra.program.model.lang.InstructionError: ...

    @property
    def instructionCount(self) -> int: ...

    @property
    def instructionsAddedCount(self) -> int: ...

    @instructionsAddedCount.setter
    def instructionsAddedCount(self, value: int) -> None: ...

    @property
    def lastInstructionAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def maxAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def startAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def startOfFlow(self) -> None: ...  # No getter available.

    @startOfFlow.setter
    def startOfFlow(self, value: bool) -> None: ...
