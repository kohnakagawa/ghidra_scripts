import ghidra.framework.cmd
import ghidra.framework.model
import java.lang


class CreateArrayInStructureCmd(object, ghidra.framework.cmd.Command):
    """
    Command to create an array inside of a structure.
    """





    def __init__(self, addr: ghidra.program.model.address.Address, numElements: int, dt: ghidra.program.model.data.DataType, compPath: List[int]):
        """
        Constructs a new command for creating arrays inside of structures.
        @param addr The address of the structure that will contain the new array.
        @param numElements the number of elements in the array to be created.
        @param dt the dataType of the elements in the array to be created.
        @param compPath the component path within the structure at which to create
         the array. The component path is an array of integers where each integer
         is a component index of the component above it.
        """
        ...



    def applyTo(self, obj: ghidra.framework.model.DomainObject) -> bool:
        """
        @see ghidra.framework.cmd.Command#applyTo(ghidra.framework.model.DomainObject)
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode:
        """
        @see ghidra.framework.cmd.Command#getName()
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
    def statusMsg(self) -> unicode: ...
