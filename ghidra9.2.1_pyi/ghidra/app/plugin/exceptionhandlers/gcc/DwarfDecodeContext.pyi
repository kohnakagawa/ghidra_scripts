import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.model.mem
import java.lang


class DwarfDecodeContext(object):




    @overload
    def __init__(self, __a0: ghidra.program.model.mem.MemBuffer, __a1: int): ...

    @overload
    def __init__(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.Address): ...

    @overload
    def __init__(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.Address, __a2: ghidra.program.model.address.Address): ...

    @overload
    def __init__(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.Address, __a2: ghidra.program.model.listing.Function): ...

    @overload
    def __init__(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.Address, __a2: ghidra.program.model.mem.MemoryBlock): ...

    @overload
    def __init__(self, __a0: ghidra.program.model.mem.MemBuffer, __a1: int, __a2: ghidra.program.model.mem.MemoryBlock, __a3: ghidra.program.model.address.Address): ...

    @overload
    def __init__(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.Address, __a2: ghidra.program.model.mem.MemoryBlock, __a3: ghidra.program.model.address.Address): ...



    def equals(self, __a0: object) -> bool: ...

    def getAddress(self) -> ghidra.program.model.address.Address: ...

    def getClass(self) -> java.lang.Class: ...

    def getDecodedValue(self) -> object: ...

    def getEhBlock(self) -> ghidra.program.model.mem.MemoryBlock: ...

    def getEncodedLength(self) -> int: ...

    def getFunctionEntryPoint(self) -> ghidra.program.model.address.Address: ...

    def getProgram(self) -> ghidra.program.model.listing.Program: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setDecodedValue(self, __a0: object, __a1: int) -> None: ...

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
    def decodedValue(self) -> object: ...

    @property
    def ehBlock(self) -> ghidra.program.model.mem.MemoryBlock: ...

    @property
    def encodedLength(self) -> int: ...

    @property
    def functionEntryPoint(self) -> ghidra.program.model.address.Address: ...

    @property
    def program(self) -> ghidra.program.model.listing.Program: ...
