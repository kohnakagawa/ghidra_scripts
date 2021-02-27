import ghidra.app.context
import ghidra.program.model.data
import java.lang


class DataService(object):
    """
    Data Creation service.

     NOTE: This version is dependant on the currentProgram of the implementing
     plugin class. If you want a version that is not dependant on it, please use
     DataCreationService
    """









    def createData(self, dt: ghidra.program.model.data.DataType, context: ghidra.app.context.ListingActionContext, enableConflictHandling: bool) -> bool:
        """
        Apply the given data type at a location.
        @param dt dataType to create at the location
        @param context the context containing program, location, and selection information
        @param enableConflictHandling if true, the service may prompt the user to resolve data conflicts
        @return true if the data could be created at the current location
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isCreateDataAllowed(self, context: ghidra.app.context.ListingActionContext) -> bool:
        """
        Determine if create data is permitted on the specified location. If the
         location is contained within the current program selection, the entire
         selection is examined.
        @param context the context containing program, location, and selection information
        @return true if create data is allowed, else false.
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
