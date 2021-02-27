import ghidra.program.model.address
import java.io
import java.lang


class AddressLabelPair(object, java.io.Serializable):
    """
    Container for holding an address and label.
    """





    def __init__(self, addr: ghidra.program.model.address.Address, label: unicode):
        """
        Creates a new <CODE>AddressLabelPair</CODE>.
        @param addr the address
        @param label the label
        """
        ...



    def equals(self, obj: object) -> bool:
        """
        @see java.lang.Object#equals(java.lang.Object)
        """
        ...

    def getAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the address.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getLabel(self) -> unicode:
        """
        Returns the label.
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
    def label(self) -> unicode: ...
