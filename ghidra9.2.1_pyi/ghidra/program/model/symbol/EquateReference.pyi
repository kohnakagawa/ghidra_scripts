import ghidra.program.model.address
import java.lang


class EquateReference(object):
    """
    Interface to define an equate reference. Equate references consist of an
     address and an operand index.
    """









    def equals(self, __a0: object) -> bool: ...

    def getAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the address associated with this reference.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDynamicHashValue(self) -> long:
        """
        Returns the dynamic Hash value associated with the referenced constant varnode.
         A value of zero (0) indicates not applicable.
        @see ghidra.program.model.pcode.DynamicHash
        """
        ...

    def getOpIndex(self) -> int:
        """
        Returns the opcode index for the instruction located at this
         references address, or -1 if .
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
    def dynamicHashValue(self) -> long: ...

    @property
    def opIndex(self) -> int: ...
