import ghidra.app.cmd.memory
import ghidra.framework.model
import java.lang


class AddByteMappedMemoryBlockCmd(ghidra.app.cmd.memory.AbstractAddMemoryBlockCmd):
    """
    Command for adding byte-mapped memory blocks
    """





    @overload
    def __init__(self, name: unicode, comment: unicode, source: unicode, start: ghidra.program.model.address.Address, length: long, read: bool, write: bool, execute: bool, isVolatile: bool, mappedAddress: ghidra.program.model.address.Address, isOverlay: bool):
        """
        Create a new AddByteMappedMemoryBlockCmd with 1:1 byte mapping scheme
        @param name the name for the new memory block.
        @param comment the comment for the block
        @param source indicates what is creating the block
        @param start the start address for the the block
        @param length the length of the new block
        @param read sets the block's read permission flag
        @param write sets the block's write permission flag
        @param execute sets the block's execute permission flag
        @param isVolatile sets the block's volatile flag
        @param mappedAddress the address in memory that will serve as the bytes source for the block
        @param isOverlay if true, the block will be created in a new overlay address space.
        """
        ...

    @overload
    def __init__(self, name: unicode, comment: unicode, source: unicode, start: ghidra.program.model.address.Address, length: long, read: bool, write: bool, execute: bool, isVolatile: bool, mappedAddress: ghidra.program.model.address.Address, byteMappingScheme: ghidra.program.database.mem.ByteMappingScheme, isOverlay: bool):
        """
        Create a new AddByteMappedMemoryBlockCmd with a specified byte mapping scheme.
         Byte mapping scheme is specified by two values schemeDestByteCount and schemeSrcByteCount which
         may be viewed as a ratio of number of destination bytes to number of mapped source bytes.
         When the destination consumes bytes from the mapped source it consume schemeDestByteCount bytes then
         skips (schemeSrcByteCount - schemeDestByteCount) bytes before repeating the mapping sequence over
         the extent of the destination block.  The block start address and source mappedAddress must
         be chosen carefully as they relate to the mapping scheme when it is anything other than 1:1.
        @param name the name for the new memory block.
        @param comment the comment for the block
        @param source indicates what is creating the block
        @param start the start address for the the block
        @param length the length of the new block
        @param read sets the block's read permission flag
        @param write sets the block's write permission flag
        @param execute sets the block's execute permission flag
        @param isVolatile sets the block's volatile flag
        @param mappedAddress the address in memory that will serve as the bytes source for the block
        @param byteMappingScheme byte mapping scheme (may be null for 1:1 mapping)
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
