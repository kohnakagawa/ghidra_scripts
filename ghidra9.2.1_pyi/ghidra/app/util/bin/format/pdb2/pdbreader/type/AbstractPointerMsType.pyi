from typing import List
import ghidra.app.util.bin.format.pdb2.pdbreader
import ghidra.app.util.bin.format.pdb2.pdbreader.type
import java.lang


class AbstractPointerMsType(ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractMsType):





    class PointerType(java.lang.Enum):
        ADDRESS_BASED: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.PointerType = base(addr)
        FAR: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.PointerType = far
        FAR32: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.PointerType = far32
        HUGE: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.PointerType = huge
        INVALID: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.PointerType = invalid
        NEAR: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.PointerType = near
        NEAR32: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.PointerType =
        PTR64: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.PointerType = far64
        SEGMENT_ADDRESS_BASED: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.PointerType = base(segaddr)
        SEGMENT_BASED: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.PointerType = base(seg)
        SEGMENT_VALUE_BASED: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.PointerType = base(segval)
        SELF_BASED: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.PointerType = base(addr)
        TYPE_BASED: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.PointerType = base(type)
        UNSPECIFIED: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.PointerType = unspecified
        VALUE_BASED: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.PointerType = base(val)
        label: unicode
        value: int







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        @staticmethod
        def fromValue(__a0: int) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.PointerType: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.PointerType: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.PointerType]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...






    class PointerMode(java.lang.Enum):
        INVALID: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.PointerMode =
        LVALUE_REFERENCE: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.PointerMode = &
        MEMBER_DATA_POINTER: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.PointerMode = ::*
        MEMBER_FUNCTION_POINTER: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.PointerMode = ::*
        POINTER: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.PointerMode = *
        RESERVED: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.PointerMode =
        RVALUE_REFERENCE: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.PointerMode = &&
        label: unicode
        value: int







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def emit(self, __a0: java.lang.StringBuilder) -> None: ...

        def equals(self, __a0: object) -> bool: ...

        @staticmethod
        def fromValue(__a0: int) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.PointerMode: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.PointerMode: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.PointerMode]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...






    class MemberPointerType(java.lang.Enum):
        DATA_GENERAL: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.MemberPointerType = pdm32_vbase
        DATA_MULTIPLE_INHERITANCE: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.MemberPointerType = pdm16_vbase
        DATA_SINGLE_INHERITANCE: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.MemberPointerType = pdm16_vfcn
        DATA_VIRTUAL_INHERITANCE: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.MemberPointerType = pdm32_nvvfcn
        FUNCTION_MULTIPLE_INHERITANCE: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.MemberPointerType = pmf16_nearnvma
        FUNCTION_MULTIPLE_INHERITANCE_1632: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.MemberPointerType = pmf16_farnvma
        FUNCTION_MULTIPLE_INHERITANCE_32: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.MemberPointerType = pmf32_nvma
        FUNCTION_SINGLE_INHERITANCE: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.MemberPointerType = pmf16_nearnvsa
        FUNCTION_SINGLE_INHERITANCE_1632: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.MemberPointerType = pmf16_farnvsa
        FUNCTION_SINGLE_INHERITANCE_32: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.MemberPointerType = pmf32_nvsa
        FUNCTION_VIRTUAL_INHERITANCE: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.MemberPointerType = pmf16_nearvbase
        FUNCTION_VIRTUAL_INHERITANCE_1632: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.MemberPointerType = pmf16_farnvbase
        FUNCTION_VIRTUAL_INHERITANCE_32: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.MemberPointerType = pmf32_nvbase
        INVALID: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.MemberPointerType = invalid
        UNSPECIFIED: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.MemberPointerType = pdm16_nonvirt
        label: unicode
        value: int







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        @staticmethod
        def fromValue(__a0: int) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.MemberPointerType: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.MemberPointerType: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.MemberPointerType]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...



    def __init__(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb, __a1: ghidra.app.util.bin.format.pdb2.pdbreader.PdbByteReader): ...



    @overload
    def emit(self, __a0: java.lang.StringBuilder) -> None: ...

    @overload
    def emit(self, __a0: java.lang.StringBuilder, __a1: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractMsType.Bind) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getLength(self) -> long: ...

    def getMemberPointerType(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.MemberPointerType: ...

    def getName(self) -> unicode: ...

    def getPdbId(self) -> int: ...

    def getPointerMode(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.PointerMode: ...

    def getPointerType(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.PointerType: ...

    def getRecordNumber(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.RecordNumber: ...

    def getSize(self) -> long: ...

    def getUnderlyingRecordNumber(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.RecordNumber: ...

    def getUnderlyingType(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractMsType: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def parseExtendedPointerInfo(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.PdbByteReader, __a1: int, __a2: ghidra.app.util.bin.format.pdb2.pdbreader.StringParseType) -> None: ...

    def setRecordNumber(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.RecordNumber) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def memberPointerType(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.MemberPointerType: ...

    @property
    def pointerMode(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.PointerMode: ...

    @property
    def pointerType(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.PointerType: ...

    @property
    def size(self) -> long: ...

    @property
    def underlyingRecordNumber(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.RecordNumber: ...

    @property
    def underlyingType(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractMsType: ...
