import db.util
import ghidra.program.database
import ghidra.program.database.map
import ghidra.program.database.util
import ghidra.program.model.address
import ghidra.program.model.util
import ghidra.util
import ghidra.util.task
import java.lang


class AddressSetPropertyMapDB(object, ghidra.program.model.util.AddressSetPropertyMap):
    """
    AddressSetPropertyMap that uses a RangeMapDB to maintain a set of addresses.
    """









    @overload
    def add(self, addressSet: ghidra.program.model.address.AddressSetView) -> None: ...

    @overload
    def add(self, startAddr: ghidra.program.model.address.Address, endAddr: ghidra.program.model.address.Address) -> None: ...

    def clear(self) -> None: ...

    def contains(self, addr: ghidra.program.model.address.Address) -> bool: ...

    @staticmethod
    def createPropertyMap(program: ghidra.program.database.ProgramDB, mapName: unicode, errHandler: db.util.ErrorHandler, addrMap: ghidra.program.database.map.AddressMap, lock: ghidra.util.Lock) -> ghidra.program.database.util.AddressSetPropertyMapDB: ...

    def delete(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getAddressRanges(self) -> ghidra.program.model.address.AddressRangeIterator: ...

    def getAddressSet(self) -> ghidra.program.model.address.AddressSet: ...

    def getAddresses(self) -> ghidra.program.model.address.AddressIterator: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getPropertyMap(program: ghidra.program.database.ProgramDB, mapName: unicode, errHandler: db.util.ErrorHandler, addrMap: ghidra.program.database.map.AddressMap, lock: ghidra.util.Lock) -> ghidra.program.database.util.AddressSetPropertyMapDB: ...

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
    def remove(self, addressSet: ghidra.program.model.address.AddressSetView) -> None: ...

    @overload
    def remove(self, startAddr: ghidra.program.model.address.Address, endAddr: ghidra.program.model.address.Address) -> None: ...

    def set(self, addressSet: ghidra.program.model.address.AddressSetView) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def addressRanges(self) -> ghidra.program.model.address.AddressRangeIterator: ...

    @property
    def addressSet(self) -> ghidra.program.model.address.AddressSet: ...

    @property
    def addresses(self) -> ghidra.program.model.address.AddressIterator: ...
