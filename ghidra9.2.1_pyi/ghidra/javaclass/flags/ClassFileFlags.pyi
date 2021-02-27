from typing import List
import ghidra.javaclass.flags
import java.lang


class ClassFileFlags(java.lang.Enum):
    ACC_ABSTRACT: ghidra.javaclass.flags.ClassFileFlags = ACC_ABSTRACT
    ACC_ANNOTATION: ghidra.javaclass.flags.ClassFileFlags = ACC_ANNOTATION
    ACC_ENUM: ghidra.javaclass.flags.ClassFileFlags = ACC_ENUM
    ACC_FINAL: ghidra.javaclass.flags.ClassFileFlags = ACC_FINAL
    ACC_INTERFACE: ghidra.javaclass.flags.ClassFileFlags = ACC_INTERFACE
    ACC_PUBLIC: ghidra.javaclass.flags.ClassFileFlags = ACC_PUBLIC
    ACC_SUPER: ghidra.javaclass.flags.ClassFileFlags = ACC_SUPER
    ACC_SYNTHETIC: ghidra.javaclass.flags.ClassFileFlags = ACC_SYNTHETIC







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDeclaringClass(self) -> java.lang.Class: ...

    def getValue(self) -> int: ...

    def hashCode(self) -> int: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ordinal(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.javaclass.flags.ClassFileFlags: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.javaclass.flags.ClassFileFlags]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def value(self) -> int: ...
