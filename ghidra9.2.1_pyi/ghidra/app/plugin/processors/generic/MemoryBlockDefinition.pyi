import ghidra.program.model.listing
import java.lang


class MemoryBlockDefinition(object):
    """
    TODO To change the template for this generated type comment go to
     Window - Preferences - Java - Code Style - Code Templates
    """





    @overload
    def __init__(self, element: ghidra.xml.XmlElement): ...

    @overload
    def __init__(self, blockName: unicode, addressString: unicode, bitMappedAddress: unicode, mode: unicode, lengthString: unicode, initializedString: unicode): ...



    def createBlock(self, program: ghidra.program.model.listing.Program) -> None: ...

    def equals(self, __a0: object) -> bool: ...

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
