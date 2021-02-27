import ghidra.program.model.block
import ghidra.util.task
import java.lang


class SimpleSourceReferenceIterator(object, ghidra.program.model.block.CodeBlockReferenceIterator):
    """
    SimpleSourceReferenceIterator is a unidirectional iterator over the CodeBlockReferences
     for a CodeBlock.  It is not failfast, whenever hasNext()
     are called it will find if there is a next CodeBlockReference and acquire
     a handle if there is one. If new code units are added to the listing after
     the iterator is created it will find them as it scans ahead.
    """





    def __init__(self, block: ghidra.program.model.block.CodeBlock, followIndirectFlows: bool, monitor: ghidra.util.task.TaskMonitor):
        """
        Construct an Iterator over Source blocks for a CodeBlock.
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
    def getNumSources(block: ghidra.program.model.block.CodeBlock, followIndirectFlows: bool, monitor: ghidra.util.task.TaskMonitor) -> int:
        """
        Get number of source references flowing from this subroutine (block).
         All Calls to this block, and all external FlowType block references
         to this block are counted.
        @param block code block to get the number of source references to.
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
