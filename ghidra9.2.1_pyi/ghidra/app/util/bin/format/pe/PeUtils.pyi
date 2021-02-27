import ghidra.app.util.bin.format.pe
import ghidra.app.util.importer
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.listing
import java.lang


class PeUtils(object):




    def __init__(self): ...



    @overload
    @staticmethod
    def createData(program: ghidra.program.model.listing.Program, addr: ghidra.program.model.address.Address, datatype: ghidra.program.model.data.DataType, log: ghidra.app.util.importer.MessageLog) -> ghidra.program.model.listing.Data: ...

    @overload
    @staticmethod
    def createData(program: ghidra.program.model.listing.Program, addr: ghidra.program.model.address.Address, datatype: ghidra.program.model.data.DataType, datatypeLength: int, log: ghidra.app.util.importer.MessageLog) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getMarkupAddress(program: ghidra.program.model.listing.Program, isBinary: bool, ntHeader: ghidra.app.util.bin.format.pe.NTHeader, offset: int) -> ghidra.program.model.address.Address: ...

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
