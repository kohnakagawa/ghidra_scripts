from typing import List
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.model.mem
import java.io
import java.lang


class MemoryBlockStub(object, ghidra.program.model.mem.MemoryBlock):
    """
    MemoryBlockStub can be extended for use by tests. It throws an UnsupportedOperationException
     for all methods in the MemoryBlock interface. Any method that is needed for your test can then
     be overridden so it can provide its own test implementation and return value.
    """

    EXECUTE: int = 1
    EXTERNAL_BLOCK_NAME: unicode = u'EXTERNAL'
    READ: int = 4
    VOLATILE: int = 8
    WRITE: int = 2



    @overload
    def __init__(self): ...

    @overload
    def __init__(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address): ...



    @overload
    def compareTo(self, o: ghidra.program.model.mem.MemoryBlock) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def contains(self, addr: ghidra.program.model.address.Address) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getByte(self, addr: ghidra.program.model.address.Address) -> int: ...

    @overload
    def getBytes(self, addr: ghidra.program.model.address.Address, b: List[int]) -> int: ...

    @overload
    def getBytes(self, addr: ghidra.program.model.address.Address, b: List[int], off: int, len: int) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getComment(self) -> unicode: ...

    def getData(self) -> java.io.InputStream: ...

    def getEnd(self) -> ghidra.program.model.address.Address: ...

    def getName(self) -> unicode: ...

    def getPermissions(self) -> int: ...

    def getSize(self) -> long: ...

    def getSourceInfos(self) -> List[ghidra.program.model.mem.MemoryBlockSourceInfo]: ...

    def getSourceName(self) -> unicode: ...

    def getStart(self) -> ghidra.program.model.address.Address: ...

    def getType(self) -> ghidra.program.model.mem.MemoryBlockType: ...

    def hashCode(self) -> int: ...

    def isExecute(self) -> bool: ...

    @staticmethod
    def isExternalBlockAddress(__a0: ghidra.program.model.address.Address, __a1: ghidra.program.model.listing.Program) -> bool: ...

    def isInitialized(self) -> bool: ...

    def isLoaded(self) -> bool: ...

    def isMapped(self) -> bool: ...

    def isOverlay(self) -> bool: ...

    def isRead(self) -> bool: ...

    def isVolatile(self) -> bool: ...

    def isWrite(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def putByte(self, addr: ghidra.program.model.address.Address, b: int) -> None: ...

    @overload
    def putBytes(self, addr: ghidra.program.model.address.Address, b: List[int]) -> int: ...

    @overload
    def putBytes(self, addr: ghidra.program.model.address.Address, b: List[int], off: int, len: int) -> int: ...

    def setComment(self, comment: unicode) -> None: ...

    def setExecute(self, e: bool) -> None: ...

    def setName(self, name: unicode) -> None: ...

    def setPermissions(self, read: bool, write: bool, execute: bool) -> None: ...

    def setRead(self, r: bool) -> None: ...

    def setSourceName(self, sourceName: unicode) -> None: ...

    def setVolatile(self, v: bool) -> None: ...

    def setWrite(self, w: bool) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def comment(self) -> unicode: ...

    @comment.setter
    def comment(self, value: unicode) -> None: ...

    @property
    def data(self) -> java.io.InputStream: ...

    @property
    def end(self) -> ghidra.program.model.address.Address: ...

    @property
    def execute(self) -> bool: ...

    @execute.setter
    def execute(self, value: bool) -> None: ...

    @property
    def initialized(self) -> bool: ...

    @property
    def loaded(self) -> bool: ...

    @property
    def mapped(self) -> bool: ...

    @property
    def name(self) -> unicode: ...

    @name.setter
    def name(self, value: unicode) -> None: ...

    @property
    def overlay(self) -> bool: ...

    @property
    def permissions(self) -> int: ...

    @property
    def read(self) -> bool: ...

    @read.setter
    def read(self, value: bool) -> None: ...

    @property
    def size(self) -> long: ...

    @property
    def sourceInfos(self) -> List[object]: ...

    @property
    def sourceName(self) -> unicode: ...

    @sourceName.setter
    def sourceName(self, value: unicode) -> None: ...

    @property
    def start(self) -> ghidra.program.model.address.Address: ...

    @property
    def type(self) -> ghidra.program.model.mem.MemoryBlockType: ...

    @property
    def volatile(self) -> bool: ...

    @volatile.setter
    def volatile(self, value: bool) -> None: ...

    @property
    def write(self) -> bool: ...

    @write.setter
    def write(self, value: bool) -> None: ...