import ghidra.app.cmd.data
import ghidra.framework.model
import ghidra.program.model.data
import java.lang


class CreateStructureCmd(ghidra.app.cmd.data.AbstractCreateStructureCmd):
    """
    Command to create a structure.
    """





    @overload
    def __init__(self, address: ghidra.program.model.address.Address, length: int):
        """
        Constructs a new command for creating a new structure and applying it to
         the browser.  This method simply calls
         {@link #CreateStructureCmd(String, Address, int)} with
         {@link ghidra.program.model.data.StructureFactory#DEFAULT_STRUCTURE_NAME} as the name of the structure.
        @param address the address at which to create the new structure.
        @param length the number of undefined bytes to consume in the new
                structure.
        """
        ...

    @overload
    def __init__(self, newStructure: ghidra.program.model.data.Structure, address: ghidra.program.model.address.Address):
        """
        Creates a new structure by using the provided structure and attaching
         it to the program passed in the {@link #applyTo(DomainObject)} method.
        @param newStructure The new structure to attach to the program
                provided in the {@link #applyTo(DomainObject)} method.
        @param address the address at which to create the new structure.
        """
        ...

    @overload
    def __init__(self, name: unicode, address: ghidra.program.model.address.Address, length: int):
        """
        Constructs a new command for creating a new structure and applying it to
         the browser.
        @param name The name of the new structure to create.
        @param address the address at which to create the new structure.
        @param length the number of undefined bytes to consume in the new
                structure.
        """
        ...



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
