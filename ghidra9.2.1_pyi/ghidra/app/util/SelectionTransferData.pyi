import ghidra.program.model.address
import java.lang


class SelectionTransferData(object):
    """
    Data that is the transferable in SelectionTransferable; it contains an address set and the
     path of the program.
    """





    def __init__(self, set: ghidra.program.model.address.AddressSetView, programPath: unicode):
        """
        Constructor
        @param set address set to transfer
        @param programPath path to the program that contains the set
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getAddressSet(self) -> ghidra.program.model.address.AddressSetView:
        """
        Return the address set.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getProgramPath(self) -> unicode:
        """
        Return the program path.
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
    def addressSet(self) -> ghidra.program.model.address.AddressSetView: ...

    @property
    def programPath(self) -> unicode: ...
