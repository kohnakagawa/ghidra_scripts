import ghidra.framework.cmd
import ghidra.framework.model
import ghidra.program.model.data
import java.lang


class AbstractCreateStructureCmd(object, ghidra.framework.cmd.Command):
    """
    A base class to hold duplicate information for commands that create
     structures.  This class implements the logic of the
     #applyTo(DomainObject) method so that child implementations need
     only to implement the abstract methods.
    """









    def applyTo(self, domainObject: ghidra.framework.model.DomainObject) -> bool:
        """
        Applies this command to the given domain object.
         <p>
         This method is a Form Template method in that child subclasses do not
         need to override the method, but only need to implement the methods
         that this method calls.
        @param domainObject The domain object that is associated with this
                command
        @see Command#applyTo(DomainObject)
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode:
        """
        @see ghidra.framework.cmd.Command#getName()
        """
        ...

    def getNewDataType(self) -> ghidra.program.model.data.DataType:
        """
        Get the new structure data type which was created.
        @return new structure.
        """
        ...

    def getStatusMsg(self) -> unicode:
        """
        @see ghidra.framework.cmd.Command#getStatusMsg()
        """
        ...

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

    @property
    def name(self) -> unicode: ...

    @property
    def newDataType(self) -> ghidra.program.model.data.DataType: ...

    @property
    def statusMsg(self) -> unicode: ...
