import db
import ghidra.program.database.map
import ghidra.program.database.util
import ghidra.program.model.address
import ghidra.util.task
import java.lang


class DatabaseTableUtils(object):
    """
    Collection of static functions for upgrading various database tables.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def updateAddressKey(table: db.Table, addrMap: ghidra.program.database.map.AddressMap, fromAddr: ghidra.program.model.address.Address, toAddr: ghidra.program.model.address.Address, length: long, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Handles redoing a table whose key is address based when a ranges of addresses is moved.
        @param table the database table.
        @param addrMap the address map.
        @param fromAddr the from address of the block being moved.
        @param toAddr the destination address of the block being moved.
        @param length the size of the block being moved.
        @param monitor the taskmonitor
        @throws IOException thrown if a database io error occurs.
        @throws CancelledException thrown if the user cancels the move operation.
        """
        ...

    @overload
    @staticmethod
    def updateAddressKey(table: db.Table, addrMap: ghidra.program.database.map.AddressMap, fromAddr: ghidra.program.model.address.Address, endAddr: ghidra.program.model.address.Address, toAddr: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Handles redoing a table whose key is address based when a ranges of addresses is moved.
        @param table the database table.
        @param addrMap the address map.
        @param fromAddr the first address of the block being moved.
        @param endAddr the last address of the block being moved.
        @param toAddr the destination address of the block being moved.
        @param monitor the task monitor
        @throws IOException thrown if a database io error occurs.
        @throws CancelledException thrown if the user cancels the move operation.
        """
        ...

    @staticmethod
    def updateIndexedAddressField(table: db.Table, addrCol: int, addrMap: ghidra.program.database.map.AddressMap, fromAddr: ghidra.program.model.address.Address, toAddr: ghidra.program.model.address.Address, length: long, filter: ghidra.program.database.util.RecordFilter, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Updates an indexed address field for when a block is moved.
        @param table the database table
        @param addrCol the address column in the table
        @param addrMap the address map
        @param fromAddr the from address of the block being moved
        @param toAddr the address to where the block is being moved.
        @param length the size of the block being moved.
        @param monitor the task monitor
        @throws IOException thrown if a database io error occurs.
        @throws CancelledException thrown if the user cancels the move operation.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
