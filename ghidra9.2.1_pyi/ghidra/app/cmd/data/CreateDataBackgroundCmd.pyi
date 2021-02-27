import ghidra.framework.cmd
import ghidra.framework.model
import ghidra.util.task
import java.lang


class CreateDataBackgroundCmd(ghidra.framework.cmd.BackgroundCommand):
    """
    This command will create a data of type dataType throughout an addressSet.
     If there are any existing
     instructions in the area to be made into data, the command will fail.  Any data
     in the area will be replaced with the new dataType, except when the existing data
     or the given dataType is a pointer.  If the existing dataType is a pointer, then
     it will be changed into a pointer to the given dataType.  If the given dataType
     is a pointer and the existing data is = to the size of a pointer, it will become
     a pointer to the existing type.  If the existing dataType is less than the size
     of a pointer, then a pointer to dataType will only be created if there are
     enough undefined bytes following to make a pointer.
    """





    @overload
    def __init__(self, addrSet: ghidra.program.model.address.AddressSetView, dataType: ghidra.program.model.data.DataType):
        """
        Constructs a command for applying a dataType to a set of addresses.
         Simple pointer conversion will NOT be performed.
        @param addrSet The address set to fill with the given dataType.
        @param dataType the dataType to be applied to the address set.
        """
        ...

    @overload
    def __init__(self, addrSet: ghidra.program.model.address.AddressSetView, dataType: ghidra.program.model.data.DataType, stackPointers: bool):
        """
        This is the same as {@link #CreateDataBackgroundCmd(AddressSetView, DataType)} except that
         it allows the caller to control whether or not a pointer data type is created when a
         non-pointer data type is applied at a location that previously contained a pointer data
         type.
        @param addrSet The address set to fill with the given dataType.
        @param dataType the dataType to be applied to the address set.
        @param stackPointers if true simple pointer conversion is enabled
         (see {@link DataUtilities#reconcileAppliedDataType(DataType, DataType, boolean)}).
        """
        ...



    @overload
    def applyTo(self, obj: ghidra.framework.model.DomainObject) -> bool: ...

    @overload
    def applyTo(self, obj: ghidra.framework.model.DomainObject, monitor: ghidra.util.task.TaskMonitor) -> bool: ...

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

    def doApplyTo(self, obj: ghidra.framework.model.DomainObject, monitor: ghidra.util.task.TaskMonitor) -> bool: ...

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
