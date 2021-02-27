import ghidra.program.model.block
import java.lang


class SimpleBlockIterator(object, ghidra.program.model.block.CodeBlockIterator):
    """
    SimpleBlockIterator is an implementation of
     CodeBlockIterator capable of iterating in
     the forward direction over "simple blocks".
    """





    @overload
    def __init__(self, model: ghidra.program.model.block.SimpleBlockModel, monitor: ghidra.util.task.TaskMonitor):
        """
        Creates a new iterator that will iterate over the entire
         program starting from its current minimum address.
         <P>
        @param model the BlockModel the iterator will use in its operations.
        @param monitor task monitor which allows user to cancel operation.
        @throws CancelledException if the monitor cancels the operation.
        """
        ...

    @overload
    def __init__(self, model: ghidra.program.model.block.SimpleBlockModel, set: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor):
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
