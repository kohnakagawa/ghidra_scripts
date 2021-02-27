from typing import List
import java.lang


class MachHeaderFlags(object):
    """
    Constants for the flags field of the mach_header
    """

    MH_ALLMODSBOUND: int = 4096
    MH_ALLOW_STACK_EXECUTION: int = 131072
    MH_APP_EXTENSION_SAFE: int = 33554432
    MH_BINDATLOAD: int = 8
    MH_BINDS_TO_WEAK: int = 65536
    MH_CANONICAL: int = 16384
    MH_DEAD_STRIPPABLE_DYLIB: int = 4194304
    MH_DYLDLINK: int = 4
    MH_FORCE_FLAT: int = 256
    MH_HAS_TLV_DESCRIPTORS: int = 8388608
    MH_INCRLINK: int = 2
    MH_LAZY_INIT: int = 64
    MH_NOFIXPREBINDING: int = 1024
    MH_NOMULTIDEFS: int = 512
    MH_NOUNDEFS: int = 1
    MH_NO_HEAP_EXECUTION: int = 16777216
    MH_NO_REEXPORTED_DYLIBS: int = 1048576
    MH_PIE: int = 2097152
    MH_PREBINDABLE: int = 2048
    MH_PREBOUND: int = 16
    MH_ROOT_SAFE: int = 262144
    MH_SETUID_SAFE: int = 524288
    MH_SPLIT_SEGS: int = 32
    MH_SUBSECTIONS_VIA_SYMBOLS: int = 8192
    MH_TWOLEVEL: int = 128
    MH_WEAK_DEFINES: int = 32768



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getFlags(flags: int) -> List[unicode]:
        """
        Returns string representation of the flag values.
        """
        ...

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
