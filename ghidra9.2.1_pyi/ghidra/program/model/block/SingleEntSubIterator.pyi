import ghidra.program.model.block
import java.lang


class SingleEntSubIterator(object, ghidra.program.model.block.CodeBlockIterator):
    """
    SingleEntSubIterator is an implementation of
     CodeBlockIterator capable of iterating in
     the forward direction over subroutine code blocks.
     This iterator supports subroutine models which allow only one
     called/source entry point within a subroutine and may
     share code with other subroutines produced by the same model.
     All entry points must be accounted for within M-Model subroutines.

     NOTE: This iterator only supports OverlapCodeSubModel block models
     and extensions.

     NOTE: If the containing M-model subroutine has two entry points, say
     A and B, such that the code traversed from A is identical to the code traversed
     by B (due to a cycle), then this iterator will include it twice rather than
     skipping over the identical address set.  This is because the iterator works by
     iterating through M-model subroutines, and wherever M-model subroutines have
     n  1 multiple entry points, the iterator produces an O-model subroutine
     for every one of the entry points.
    """





    @overload
    def __init__(self, model: ghidra.program.model.block.OverlapCodeSubModel, monitor: ghidra.util.task.TaskMonitor):
        """
        Creates a new iterator that will iterate over the entire
         program starting from its current minimum address.
        @param model the BlockModel the iterator will use in its operations.
        @param monitor task monitor which allows user to cancel operation.
        @throws CancelledException if the monitor cancels the operation.
        """
        ...

    @overload
    def __init__(self, model: ghidra.program.model.block.OverlapCodeSubModel, set: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor):
        """
        Creates a new iterator that will iterate over the
         program within a given address range set. All blocks which
         overlap the address set will be returned.
         <P>
        @param model the BlockModel the iterator will use in its operations.
        @param set the address range set which the iterator is to be
                       restricted to.
        @param monitor task monitor which allows user to cancel operation.
        @throws CancelledException if the monitor cancels the operation.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hasNext(self) -> bool:
        """
        @see ghidra.program.model.block.CodeBlockIterator#hasNext()
        """
        ...

    def hashCode(self) -> int: ...

    def next(self) -> ghidra.program.model.block.CodeBlock:
        """
        @see ghidra.program.model.block.CodeBlockIterator#next()
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
