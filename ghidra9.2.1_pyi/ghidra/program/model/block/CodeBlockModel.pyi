from typing import List
import ghidra.program.model.address
import ghidra.program.model.block
import ghidra.program.model.listing
import ghidra.program.model.symbol
import ghidra.util.task
import java.lang


class CodeBlockModel(object):
    """
    An implementation of a CodeBlockModel will produce CodeBlocks
     based on some algorithm.
    """

    emptyBlockArray: List[ghidra.program.model.block.CodeBlock] = array(ghidra.program.model.block.CodeBlock)







    def allowsBlockOverlap(self) -> bool:
        """
        Return true if this model allows overlapping of address sets for
         the blocks it returns.
        @return true if this model allows overlapping of address sets for
                 the blocks it returns.
                 This implies that getBlocksContaining() can return more than one block.
                 false implies that getBlocksContaining() will return at most one block.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def externalsIncluded(self) -> bool:
        """
        Returns true if externals are handled by the model,
         false if externals are ignored.  When handled, externals
         are represented by an ExtCodeBlockImpl.
        """
        ...

    def getBasicBlockModel(self) -> ghidra.program.model.block.CodeBlockModel:
        """
        Get the basic block model used by this model.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getCodeBlockAt(self, addr: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.block.CodeBlock:
        """
        Get the code block with a starting address (i.e., entry-point) of addr.
        @param addr starting address of a codeblock.
        @param monitor task monitor which allows user to cancel operation.
        @return null if there is no codeblock starting at the address.
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
        Get all the code blocks containing the address.
        @param addr address to find a containing block.
        @param monitor task monitor which allows user to cancel operation.
        @return an array of blocks that contains the address, null otherwise.
        @throws CancelledException if the monitor cancels the operation.
        """
        ...

    @overload
    def getCodeBlocksContaining(self, addrSet: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.block.CodeBlockIterator:
        """
        Get an iterator over code blocks which overlap the specified address set.
        @param addrSet an address set within program
        @param monitor task monitor which allows user to cancel operation.
        @throws CancelledException if the monitor cancels the operation.
        """
        ...

    def getDestinations(self, block: ghidra.program.model.block.CodeBlock, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.block.CodeBlockReferenceIterator:
        """
        Get an iterator over the destination flows out of the block.
        @param block the block to get the destination flows for.
        @param monitor task monitor which allows user to cancel operation.
        @throws CancelledException if the monitor cancels the operation.
        """
        ...

    def getFirstCodeBlockContaining(self, addr: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.block.CodeBlock:
        """
        Get the first code block that contains the given address.
        @param addr address to find a containing block.
        @param monitor task monitor which allows user to cancel operation.
        @return a block that contains the address, or null otherwise.
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
        @return flow type of this node
        """
        ...

    @overload
    def getName(self) -> unicode:
        """
        Returns the model name.
        @return the model name
        """
        ...

    @overload
    def getName(self, block: ghidra.program.model.block.CodeBlock) -> unicode:
        """
        Get a name for this block.
        @return usually the label at the start address of the block
            however the model can choose any name it wants for its blocks.
        """
        ...

    def getNumDestinations(self, block: ghidra.program.model.block.CodeBlock, monitor: ghidra.util.task.TaskMonitor) -> int:
        """
        Get the number of destination flows out of the block.
        @param block the code blocks to get the destination flows for.
        @param monitor task monitor which allows user to cancel operation.
        @throws CancelledException if the monitor cancels the operation.
        """
        ...

    def getNumSources(self, block: ghidra.program.model.block.CodeBlock, monitor: ghidra.util.task.TaskMonitor) -> int:
        """
        Get the number of source flows into the block.
        @param block the code blocks to get the destination flows for.
        @param monitor task monitor which allows user to cancel operation.
        @throws CancelledException if the monitor cancels the operation.
        """
        ...

    def getProgram(self) -> ghidra.program.model.listing.Program:
        """
        Returns the program object associated with this CodeBlockModel instance.
        @return program associated with this CodeBlockModel.
        """
        ...

    def getSources(self, block: ghidra.program.model.block.CodeBlock, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.block.CodeBlockReferenceIterator:
        """
        Get an iterator over the source flows into the block.
        @param block the block to get the destination flows for.
        @param monitor task monitor which allows user to cancel operation.
        @throws CancelledException if the monitor cancels the operation.
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

    @property
    def basicBlockModel(self) -> ghidra.program.model.block.CodeBlockModel: ...

    @property
    def name(self) -> unicode: ...

    @property
    def program(self) -> ghidra.program.model.listing.Program: ...
