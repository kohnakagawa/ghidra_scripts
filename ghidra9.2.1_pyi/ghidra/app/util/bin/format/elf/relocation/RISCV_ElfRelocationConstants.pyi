import java.lang


class RISCV_ElfRelocationConstants(object):
    R_RISCV_32: int = 1
    R_RISCV_32_PCREL: int = 57
    R_RISCV_64: int = 2
    R_RISCV_ADD16: int = 34
    R_RISCV_ADD32: int = 35
    R_RISCV_ADD64: int = 36
    R_RISCV_ADD8: int = 33
    R_RISCV_ALIGN: int = 43
    R_RISCV_BRANCH: int = 16
    R_RISCV_CALL: int = 18
    R_RISCV_CALL_PLT: int = 19
    R_RISCV_COPY: int = 4
    R_RISCV_GNU_VTENTRY: int = 42
    R_RISCV_GNU_VTINHERIT: int = 41
    R_RISCV_GOT_HI20: int = 20
    R_RISCV_GPREL_I: int = 47
    R_RISCV_GPREL_S: int = 48
    R_RISCV_HI20: int = 26
    R_RISCV_JAL: int = 17
    R_RISCV_JUMP_SLOT: int = 5
    R_RISCV_LO12_I: int = 27
    R_RISCV_LO12_S: int = 28
    R_RISCV_NONE: int = 0
    R_RISCV_PCREL_HI20: int = 23
    R_RISCV_PCREL_LO12_I: int = 24
    R_RISCV_PCREL_LO12_S: int = 25
    R_RISCV_RELATIVE: int = 3
    R_RISCV_RELAX: int = 51
    R_RISCV_RVC_BRANCH: int = 44
    R_RISCV_RVC_JUMP: int = 45
    R_RISCV_RVC_LUI: int = 46
    R_RISCV_SET16: int = 55
    R_RISCV_SET32: int = 56
    R_RISCV_SET6: int = 53
    R_RISCV_SET8: int = 54
    R_RISCV_SUB16: int = 38
    R_RISCV_SUB32: int = 39
    R_RISCV_SUB6: int = 52
    R_RISCV_SUB64: int = 40
    R_RISCV_SUB8: int = 37
    R_RISCV_TLS_DTPMOD32: int = 6
    R_RISCV_TLS_DTPMOD64: int = 7
    R_RISCV_TLS_DTPREL32: int = 8
    R_RISCV_TLS_DTPREL64: int = 9
    R_RISCV_TLS_GD_HI20: int = 22
    R_RISCV_TLS_GOT_HI20: int = 21
    R_RISCV_TLS_TPREL32: int = 10
    R_RISCV_TLS_TPREL64: int = 11
    R_RISCV_TPREL_ADD: int = 32
    R_RISCV_TPREL_HI20: int = 29
    R_RISCV_TPREL_I: int = 49
    R_RISCV_TPREL_LO12_I: int = 30
    R_RISCV_TPREL_LO12_S: int = 31
    R_RISCV_TPREL_S: int = 50



    def __init__(self): ...



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
