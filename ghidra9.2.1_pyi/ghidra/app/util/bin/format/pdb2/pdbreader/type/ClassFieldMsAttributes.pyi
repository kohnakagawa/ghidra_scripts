from typing import List
import ghidra.app.util.bin.format.pdb2.pdbreader
import ghidra.app.util.bin.format.pdb2.pdbreader.type
import java.lang


class ClassFieldMsAttributes(ghidra.app.util.bin.format.pdb2.pdbreader.AbstractParsableItem):





    class Access(java.lang.Enum):
        BLANK: ghidra.app.util.bin.format.pdb2.pdbreader.type.ClassFieldMsAttributes.Access =
        INVALID: ghidra.app.util.bin.format.pdb2.pdbreader.type.ClassFieldMsAttributes.Access =
        PRIVATE: ghidra.app.util.bin.format.pdb2.pdbreader.type.ClassFieldMsAttributes.Access = private
        PROTECTED: ghidra.app.util.bin.format.pdb2.pdbreader.type.ClassFieldMsAttributes.Access = protected
        PUBLIC: ghidra.app.util.bin.format.pdb2.pdbreader.type.ClassFieldMsAttributes.Access = public
        label: unicode
        value: int







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def emit(self, __a0: java.lang.StringBuilder) -> None: ...

        def equals(self, __a0: object) -> bool: ...

        @staticmethod
        def fromValue(__a0: int) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.ClassFieldMsAttributes.Access: ...

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
        def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.ClassFieldMsAttributes.Access: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.app.util.bin.format.pdb2.pdbreader.type.ClassFieldMsAttributes.Access]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...






    class Property(java.lang.Enum):
        BLANK: ghidra.app.util.bin.format.pdb2.pdbreader.type.ClassFieldMsAttributes.Property =
        FRIEND: ghidra.app.util.bin.format.pdb2.pdbreader.type.ClassFieldMsAttributes.Property = friend
        INTRO: ghidra.app.util.bin.format.pdb2.pdbreader.type.ClassFieldMsAttributes.Property = <intro>
        INTRO_PURE: ghidra.app.util.bin.format.pdb2.pdbreader.type.ClassFieldMsAttributes.Property = <intro,pure>
        INVALID: ghidra.app.util.bin.format.pdb2.pdbreader.type.ClassFieldMsAttributes.Property =
        PURE: ghidra.app.util.bin.format.pdb2.pdbreader.type.ClassFieldMsAttributes.Property = <pure>
        RESERVED: ghidra.app.util.bin.format.pdb2.pdbreader.type.ClassFieldMsAttributes.Property =
        STATIC: ghidra.app.util.bin.format.pdb2.pdbreader.type.ClassFieldMsAttributes.Property = static
        VIRTUAL: ghidra.app.util.bin.format.pdb2.pdbreader.type.ClassFieldMsAttributes.Property = virtual
        label: unicode
        value: int







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def emit(self, __a0: java.lang.StringBuilder) -> None: ...

        def equals(self, __a0: object) -> bool: ...

        @staticmethod
        def fromValue(__a0: int) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.ClassFieldMsAttributes.Property: ...

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
        def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.ClassFieldMsAttributes.Property: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.app.util.bin.format.pdb2.pdbreader.type.ClassFieldMsAttributes.Property]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...



    def __init__(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.PdbByteReader): ...



    def emit(self, __a0: java.lang.StringBuilder) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getAccess(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.ClassFieldMsAttributes.Access: ...

    def getClass(self) -> java.lang.Class: ...

    def getProperty(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.ClassFieldMsAttributes.Property: ...

    def hashCode(self) -> int: ...

    def isCannotBeOverridden(self) -> bool: ...

    def isCompilerGeneratedFunctionDoesExist(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def access(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.ClassFieldMsAttributes.Access: ...

    @property
    def cannotBeOverridden(self) -> bool: ...

    @property
    def compilerGeneratedFunctionDoesExist(self) -> bool: ...

    @property
    def property(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.ClassFieldMsAttributes.Property: ...
