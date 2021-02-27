import ghidra.program.model.address
import java.lang


class XmlProgramUtilities(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def parseAddress(factory: ghidra.program.model.address.AddressFactory, addrString: unicode) -> ghidra.program.model.address.Address:
        """
        Parses the address string.
        @param factory the address factory
        @param addrString the address string to parse
        @return the parsed address, or null
        """
        ...

    @overload
    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def toString(addr: ghidra.program.model.address.Address) -> unicode:
        """
        Creates a string representation of the specifed address.
        @param addr the address to convert to a string
        @return the string representation of the address
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
