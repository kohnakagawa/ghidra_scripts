import ghidra.program.model.block
import ghidra.util.task
import java.lang


class SubroutineSourceReferenceIterator(object, ghidra.program.model.block.CodeBlockReferenceIterator):
    """
    SubroutineSourceReferenceIterator is a unidirectional iterator over
     the source CodeBlockReferences for a CodeBlock.
    """





    def __init__(self, block: ghidra.program.model.block.CodeBlock, monitor: ghidra.util.task.TaskMonitor):
        """
        Construct an Iterator over Source blocks for a CodeBlock.
        @param block block to get destination blocks for.  This should be a
         subroutine obtained from SubroutineBlockModel.
        @param monitor task monitor which allows user to cancel operation.
        @throws CancelledException if the monitor cancels the operation.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getNumSources(block: ghidra.program.model.block.CodeBlock, monitor: ghidra.util.task.TaskMonitor) -> int:
        """
        Get number of source references flowing from this subroutine (block).
         All Calls to this block, and all external FlowType block references
         to this block are counted.
        @param block code block to get the number of source references to.
        @param monitor task monitor which allows user to cancel operation.
        @throws CancelledException if the monitor cancels the operation.
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
