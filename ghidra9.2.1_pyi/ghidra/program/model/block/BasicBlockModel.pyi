from typing import List
import ghidra.program.model.address
import ghidra.program.model.block
import ghidra.program.model.listing
import ghidra.program.model.symbol
import ghidra.util.task
import java.lang


class BasicBlockModel(ghidra.program.model.block.SimpleBlockModel):
    """
    This BlockModel implements the Basic block model.

     Each Codeblock is made up of contiguous instructions in address order.

      Blocks satisfy the following:
       Any instruction with a label starts a block.
       Each instruction that could cause program control flow to change local to
           the containing function (i.e., excludes calls) is the last instruction of a Codeblock.
       All other instructions are "NOP" fallthroughs, meaning
          after execution the program counter will be at
          the instruction immediately following.
       Any instruction that is unreachable and has no label is also considered the start
           of a block.

     So a CodeBlock in this model consists of contiguous code that has zero or
     more fallthrough or call instructions followed by a single flow instruction.
     Each block may or may not have a label at the first instruction, but may not
     have a label at any other instruction contained in the block.

     This model handles delay slot instructions with the following
     assumptions:
     The delay slot depth of the delayed instruction will always
         correspond to the number of delay slot instructions immediately
         following the instruction. The model may not behave properly if
         the disassembled code violates this assumption.

    """

    NAME: unicode = u'Basic Block'



    @overload
    def __init__(self, program: ghidra.program.model.listing.Program): ...

    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, includeExternals: bool): ...



    def allowsBlockOverlap(self) -> bool:
        """
        @see ghidra.program.model.block.CodeBlockModel#allowsBlockOverlap()
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def externalsIncluded(self) -> bool: ...

    def getBasicBlockModel(self) -> ghidra.program.model.block.CodeBlockModel:
        """
        @see ghidra.program.model.block.CodeBlockModel#getBasicBlockModel()
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getCodeBlockAt(self, addr: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.block.CodeBlock:
        """
        Get the code/data block starting at this address.
        @param addr
        @param monitor task monitor which allows user to cancel operation.
        @return null if there is no codeblock starting at the address
        @throws CancelledException if the monitor cancels the operation.
        """
        ...

    def getCodeBlocks(self, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.block.CodeBlockIterator:
        """
        Get an iterator over the code blocks in the entire program.
        @param monitor task monitor which allows user to cancel operation.
        @throws CancelledException if the monitor cancels the operation.
        """
        ...

    @overload
    def getCodeBlocksContaining(self, addr: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> List[ghidra.program.model.block.CodeBlock]:
        """
        Get all the Code Blocks containing the address.
        @param addr Address to find a containing block.
        @param monitor task monitor which allows user to cancel operation.
        @return A SimpleBlock if any block contains the address
                empty array otherwise.
        @throws CancelledException if the monitor cancels the operation.
        """
        ...

    @overload
    def getCodeBlocksContaining(self, addrSet: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.block.CodeBlockIterator:
        """
        Get an iterator over CodeBlocks which overlap the specified address set.
        @param addrSet an address set within program
        @param monitor task monitor which allows user to cancel operation.
        @throws CancelledException if the monitor cancels the operation.
        """
        ...

    def getDestinations(self, block: ghidra.program.model.block.CodeBlock, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.block.CodeBlockReferenceIterator:
        """
        Get an iterator over destination blocks flowing from this block.
        @param block code block to get the destination block iterator for.
        @param monitor task monitor which allows user to cancel operation.
        @throws CancelledException if the monitor cancels the operation.
        """
        ...

    def getFirstCodeBlockContaining(self, addr: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.block.CodeBlock:
        """
        Get the First Code Block that contains the address.
        @param addr Address to find a containing block.
        @param monitor task monitor which allows user to cancel operation.
        @return A SimpleBlock if any block contains the address.
                null otherwise.
        @throws CancelledException if the monitor cancels the operation.
        """
        ...

    def getFlowType(self, block: ghidra.program.model.block.CodeBlock) -> ghidra.program.model.symbol.FlowType:
        """
        Return in general how things flow out of this node.
         If there are any abnormal ways to flow out of this node,
         (ie: jump, call, etc...) then the flow type of the node
         takes on that type.

         If there are multiple unique ways out of the node, then we
         should return FlowType.UNKNOWN (or FlowType.MULTIFLOW ?).

         Fallthrough is returned if that is the only way out.

         If this block really has no valid instructions, it can't flow,
         so FlowType.INVALID is returned.
        @return flow type of this node
        """
        ...

    @overload
    def getName(self) -> unicode:
        """
        @see ghidra.program.model.block.CodeBlockModel#getName()
        """
        ...

    @overload
    def getName(self, block: ghidra.program.model.block.CodeBlock) -> unicode:
        """
        @see ghidra.program.model.block.CodeBlockModel#getName(ghidra.program.model.block.CodeBlock)
        """
        ...

    def getNumDestinations(self, block: ghidra.program.model.block.CodeBlock, monitor: ghidra.util.task.TaskMonitor) -> int:
        """
        Get number of destination blocks flowing out of this block
        @param block code block to get the destination block iterator for.
        @param monitor task monitor which allows user to cancel operation.
        @throws CancelledException if the monitor cancels the operation.
        @deprecated this method should be avoided since it repeats the work of the getDestinations iterator
        """
        ...

    def getNumSources(self, block: ghidra.program.model.block.CodeBlock, monitor: ghidra.util.task.TaskMonitor) -> int:
        """
        Get number of source blocks flowing into this block
        @param block code block to get the source iterator for.
        @param monitor task monitor which allows user to cancel operation.
        @throws CancelledException if the monitor cancels the operation.
        @deprecated this method should be avoided since it repeats the work of the getSources iterator
        """
        ...

    def getProgram(self) -> ghidra.program.model.listing.Program:
        """
        @see ghidra.program.model.block.CodeBlockModel#getProgram()
        """
        ...

    def getSources(self, block: ghidra.program.model.block.CodeBlock, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.block.CodeBlockReferenceIterator:
        """
        Get an iterator over source blocks flowing into this block.
        @param block code block to get the source iterator for.
        @param monitor task monitor which allows user to cancel operation.
        @throws CancelledException if the monitor cancels the operation.
        """
        ...

    def hashCode(self) -> int: ...

    def isBlockStart(self, instruction: ghidra.program.model.listing.Instruction) -> bool:
        """
        Check if the instruction starts a Simple block.
        @param instruction instruction to test if it starts a block
        @return true if this instruction is the start of a simple block.
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
