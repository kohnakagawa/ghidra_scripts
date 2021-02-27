from typing import List
import ghidra.file.formats.android.dex.format
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.program.model.symbol
import java.lang


class DexUtil(object):
    CATEGORY_PATH: unicode = u'classes/'
    CLASSDEF_NAME: unicode = u'__classdef__'
    HANDLE_PATH: unicode = u'/handles/'
    LOOKUP_ADDRESS: long = -0x20000000L
    MAX_METHOD_LENGTH: long = 0x40000L
    METHOD_ADDRESS: long = 0x50000000L



    def __init__(self): ...



    @staticmethod
    def convertClassStringToPathArray(__a0: unicode, __a1: unicode) -> List[unicode]: ...

    @staticmethod
    def convertPrototypeIndexToString(__a0: ghidra.file.formats.android.dex.format.DexHeader, __a1: int) -> unicode: ...

    @staticmethod
    def convertToString(__a0: ghidra.file.formats.android.dex.format.DexHeader, __a1: int) -> unicode: ...

    @overload
    @staticmethod
    def convertTypeIndexToString(__a0: ghidra.file.formats.android.dex.format.DexHeader, __a1: int) -> unicode: ...

    @overload
    @staticmethod
    def convertTypeIndexToString(__a0: ghidra.file.formats.android.dex.format.DexHeader, __a1: int) -> unicode: ...

    @overload
    @staticmethod
    def createNameSpaceFromMangledClassName(__a0: ghidra.program.model.listing.Program, __a1: unicode) -> ghidra.program.model.symbol.Namespace: ...

    @overload
    @staticmethod
    def createNameSpaceFromMangledClassName(__a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.symbol.Namespace, __a2: unicode) -> ghidra.program.model.symbol.Namespace: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getOrCreateNameSpace(__a0: ghidra.program.model.listing.Program, __a1: unicode) -> ghidra.program.model.symbol.Namespace: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def toDataType(__a0: ghidra.program.model.data.DataTypeManager, __a1: unicode) -> ghidra.program.model.data.DataType: ...

    @staticmethod
    def toLookupAddress(__a0: ghidra.program.model.listing.Program, __a1: int) -> ghidra.program.model.address.Address: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
