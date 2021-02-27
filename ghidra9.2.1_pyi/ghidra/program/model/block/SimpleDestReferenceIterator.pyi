import ghidra.program.model.block
import ghidra.util.task
import java.lang


class SimpleDestReferenceIterator(object, ghidra.program.model.block.CodeBlockReferenceIterator):
    """
    This iterator is implemented by getting the flows from the instruction
      and iterating over those flows (plus the fallthrough).  This is probably
      not the most efficient method.  An linked-list of references has to be created each
      time we want to get the destinations from a block.
    """





    def __init__(self, block: ghidra.program.model.block.CodeBlock, followIndirectFlows: bool, monitor: ghidra.util.task.TaskMonitor):
        """
        Construct an Iterator over Destination blocks for a CodeBlock.
         External references are ignored.
        @param block block to get destination blocks for.  This should be a
         block obtained from SimpleBlockModel.
        @param followIndirectFlows indirect references will only be included if true
        @param monitor task monitor which allows user to cancel operation.
        @throws CancelledException if the monitor cancels the operation.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getNumDestinations(block: ghidra.program.model.block.CodeBlock, followIndirectFlows: bool, monitor: ghidra.util.task.TaskMonitor) -> int:
        """
        Get number of destination references flowing out of this block.
         All Calls from this block, and all external FlowType block references
         from this block are ignored.
        @param block code block to get the number of destination references from.
        @param followIndirectFlows indirect references will only be included if true
        @param monitor task monitor which allows user to cancel operation.
        @throws CancelledException if the monitor cancels the operation.
        @deprecated this method should be avoided since it repeats the work of the iterator
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
