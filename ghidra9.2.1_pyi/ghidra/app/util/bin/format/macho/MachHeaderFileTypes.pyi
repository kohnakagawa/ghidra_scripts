import java.lang


class MachHeaderFileTypes(object):
    MH_BUNDLE: int = 8
    MH_CORE: int = 4
    MH_DSYM: int = 10
    MH_DYLIB: int = 6
    MH_DYLIB_STUB: int = 9
    MH_DYLINKER: int = 7
    MH_EXECUTE: int = 2
    MH_FVMLIB: int = 3
    MH_KEXT_BUNDLE: int = 11
    MH_OBJECT: int = 1
    MH_PRELOAD: int = 5



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getFileTypeDescription(fileType: int) -> unicode: ...

    @staticmethod
    def getFileTypeName(fileType: int) -> unicode: ...

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
