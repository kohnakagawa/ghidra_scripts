import java.lang


class MachineConstants(object):
    """
    PE machine ID constants defined by standard header file 'ntimage.h'
    """

    IMAGE_FILE_MACHINE_ALPHA: int = 388
    IMAGE_FILE_MACHINE_ALPHA64: int = 644
    IMAGE_FILE_MACHINE_AM33: int = 467
    IMAGE_FILE_MACHINE_AMD64: int = -31132
    IMAGE_FILE_MACHINE_ARM: int = 448
    IMAGE_FILE_MACHINE_ARM64: int = -21916
    IMAGE_FILE_MACHINE_ARMNT: int = 452
    IMAGE_FILE_MACHINE_AXP64: int = 644
    IMAGE_FILE_MACHINE_CEE: int = -16146
    IMAGE_FILE_MACHINE_CEF: int = 3311
    IMAGE_FILE_MACHINE_EBC: int = 3772
    IMAGE_FILE_MACHINE_I386: int = 332
    IMAGE_FILE_MACHINE_IA64: int = 512
    IMAGE_FILE_MACHINE_M32R: int = -28607
    IMAGE_FILE_MACHINE_MIPS16: int = 614
    IMAGE_FILE_MACHINE_MIPSFPU: int = 870
    IMAGE_FILE_MACHINE_MIPSFPU16: int = 1126
    IMAGE_FILE_MACHINE_POWERPC: int = 496
    IMAGE_FILE_MACHINE_POWERPCFP: int = 497
    IMAGE_FILE_MACHINE_R10000: int = 360
    IMAGE_FILE_MACHINE_R3000: int = 354
    IMAGE_FILE_MACHINE_R4000: int = 358
    IMAGE_FILE_MACHINE_SH3: int = 418
    IMAGE_FILE_MACHINE_SH3DSP: int = 419
    IMAGE_FILE_MACHINE_SH3E: int = 420
    IMAGE_FILE_MACHINE_SH4: int = 422
    IMAGE_FILE_MACHINE_SH5: int = 424
    IMAGE_FILE_MACHINE_THUMB: int = 450
    IMAGE_FILE_MACHINE_TRICORE: int = 1312
    IMAGE_FILE_MACHINE_UNKNOWN: int = 0
    IMAGE_FILE_MACHINE_WCEMIPSV2: int = 361



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
