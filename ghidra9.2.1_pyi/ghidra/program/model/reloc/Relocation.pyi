from typing import List
import ghidra.program.model.address
import java.lang


class Relocation(object):
    """
    A class to store the information needed for a single
     program relocation.
    """





    def __init__(self, addr: ghidra.program.model.address.Address, type: int, values: List[long], bytes: List[int], symbolName: unicode):
        """
        Constructs a new relocation.
        @param addr the address where the relocation is required
        @param type the type of relocation to perform
        @param values the values needed when performing the relocation
        @param bytes original instruction bytes affected by relocation
        @param symbolName the name of the symbol being relocated
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the address where the relocation is required.
        @return the address where the relocation is required
        """
        ...

    def getBytes(self) -> List[int]:
        """
        Returns the original instruction bytes affected by relocation.
        @return original instruction bytes affected by relocation
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getSymbolName(self) -> unicode:
        """
        The name of the symbol being relocated or <code>null</code> if there is no symbol name.
        @return the name of the symbol being relocated or <code>null</code> if there is no symbol name.
        """
        ...

    def getType(self) -> int:
        """
        Returns the type of the relocation to perform.
        @return the type of the relocation to perform
        """
        ...

    def getValues(self) -> List[long]:
        """
        Returns the value needed when performing the relocation.
        @return the value needed when performing the relocation
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
    def address(self) -> ghidra.program.model.address.Address: ...

    @property
    def bytes(self) -> List[int]: ...

    @property
    def symbolName(self) -> unicode: ...

    @property
    def type(self) -> int: ...

    @property
    def values(self) -> List[long]: ...
