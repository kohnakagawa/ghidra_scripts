import java.lang


class X86_32_ElfRelocationConstants(object):
    R_386_32: int = 1
    R_386_32PLT: int = 11
    R_386_COPY: int = 5
    R_386_GLOB_DAT: int = 6
    R_386_GOT32: int = 3
    R_386_GOTOFF: int = 9
    R_386_GOTPC: int = 10
    R_386_IRELATIVE: int = 42
    R_386_JMP_SLOT: int = 7
    R_386_NONE: int = 0
    R_386_PC32: int = 2
    R_386_PLT32: int = 4
    R_386_RELATIVE: int = 8
    R_386_TLS_DESC: int = 41
    R_386_TLS_DESC_CALL: int = 40
    R_386_TLS_DTPMOD32: int = 35
    R_386_TLS_DTPOFF32: int = 36
    R_386_TLS_GD: int = 18
    R_386_TLS_GD_32: int = 24
    R_386_TLS_GD_CALL: int = 26
    R_386_TLS_GD_POP: int = 27
    R_386_TLS_GD_PUSH: int = 25
    R_386_TLS_GOTDESC: int = 39
    R_386_TLS_GOTIE: int = 16
    R_386_TLS_IE: int = 15
    R_386_TLS_IE_32: int = 33
    R_386_TLS_LDM: int = 19
    R_386_TLS_LDM_32: int = 28
    R_386_TLS_LDM_CALL: int = 30
    R_386_TLS_LDM_POP: int = 31
    R_386_TLS_LDM_PUSH: int = 29
    R_386_TLS_LDO_32: int = 32
    R_386_TLS_LE: int = 17
    R_386_TLS_LE_32: int = 34
    R_386_TLS_TPOFF: int = 14
    R_386_TLS_TPOFF32: int = 37







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
