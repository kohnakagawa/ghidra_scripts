import db.util
import ghidra.program.database
import ghidra.program.database.map
import ghidra.program.model.address
import ghidra.util
import ghidra.util.task
import java.lang


class IntRangeMapDB(object, ghidra.program.database.IntRangeMap):
    TABLE_PREFIX: unicode = u'Range Map - IntMap - '







    def clearAll(self) -> None: ...

    @overload
    def clearValue(self, addresses: ghidra.program.model.address.AddressSetView) -> None: ...

    @overload
    def clearValue(self, startAddr: ghidra.program.model.address.Address, endAddr: ghidra.program.model.address.Address) -> None: ...

    @staticmethod
    def createPropertyMap(program: ghidra.program.database.ProgramDB, mapName: unicode, errHandler: db.util.ErrorHandler, addrMap: ghidra.program.database.map.AddressMap, lock: ghidra.util.Lock) -> ghidra.program.database.IntRangeMapDB: ...

    def delete(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    @overload
    def getAddressSet(self) -> ghidra.program.model.address.AddressSet: ...

    @overload
    def getAddressSet(self, value: int) -> ghidra.program.model.address.AddressSet: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getPropertyMap(program: ghidra.program.database.ProgramDB, mapName: unicode, errHandler: db.util.ErrorHandler, addrMap: ghidra.program.database.map.AddressMap, lock: ghidra.util.Lock) -> ghidra.program.database.IntRangeMapDB: ...

    def getValue(self, address: ghidra.program.model.address.Address) -> int: ...

    def hashCode(self) -> int: ...

    def moveAddressRange(self, fromAddr: ghidra.program.model.address.Address, toAddr: ghidra.program.model.address.Address, length: long, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Move the address range to a new starting address.
        @param fromAddr move from address
        @param toAddr move to address
        @param length number of address to move
        @param monitor
        @throws CancelledException
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def setValue(self, addresses: ghidra.program.model.address.AddressSetView, value: int) -> None: ...

    @overload
    def setValue(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address, value: int) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def addressSet(self) -> ghidra.program.model.address.AddressSet: ...
