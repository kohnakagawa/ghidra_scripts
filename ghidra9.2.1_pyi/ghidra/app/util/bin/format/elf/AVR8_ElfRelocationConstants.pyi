import java.lang


class AVR8_ElfRelocationConstants(object):
    R_AVR_13_PCREL: int = 3
    R_AVR_16: int = 4
    R_AVR_16_PM: int = 5
    R_AVR_32: int = 1
    R_AVR_6: int = 20
    R_AVR_6_ADIW: int = 21
    R_AVR_7_PCREL: int = 2
    R_AVR_8: int = 26
    R_AVR_8_HI8: int = 28
    R_AVR_8_HLO8: int = 29
    R_AVR_8_LO8: int = 27
    R_AVR_CALL: int = 18
    R_AVR_DIFF16: int = 31
    R_AVR_DIFF32: int = 32
    R_AVR_DIFF8: int = 30
    R_AVR_HH8_LDI: int = 8
    R_AVR_HH8_LDI_NEG: int = 11
    R_AVR_HH8_LDI_PM: int = 14
    R_AVR_HH8_LDI_PM_NEG: int = 17
    R_AVR_HI8_LDI: int = 7
    R_AVR_HI8_LDI_GS: int = 25
    R_AVR_HI8_LDI_NEG: int = 10
    R_AVR_HI8_LDI_PM: int = 13
    R_AVR_HI8_LDI_PM_NEG: int = 16
    R_AVR_LDI: int = 19
    R_AVR_LDS_STS_16: int = 33
    R_AVR_LO8_LDI: int = 6
    R_AVR_LO8_LDI_GS: int = 24
    R_AVR_LO8_LDI_NEG: int = 9
    R_AVR_LO8_LDI_PM: int = 12
    R_AVR_LO8_LDI_PM_NEG: int = 15
    R_AVR_MS8_LDI: int = 22
    R_AVR_MS8_LDI_NEG: int = 23
    R_AVR_NONE: int = 0
    R_AVR_PORT5: int = 35
    R_AVR_PORT6: int = 34



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
