import ghidra.app.cmd.memory
import ghidra.framework.model
import java.lang


class AddInitializedMemoryBlockCmd(ghidra.app.cmd.memory.AbstractAddMemoryBlockCmd):
    """
    Command for adding a new memory block initialized with a specific byte.
    """





    def __init__(self, name: unicode, comment: unicode, source: unicode, start: ghidra.program.model.address.Address, length: long, read: bool, write: bool, execute: bool, isVolatile: bool, initialValue: int, isOverlay: bool):
        """
        Create a new AddFileBytesMemoryBlockCmd
        @param name the name for the new memory block.
        @param comment the comment for the block
        @param source indicates what is creating the block
        @param start the start address for the the block
        @param length the length of the new block
        @param read sets the block's read permission flag
        @param write sets the block's write permission flag
        @param execute sets the block's execute permission flag
        @param isVolatile sets the block's volatile flag
        @param initialValue the bytes value to use throught the new block.
        @param isOverlay if true, the block will be created in a new overlay address space.
        """
        ...



    def applyTo(self, obj: ghidra.framework.model.DomainObject) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode: ...

    def getStatusMsg(self) -> unicode: ...

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
