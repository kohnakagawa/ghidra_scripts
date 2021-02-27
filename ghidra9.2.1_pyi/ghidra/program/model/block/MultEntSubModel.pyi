from typing import List
import ghidra.program.model.address
import ghidra.program.model.block
import ghidra.program.model.listing
import ghidra.program.model.symbol
import ghidra.util.task
import java.lang


class MultEntSubModel(object, ghidra.program.model.block.SubroutineBlockModel):
    """
    MultEntSubModel (M-model) defines subroutines which do not share code with
     any other subroutine and may have one or more entry points. Each entry-
     points represent either a source or called entry-point.

     MODEL-M subroutines should be used to determine which subroutine(s) contains
     a particular instruction.
     Since model-M subroutines yield the largest subroutines, they should be particular useful
     in the process of program slicing -- the process of splitting the program into modules
     or subroutine cliques -- in order to begin to understand the structure and functionality
     of the program.
    """

    NAME: unicode = u'Multiple Entry'
    emptyBlockArray: List[ghidra.program.model.block.CodeBlock] = array(ghidra.program.model.block.CodeBlock)



    @overload
    def __init__(self, program: ghidra.program.model.listing.Program):
        """
        Construct a <CODE>MultEntSubModel</CODE> for a program.
        @param program program to create blocks from.
        """
        ...

    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, includeExternals: bool):
        """
        Construct a <CODE>MultEntSubModel</CODE> for a program.
        @param program program to create blocks from.
        @param includeExternals external blocks will be included if true
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

    def getAddressSet(self, block: ghidra.program.model.block.CodeBlock) -> ghidra.program.model.address.AddressSetView:
        """
        Compute an address set that represents all the addresses contained
          in all instructions that are part of this block
        @param block code block to compute address set for.
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
        Get the code block that has an entry point at addr.
        @param addr one of the entry points for a Model-M subroutine
        @param monitor task monitor which allows user to cancel operation.
        @return null if there is no subroutine with an entry at addr.
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
        Returns the one code block contained by addr (only for
          a model that has shared subroutines would this method
          return more than one code block)
        @param addr Address to find a containing block.
        @param monitor task monitor which allows user to cancel operation.
        @return A CodeBlock if any block contains the address.
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
        @see ghidra.program.model.block.CodeBlockModel#getDestinations(ghidra.program.model.block.CodeBlock, ghidra.util.task.TaskMonitor)
        """
        ...

    def getFirstCodeBlockContaining(self, addr: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.block.CodeBlock:
        """
        Get the MultEntSubModel Code Block that contains the address.
        @param addr Address to find a containing block.
        @param monitor task monitor which allows user to cancel operation.
        @return A CodeBlock if any block contains the address.
                 null otherwise.
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
        @return the listing associated with this block model.
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
    def baseSubroutineModel(self) -> ghidra.program.model.block.SubroutineBlockModel: ...

    @property
    def basicBlockModel(self) -> ghidra.program.model.block.CodeBlockModel: ...

    @property
    def listing(self) -> ghidra.program.model.listing.Listing: ...

    @property
    def name(self) -> unicode: ...

    @property
    def program(self) -> ghidra.program.model.listing.Program: ...
