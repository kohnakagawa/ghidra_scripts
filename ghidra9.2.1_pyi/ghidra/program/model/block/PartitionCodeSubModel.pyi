from typing import List
import ghidra.program.model.address
import ghidra.program.model.block
import ghidra.program.model.listing
import ghidra.program.model.symbol
import ghidra.util.task
import java.lang


class PartitionCodeSubModel(object, ghidra.program.model.block.SubroutineBlockModel):
    """
    PartitionCodeSubModel (Model-P) defines subroutines which do not share code with
     other subroutines and may have one or more entry points.
     Entry points represent anyone of a variety of flow entries, including a source, called, jump or
     fall-through entry point.

     MODEL-P is the answer to those who always want to be able to know what subroutine
     a given instruction is in, but also do not want the subroutine to have multiple
     entry points.  When a model-M subroutine has multiple entry points,
     that set of code will necessarily consist of several model-P subroutines.  When
     a model-M subroutine has a single entry point, it will consist of a single model-P subroutine
     which has the same address set and entry point.
    """

    NAME: unicode = u'Partitioned Code'
    emptyBlockArray: List[ghidra.program.model.block.CodeBlock] = array(ghidra.program.model.block.CodeBlock)



    @overload
    def __init__(self, program: ghidra.program.model.listing.Program):
        """
        Construct a Model-P subroutine on a program.
        @param program program to create blocks from.
        """
        ...

    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, includeExternals: bool):
        """
        Construct a Model-P subroutine on a program.
        @param program program to create blocks from.
        @param includeExternals externals included if true
        """
        ...



    def allowsBlockOverlap(self) -> bool:
        """
        @see ghidra.program.model.block.CodeBlockModel#allowsBlockOverlap()
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def externalsIncluded(self) -> bool:
        """
        @see ghidra.program.model.block.CodeBlockModel#externalsIncluded()
        """
        ...

    def getBaseSubroutineModel(self) -> ghidra.program.model.block.SubroutineBlockModel:
        """
        @see ghidra.program.model.block.SubroutineBlockModel#getBaseSubroutineModel()
        """
        ...

    def getBasicBlockModel(self) -> ghidra.program.model.block.CodeBlockModel:
        """
        @see ghidra.program.model.block.CodeBlockModel#getBasicBlockModel()
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getCodeBlockAt(self, addr: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.block.CodeBlock:
        """
        @see ghidra.program.model.block.CodeBlockModel#getCodeBlockAt(ghidra.program.model.address.Address, ghidra.util.task.TaskMonitor)
        """
        ...

    def getCodeBlocks(self, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.block.CodeBlockIterator:
        """
        @see ghidra.program.model.block.CodeBlockModel#getCodeBlocks(ghidra.util.task.TaskMonitor)
        """
        ...

    @overload
    def getCodeBlocksContaining(self, addr: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> List[ghidra.program.model.block.CodeBlock]:
        """
        Get all the Code Blocks containing the address.
         For model-P, there is only one.
        @param addr Address to find a containing block.
        @param monitor task monitor which allows user to cancel operation.
        @return A CodeBlock array with one entry containing the subroutine that
                      contains the address null otherwise.
        @throws CancelledException if the monitor cancels the operation.
        """
        ...

    @overload
    def getCodeBlocksContaining(self, addrSet: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.block.CodeBlockIterator:
        """
        Get an iterator over CodeBlocks which overlap the specified address set.
        @param addrSet an address set within program
        @param monitor task monitor which allows user to cancel operation.
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
        Get the (first) Model-P subroutine that contains the address.
         This is equivalent to getCodeBlocksContaining(addr) except that
         it doesn't return an array since model-P subroutines don't share code.
        @param addr Address to find a containing block.
        @param monitor task monitor which allows user to cancel operation.
        @return A CodeBlock if any block contains the address.
                 empty array otherwise.
        @throws CancelledException if the monitor cancels the operation.
        """
        ...

    def getFlowType(self, block: ghidra.program.model.block.CodeBlock) -> ghidra.program.model.symbol.FlowType:
        """
        Return in general how things flow out of this node.
         This method exists for the SIMPLEBLOCK model.

         <p>
         Since it doesn't make a great deal of sense to ask for this method
         in the case of subroutines, we return FlowType.UNKNOWN
         as long as the block exists.</p>

         <p>
         If this block has no valid instructions, it can't flow,
         so FlowType.INVALID is returned.</p>
        @return flow type of this node
        """
        ...

    def getListing(self) -> ghidra.program.model.listing.Listing:
        """
        Returns the listing associated with this block model.
        @return the listing associated with this block model
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
        Get number of destination references flowing out of this subroutine (block).
         All Calls from this block, and all external FlowType block references
         from this block are counted.
        @param block code block to get the number of destination references from.
        @param monitor task monitor which allows user to cancel operation.
        @throws CancelledException if the monitor cancels the operation.
        """
        ...

    def getNumSources(self, block: ghidra.program.model.block.CodeBlock, monitor: ghidra.util.task.TaskMonitor) -> int:
        """
        Get number of block source references flowing into this block.
        @param block code block to get the source iterator for.
        @param monitor task monitor which allows user to cancel operation.
        @throws CancelledException if the monitor cancels the operation.
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
    def baseSubroutineModel(self) -> ghidra.program.model.block.SubroutineBlockModel: ...

    @property
    def basicBlockModel(self) -> ghidra.program.model.block.CodeBlockModel: ...

    @property
    def listing(self) -> ghidra.program.model.listing.Listing: ...

    @property
    def name(self) -> unicode: ...

    @property
    def program(self) -> ghidra.program.model.listing.Program: ...
