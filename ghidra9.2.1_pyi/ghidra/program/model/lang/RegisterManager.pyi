from typing import List
import ghidra.program.model.address
import ghidra.program.model.lang
import java.lang


class RegisterManager(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getContextBaseRegister(self) -> ghidra.program.model.lang.Register:
        """
        Get context base-register
        @return context base register or null if one has not been defined by the language.
        """
        ...

    def getContextRegisters(self) -> List[ghidra.program.model.lang.Register]:
        """
        Get unsorted unmodifiable list of all processor context registers (include base context register and children)
        @return all processor context registers
        """
        ...

    @overload
    def getRegister(self, name: unicode) -> ghidra.program.model.lang.Register:
        """
        Get register by name.  A semi-case-insensitive lookup is performed.
         The specified name must match either the case-sensitive name or
         be entirely lowercase or uppercase.
        @param name register name
        @return register or null if not found
        """
        ...

    @overload
    def getRegister(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.lang.Register:
        """
        Returns the largest register located at the specified address
        @param addr register address
        @return register or null if not found
        """
        ...

    @overload
    def getRegister(self, addr: ghidra.program.model.address.Address, size: int) -> ghidra.program.model.lang.Register:
        """
        Get register by address and size
        @param addr register address
        @param size register size
        @return register or null if not found
        """
        ...

    def getRegisterNames(self) -> List[unicode]:
        """
        Get an alphabetical sorted unmodifiable list of original register names
         (including context registers).  Names correspond to orignal register
         name and not aliases which may be defined.
        @return alphabetical sorted unmodifiable list of original register names.
        """
        ...

    @overload
    def getRegisters(self) -> List[ghidra.program.model.lang.Register]:
        """
        Get all registers as an unsorted unmodifiable list.
        @return unmodifiable list of all registers defined
        """
        ...

    @overload
    def getRegisters(self, addr: ghidra.program.model.address.Address) -> List[ghidra.program.model.lang.Register]:
        """
        Returns all registers located at the specified address
        @param addr register address
        @return array of registers found (may be empty)
        """
        ...

    def getSortedVectorRegisters(self) -> List[ghidra.program.model.lang.Register]:
        """
        Get an unmodifiable list of all vector registers indentified by the processor specification
         in sorted order based upon address and size.
        @return all vector registers as unmodifiable list
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
    def contextBaseRegister(self) -> ghidra.program.model.lang.Register: ...

    @property
    def contextRegisters(self) -> List[object]: ...

    @property
    def registerNames(self) -> List[object]: ...

    @property
    def registers(self) -> List[object]: ...

    @property
    def sortedVectorRegisters(self) -> List[object]: ...
