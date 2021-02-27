from typing import List
import ghidra.program.model.data
import java.lang


class GenericCallingConvention(java.lang.Enum):
    cdecl: ghidra.program.model.data.GenericCallingConvention = __cdecl
    fastcall: ghidra.program.model.data.GenericCallingConvention = __fastcall
    stdcall: ghidra.program.model.data.GenericCallingConvention = __stdcall
    thiscall: ghidra.program.model.data.GenericCallingConvention = __thiscall
    unknown: ghidra.program.model.data.GenericCallingConvention =
    vectorcall: ghidra.program.model.data.GenericCallingConvention = __vectorcall







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def get(__a0: int) -> ghidra.program.model.data.GenericCallingConvention: ...

    def getClass(self) -> java.lang.Class: ...

    def getDeclarationName(self) -> unicode: ...

    def getDeclaringClass(self) -> java.lang.Class: ...

    @staticmethod
    def getGenericCallingConvention(__a0: unicode) -> ghidra.program.model.data.GenericCallingConvention: ...

    @staticmethod
    def guessFromName(__a0: unicode) -> ghidra.program.model.data.GenericCallingConvention: ...

    def hashCode(self) -> int: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ordinal(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.program.model.data.GenericCallingConvention: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.program.model.data.GenericCallingConvention]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def declarationName(self) -> unicode: ...
