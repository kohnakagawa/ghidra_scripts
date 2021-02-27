import ghidra.app.cmd.data
import ghidra.framework.model
import ghidra.program.model.data
import java.lang


class CreateStructureInStructureCmd(ghidra.app.cmd.data.AbstractCreateStructureCmd):
    """
    Command to create a structure inside of another structure.
    """





    @overload
    def __init__(self, address: ghidra.program.model.address.Address, fromPath: List[int], toPath: List[int]):
        """
        Constructs a new command for creating structures inside other structures.
        @param address the address of the outer-most structure.
        @param fromPath the componentPath of the first component to be consumed in
         the new structure.
        @param toPath the componentPath of the second component to be consumed in the
         the new structure.
        """
        ...

    @overload
    def __init__(self, name: unicode, addr: ghidra.program.model.address.Address, fromPath: List[int], toPath: List[int]):
        """
        Constructs a new command for creating structures inside other structures.
        @param name The name of the structure.
        @param addr the address of the outer-most structure.
        @param fromPath the componentPath of the first component to be consumed in
         the new structure.
        @param toPath the componentPath of the second component to be consumed in the
         the new structure.
        """
        ...

    @overload
    def __init__(self, newStructure: ghidra.program.model.data.Structure, address: ghidra.program.model.address.Address, fromPath: List[int], toPath: List[int]): ...



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
