import ghidra.app.plugin.exceptionhandlers.gcc
import ghidra.program.model.address
import java.lang


class LSDAHeader(ghidra.app.plugin.exceptionhandlers.gcc.GccAnalysisClass):




    def __init__(self, __a0: ghidra.util.task.TaskMonitor, __a1: ghidra.program.model.listing.Program, __a2: ghidra.app.plugin.exceptionhandlers.gcc.RegionDescriptor): ...



    def create(self, __a0: ghidra.program.model.address.Address) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getBody(self) -> ghidra.program.model.address.AddressRange: ...

    def getCallSiteTableEncoding(self) -> int: ...

    def getCallSiteTableHeaderSize(self) -> int: ...

    def getCallSiteTableLength(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getHeaderSize(self) -> long: ...

    def getLPStartAddress(self) -> ghidra.program.model.address.Address: ...

    def getLPStartEncoding(self) -> int: ...

    def getNextAddress(self) -> ghidra.program.model.address.Address: ...

    def getTTypeBaseAddress(self) -> ghidra.program.model.address.Address: ...

    def getTTypeEncoding(self) -> int: ...

    def getTTypeOffset(self) -> int: ...

    def hasTypeTable(self) -> bool: ...

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
    def LPStartAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def LPStartEncoding(self) -> int: ...

    @property
    def TTypeBaseAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def TTypeEncoding(self) -> int: ...

    @property
    def TTypeOffset(self) -> int: ...

    @property
    def body(self) -> ghidra.program.model.address.AddressRange: ...

    @property
    def callSiteTableEncoding(self) -> int: ...

    @property
    def callSiteTableHeaderSize(self) -> int: ...

    @property
    def callSiteTableLength(self) -> int: ...

    @property
    def headerSize(self) -> long: ...

    @property
    def nextAddress(self) -> ghidra.program.model.address.Address: ...
