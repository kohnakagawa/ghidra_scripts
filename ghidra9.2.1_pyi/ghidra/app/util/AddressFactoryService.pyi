import ghidra.program.model.address
import java.lang


class AddressFactoryService(object):
    """
    Simple interface for getting an address factory. This is used to delay the opening of
     a program until it is needed.
    """









    def equals(self, __a0: object) -> bool: ...

    def getAddressFactory(self) -> ghidra.program.model.address.AddressFactory: ...

    def getClass(self) -> java.lang.Class: ...

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
    def addressFactory(self) -> ghidra.program.model.address.AddressFactory: ...
