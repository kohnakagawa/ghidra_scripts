import ghidra.framework.cmd
import ghidra.framework.model
import ghidra.util.task
import java.lang


class CreateDataInStructureBackgroundCmd(ghidra.framework.cmd.BackgroundCommand):
    """
    Background command to create data across a selection inside of a structure.
    """





    @overload
    def __init__(self, addr: ghidra.program.model.address.Address, startPath: List[int], length: int, dt: ghidra.program.model.data.DataType):
        """
        Constructs a command for applying dataTypes within an existing structure
         across a range of components.
         Simple pointer conversion will NOT be performed.
        @param addr The address of the existing structure.
        @param startPath the componentPath where to begin applying the datatype.
        @param length the number of bytes to apply the data type to.
        @param dt the datatype to be applied to the range of components.
        """
        ...

    @overload
    def __init__(self, addr: ghidra.program.model.address.Address, startPath: List[int], length: int, dt: ghidra.program.model.data.DataType, stackPointers: bool):
        """
        This is the same as {@link #CreateDataInStructureBackgroundCmd(Address, int[], int, DataType )} except that
         it allows the caller to control whether or not a pointer data type is created when a
         non-pointer data type is applied at a location that previously contained a pointer data
         type.
        @param addr The address of the existing structure.
        @param startPath the componentPath where to begin applying the datatype.
        @param length the number of bytes to apply the data type to.
        @param dt the datatype to be applied to the range of components.
        @param stackPointers True will convert the given data type to a pointer if it is not one
         and the previous type was a pointer; false will not make this conversion
        """
        ...



    @overload
    def applyTo(self, obj: ghidra.framework.model.DomainObject) -> bool: ...

    @overload
    def applyTo(self, obj: ghidra.framework.model.DomainObject, monitor: ghidra.util.task.TaskMonitor) -> bool:
        """
        @see ghidra.framework.cmd.BackgroundCommand#applyTo(ghidra.framework.model.DomainObject, ghidra.util.task.TaskMonitor)
        """
        ...

    def canCancel(self) -> bool:
        """
        Check if the command can be canceled.
        @return true if this command can be canceled
        """
        ...

    def dispose(self) -> None:
        """
        Called when this command is going to be removed/canceled without
         running it.  This gives the command the opportunity to free any
         temporary resources it has hold of.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode: ...

    def getStatusMsg(self) -> unicode: ...

    def hasProgress(self) -> bool:
        """
        Check if the command provides progress information.
        @return true if the command shows progress information
        """
        ...

    def hashCode(self) -> int: ...

    def isModal(self) -> bool:
        """
        Check if the command requires the monitor to be modal.  No other
         command should be allowed, and the GUI will be locked.
        @return true if no other operation should be going on while this
         command is in progress.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def taskCompleted(self) -> None:
        """
        Called when the task monitor is completely done with indicating progress.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
