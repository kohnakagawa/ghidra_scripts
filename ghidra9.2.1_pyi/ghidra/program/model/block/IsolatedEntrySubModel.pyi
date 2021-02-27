from typing import List
import ghidra.program.model.address
import ghidra.program.model.block
import ghidra.program.model.listing
import ghidra.program.model.symbol
import ghidra.util.task
import java.lang


class IsolatedEntrySubModel(ghidra.program.model.block.OverlapCodeSubModel):
    """
    IsolatedEntryCodeSubModel (S-model) defines subroutines with a
     unique entry point, which may share code with other subroutines. Each entry-
     point may either be a source or called entry-point and is identified using
     the MultEntSubModel. This model extends the OverlapCodeSubModel, redefining
     the set of addresses contained within each subroutine. Unlike the
     OverlapCodeSubModel, the address set of a IsolatedEntryCodeSubModel
     subroutine is permitted to span entry-points of other subroutines based upon
     the possible flows from its entry- point.
    """

    ISOLATED_MODEL_NAME: unicode = u'Isolated Entry'



    @overload
    def __init__(self, program: ghidra.program.model.listing.Program):
        """
        Construct a <CODE>IsolatedEntrySubModel</CODE> subroutine on a program.
        @param program program to create blocks from.
        """
        ...

    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, includeExternals: bool):
        """
        Construct a <CODE>IsolatedEntrySubModel</CODE> subroutine on a program.
        @param program program to create blocks from.
        @param includeExternals externals are included if true
        """
        ...



    def allowsBlockOverlap(self) -> bool:
        """
        @see ghidra.program.model.block.CodeBlockModel#allowsBlockOverlap()
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def externalsIncluded(self) -> bool: ...

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
         Model-O is the only of the MOP models that allows for there to be more than one
        @param addr Address to find a containing block.
        @param monitor task monitor which allows user to cancel operation.
        @return A CodeBlock array with one entry containing the subroutine that
                      contains the address empty array otherwise.
        @throws CancelledException if the monitor cancels the operation.
        """
        ...

    @overload
    def getCodeBlocksContaining(self, addrSet: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.block.CodeBlockIterator:
        """
        @see ghidra.program.model.block.CodeBlockModel#getCodeBlocksContaining(ghidra.program.model.address.AddressSetView, ghidra.util.task.TaskMonitor)
        """
        ...

    def getDestinations(self, block: ghidra.program.model.block.CodeBlock, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.block.CodeBlockReferenceIterator:
        """
        @see ghidra.program.model.block.CodeBlockModel#getDestinations(ghidra.program.model.block.CodeBlock, ghidra.util.task.TaskMonitor)
        """
        ...

    def getFirstCodeBlockContaining(self, addr: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.block.CodeBlock:
        """
        @see ghidra.program.model.block.CodeBlockModel#getFirstCodeBlockContaining(ghidra.program.model.address.Address, ghidra.util.task.TaskMonitor)
        """
        ...

    def getFlowType(self, block: ghidra.program.model.block.CodeBlock) -> ghidra.program.model.symbol.FlowType:
        """
        Return in general how things flow out of this node.
         This method exists for the SIMPLEBLOCK model.

         <p>
         Since it doesn't make a great deal of sense to ask for this method
         in the case of subroutines, we return FlowType.UNKNOWN
         as long as the block exists.

         <p>
         If this block has no valid instructions, it can't flow,
         so FlowType.INVALID is returned.
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
        @see ghidra.program.model.block.CodeBlockModel#getNumDestinations(ghidra.program.model.block.CodeBlock, ghidra.util.task.TaskMonitor)
        """
        ...

    def getNumSources(self, block: ghidra.program.model.block.CodeBlock, monitor: ghidra.util.task.TaskMonitor) -> int:
        """
        @see ghidra.program.model.block.CodeBlockModel#getNumSources(ghidra.program.model.block.CodeBlock, ghidra.util.task.TaskMonitor)
        """
        ...

    def getProgram(self) -> ghidra.program.model.listing.Program:
        """
        @see ghidra.program.model.block.CodeBlockModel#getProgram()
        """
        ...

    def getSources(self, block: ghidra.program.model.block.CodeBlock, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.block.CodeBlockReferenceIterator:
        """
        @see ghidra.program.model.block.CodeBlockModel#getSources(ghidra.program.model.block.CodeBlock, ghidra.util.task.TaskMonitor)
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
    def name(self) -> unicode: ...
