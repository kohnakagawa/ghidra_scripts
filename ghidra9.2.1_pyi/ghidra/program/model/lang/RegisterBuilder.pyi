import ghidra.program.model.address
import ghidra.program.model.lang
import java.lang


class RegisterBuilder(object):




    def __init__(self): ...



    def addLaneSize(self, registerName: unicode, laneSizeInBytes: int) -> bool:
        """
        Add a vector lane size to the specified register.
        @param registerName register name
        @param laneSizeInBytes the size of the lane to add in bytes
        @return true if register was found, else false
        @throws UnsupportedOperationException if register is unable to support the definition of
         lanes.
        @throws IllegalArgumentException if {@code laneSizeInBytes} is invalid
        """
        ...

    @overload
    def addRegister(self, register: ghidra.program.model.lang.Register) -> None: ...

    @overload
    def addRegister(self, name: unicode, description: unicode, address: ghidra.program.model.address.Address, numBytes: int, bigEndian: bool, typeFlags: int) -> None: ...

    @overload
    def addRegister(self, name: unicode, description: unicode, address: ghidra.program.model.address.Address, numBytes: int, leastSignificantBit: int, bitLength: int, bigEndian: bool, typeFlags: int) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getProcessContextAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the processor context address of the first
         context register added to this builder.
        @return context address
        """
        ...

    def getRegister(self, name: unicode) -> ghidra.program.model.lang.Register:
        """
        Returns the register with the given name;
        @param name the name of the register to retrieve
        @return register or null if not found
        """
        ...

    def getRegisterManager(self) -> ghidra.program.model.lang.RegisterManager:
        """
        Compute current register collection and instantiate a {@link RegisterManager}
        @return new register manager instance
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def renameRegister(self, oldName: unicode, newName: unicode) -> bool:
        """
        Rename a register.  This allows generic register names declared within the langauge
         specification (*.slaspec) to be renamed for a processor variant specification (*.pspec).
        @param oldName original register name
        @param newName new register name
        @return true if rename was successful, else false
        """
        ...

    def setFlag(self, registerName: unicode, registerFlag: int) -> bool:
        """
        Set a register flag for the specified register
        @param registerName register name
        @param registerFlag Register defined flag bit(s)
        @return true if register was found, else false
        """
        ...

    def setGroup(self, registerName: unicode, groupName: unicode) -> bool:
        """
        Set the group name for the specified register
        @param registerName register name
        @param groupName group name
        @return true if register was found, else false
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def processContextAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def registerManager(self) -> ghidra.program.model.lang.RegisterManager: ...
