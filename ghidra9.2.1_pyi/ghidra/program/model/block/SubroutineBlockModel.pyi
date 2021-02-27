from typing import List
import ghidra.program.model.address
import ghidra.program.model.block
import ghidra.program.model.listing
import ghidra.program.model.symbol
import ghidra.util.task
import java.lang


class SubroutineBlockModel(ghidra.program.model.block.CodeBlockModel, object):
    """
    Subroutine block model.
    """

    emptyBlockArray: List[ghidra.program.model.block.CodeBlock] = array(ghidra.program.model.block.CodeBlock)







    def allowsBlockOverlap(self) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def externalsIncluded(self) -> bool: ...

    def getBaseSubroutineModel(self) -> ghidra.program.model.block.SubroutineBlockModel:
        """
        Get the underlying base subroutine model.
         This is generally the MultEntSubModel (M-Model).
        @return base subroutine model.  If there is no base model,
         this subroutine model is returned.
        """
        ...

    def getBasicBlockModel(self) -> ghidra.program.model.block.CodeBlockModel: ...

    def getClass(self) -> java.lang.Class: ...

    def getCodeBlockAt(self, __a0: ghidra.program.model.address.Address, __a1: ghidra.util.task.TaskMonitor) -> ghidra.program.model.block.CodeBlock: ...

    def getCodeBlocks(self, __a0: ghidra.util.task.TaskMonitor) -> ghidra.program.model.block.CodeBlockIterator: ...

    @overload
    def getCodeBlocksContaining(self, __a0: ghidra.program.model.address.Address, __a1: ghidra.util.task.TaskMonitor) -> List[ghidra.program.model.block.CodeBlock]: ...

    @overload
    def getCodeBlocksContaining(self, __a0: ghidra.program.model.address.AddressSetView, __a1: ghidra.util.task.TaskMonitor) -> ghidra.program.model.block.CodeBlockIterator: ...

    def getDestinations(self, __a0: ghidra.program.model.block.CodeBlock, __a1: ghidra.util.task.TaskMonitor) -> ghidra.program.model.block.CodeBlockReferenceIterator: ...

    def getFirstCodeBlockContaining(self, __a0: ghidra.program.model.address.Address, __a1: ghidra.util.task.TaskMonitor) -> ghidra.program.model.block.CodeBlock: ...

    def getFlowType(self, __a0: ghidra.program.model.block.CodeBlock) -> ghidra.program.model.symbol.FlowType: ...

    @overload
    def getName(self) -> unicode: ...

    @overload
    def getName(self, __a0: ghidra.program.model.block.CodeBlock) -> unicode: ...

    def getNumDestinations(self, __a0: ghidra.program.model.block.CodeBlock, __a1: ghidra.util.task.TaskMonitor) -> int: ...

    def getNumSources(self, __a0: ghidra.program.model.block.CodeBlock, __a1: ghidra.util.task.TaskMonitor) -> int: ...

    def getProgram(self) -> ghidra.program.model.listing.Program: ...

    def getSources(self, __a0: ghidra.program.model.block.CodeBlock, __a1: ghidra.util.task.TaskMonitor) -> ghidra.program.model.block.CodeBlockReferenceIterator: ...

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
    def name(self) -> unicode: ...

    @property
    def program(self) -> ghidra.program.model.listing.Program: ...