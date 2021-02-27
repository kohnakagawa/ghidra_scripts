from typing import Iterator
from typing import List
import db.util
import ghidra.program.database
import ghidra.program.model.address
import ghidra.program.model.symbol
import ghidra.util
import ghidra.util.task
import java.io
import java.lang


class EquateManager(object, ghidra.program.model.symbol.EquateTable, db.util.ErrorHandler, ghidra.program.database.ManagerDB):
    """
    Implementation of the Equate Table
    """

    DATATYPE_TAG: unicode = u'dtID'
    ERROR_TAG: unicode = u'<BAD EQUATE>'
    FORMAT_DELIMITER: unicode = u':'



    def __init__(self, handle: db.DBHandle, addrMap: ghidra.program.database.map.AddressMap, openMode: int, lock: ghidra.util.Lock, monitor: ghidra.util.task.TaskMonitor):
        """
        Constructor
        @param handle database handle
        @param addrMap map that converts addresses to longs and longs to addresses
        @param openMode one of ProgramDB.CREATE, UPDATE, UPGRADE, or READ_ONLY
        @param lock the program synchronization lock
        @param monitor the progress monitor used when upgrading.
        @throws VersionException if the database version doesn't match the current version.
        @throws IOException if a database error occurs.
        """
        ...



    def createEquate(self, name: unicode, value: long) -> ghidra.program.model.symbol.Equate: ...

    def dbError(self, e: java.io.IOException) -> None: ...

    def deleteAddressRange(self, startAddr: ghidra.program.model.address.Address, endAddr: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def formatNameForEquate(dtID: ghidra.util.UniversalID, equateValue: long) -> unicode:
        """
        Formats a string to the equate format given the enum UUID and the value for the equate. The
         formatted strings are used when setting equates from datatypes so that information can be
         stored with an equate to point back to that datatype.
        @param dtID The enum's data type UUID
        @param equateValue The value intended for the equate
        @return The formatted equate name
        """
        ...

    @staticmethod
    def formatNameForEquateError(equateValue: long) -> unicode:
        """
        Formats a string to the equate error format given the value. Used for rendering formatted
          equates that do not point back to a datatype.
        @param equateValue The value of the equate
        @return The error formatted equate name
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getDataTypeUUID(formattedEquateName: unicode) -> ghidra.util.UniversalID:
        """
        Pulls out the enum data type UUID given a formatted equate name. This UUID should point back
         to a datatype.
        @param formattedEquateName The formatted equate name to pull the UUID from
        @return The enum data type UUID or null if the given name is not formatted.
        """
        ...

    @overload
    def getEquate(self, name: unicode) -> ghidra.program.model.symbol.Equate: ...

    @overload
    def getEquate(self, reference: ghidra.program.model.address.Address, opIndex: int, scalarValue: long) -> ghidra.program.model.symbol.Equate: ...

    @overload
    def getEquateAddresses(self) -> ghidra.program.model.address.AddressIterator: ...

    @overload
    def getEquateAddresses(self, startAddr: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressIterator: ...

    @overload
    def getEquateAddresses(self, set: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.AddressIterator: ...

    @staticmethod
    def getEquateValueFromFormattedName(formattedEquateName: unicode) -> long:
        """
        Pulls out the value of the equate given the formatted equate name. The value stored in the
         equate info is a decimal.
        @param formattedEquateName The formatted equate name to pull the value from
        @return The value of the equate, or -1 if the given name is not formatted.
        """
        ...

    @overload
    def getEquates(self) -> Iterator[ghidra.program.model.symbol.Equate]: ...

    @overload
    def getEquates(self, value: long) -> List[ghidra.program.model.symbol.Equate]: ...

    @overload
    def getEquates(self, reference: ghidra.program.model.address.Address) -> List[ghidra.program.model.symbol.Equate]: ...

    @overload
    def getEquates(self, reference: ghidra.program.model.address.Address, opIndex: int) -> List[ghidra.program.model.symbol.Equate]: ...

    def hashCode(self) -> int: ...

    def invalidateCache(self, all: bool) -> None: ...

    def moveAddressRange(self, fromAddr: ghidra.program.model.address.Address, toAddr: ghidra.program.model.address.Address, length: long, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def programReady(self, openMode: int, currentRevision: int, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def removeEquate(self, name: unicode) -> bool: ...

    def setProgram(self, program: ghidra.program.database.ProgramDB) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def equateAddresses(self) -> ghidra.program.model.address.AddressIterator: ...

    @property
    def equates(self) -> java.util.Iterator: ...

    @property
    def program(self) -> None: ...  # No getter available.

    @program.setter
    def program(self, value: ghidra.program.database.ProgramDB) -> None: ...
