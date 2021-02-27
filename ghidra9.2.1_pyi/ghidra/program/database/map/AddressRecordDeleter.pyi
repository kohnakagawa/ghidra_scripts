import db
import ghidra.program.database.map
import ghidra.program.database.util
import ghidra.program.model.address
import java.lang


class AddressRecordDeleter(object):
    """
    Static methods to delete records from a table. Handles subtle issues with image base causing
     address to "wrap".
    """









    @overload
    @staticmethod
    def deleteRecords(table: db.Table, addrMap: ghidra.program.database.map.AddressMap, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> bool:
        """
        Deletes the records the fall within the given range. Uses the address map to convert the
         address range into 1 or more key ranges. (Address ranges may not be continuous after
         converting to long space).
         NOTE: Absolute key encodings are not handled currently !!
        @param table the database table to delete records from.
        @param addrMap the address map used to convert addresses into long keys.
        @param start the start address in the range.
        @param end the end address in the range.
        @throws IOException if a database io error occurs.
        """
        ...

    @overload
    @staticmethod
    def deleteRecords(table: db.Table, colIx: int, addrMap: ghidra.program.database.map.AddressMap, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address, filter: ghidra.program.database.util.RecordFilter) -> bool:
        """
        Deletes the records that have indexed address fields that fall within the given range.
         Uses the address map to convert the
         address range into 1 or more key ranges. (Address ranges may not be continuous after
         converting to long space).
         NOTE: Absolute key encodings are not handled currently !!
        @param table the database table to delete records from.
        @param colIx the column that has indexed addresses.
        @param addrMap the address map used to convert addresses into long keys.
        @param start the start address in the range.
        @param end the end address in the range.
        @throws IOException if a database io error occurs.
        """
        ...

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
