import ghidra.program.model.block
import ghidra.util.task
import java.lang


class SubroutineDestReferenceIterator(object, ghidra.program.model.block.CodeBlockReferenceIterator):
    """
    SubroutineDestReferenceIterator is a unidirectional iterator over
     the destination CodeBlockReferences for a CodeBlock.
    """





    def __init__(self, block: ghidra.program.model.block.CodeBlock, monitor: ghidra.util.task.TaskMonitor):
        """
        Construct an Iterator over Destination blocks for a CodeBlock.
         External references will be ignored.
        @param block block to get destination blocks for.  This should be a
         subroutine obtained from PartitionCodeSubModel.
        @param monitor task monitor which allows user to cancel operation.
        @throws CancelledException if the monitor cancels the operation.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getNumDestinations(block: ghidra.program.model.block.CodeBlock, monitor: ghidra.util.task.TaskMonitor) -> int:
        """
        Get number of destination references flowing out of this subroutine (block).
         All Calls from this block, and all external FlowType block references
         from this block are counted.
        @param block code block to get the number of destination references from.
        @param monitor task monitor
        """
        ...

    def hasNext(self) -> bool:
        """
        @see ghidra.program.model.block.CodeBlockReferenceIterator#hasNext()
        """
        ...

    def hashCode(self) -> int: ...

    def next(self) -> ghidra.program.model.block.CodeBlockReference:
        """
        @see ghidra.program.model.block.CodeBlockReferenceIterator#next()
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
