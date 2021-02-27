import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.util.classfinder
import ghidra.util.task
import java.lang
import java.util.function


class DataTypeReferenceFinder(ghidra.util.classfinder.ExtensionPoint, object):
    """
    An interface for extension points to implement.  Implementations know how to find data type
     references.

     Implementation class names must end with DataTypeReferenceFinder
    """









    def equals(self, __a0: object) -> bool: ...

    @overload
    def findReferences(self, program: ghidra.program.model.listing.Program, dataType: ghidra.program.model.data.DataType, callback: java.util.function.Consumer, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Finds references in the current program in a manner appropriate with the given
         implementation.
         <p>
         Note that this operation is multi-threaded and that results will be delivered as they
         are found via the <code>callback</code>.
        @param program the program to search
        @param dataType the type for which to search
        @param callback the callback to be called when a reference is found
        @param monitor the monitor that allows for progress and cancellation
        @throws CancelledException if the operation was cancelled
        """
        ...

    @overload
    def findReferences(self, program: ghidra.program.model.listing.Program, composite: ghidra.program.model.data.Composite, fieldName: unicode, callback: java.util.function.Consumer, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Finds references in the current program to specific field of the given {@link Composite} type
         in a manner appropriate with the given implementation.
         <p>
         Note that this operation is multi-threaded and that results will be delivered as they
         are found via the <code>callback</code>.
        @param program the program to search
        @param composite the type containing the field for which to search
        @param fieldName the name of the composite's field for which to search
        @param callback the callback to be called when a reference is found
        @param monitor the monitor that allows for progress and cancellation
        @throws CancelledException if the operation was cancelled
        """
        ...

    def getClass(self) -> java.lang.Class: ...

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
