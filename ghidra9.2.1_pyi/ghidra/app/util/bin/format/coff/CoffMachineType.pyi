import java.lang


class CoffMachineType(object):
    """
    The Machine field has one of the following values that specifies its CPU type.
     An image file can be run only on the specified machine or on a system that emulates
     the specified machine.
    """

    IMAGE_FILE_MACHINE_ALPHA: int = 388
    IMAGE_FILE_MACHINE_ALPHA64: int = 644
    IMAGE_FILE_MACHINE_AM29KBIGMAGIC: int = 378
    IMAGE_FILE_MACHINE_AM29KLITTLEMAGIC: int = 379
    IMAGE_FILE_MACHINE_AM33: int = 467
    IMAGE_FILE_MACHINE_AMD64: int = -31132
    IMAGE_FILE_MACHINE_ARM: int = 448
    IMAGE_FILE_MACHINE_ARM64: int = -21916
    IMAGE_FILE_MACHINE_ARMNT: int = 452
    IMAGE_FILE_MACHINE_EBC: int = 3772
    IMAGE_FILE_MACHINE_I386: int = 332
    IMAGE_FILE_MACHINE_I386_AIX: int = 373
    IMAGE_FILE_MACHINE_I386_PTX: int = 340
    IMAGE_FILE_MACHINE_I960ROMAGIC: int = 352
    IMAGE_FILE_MACHINE_I960RWMAGIC: int = 353
    IMAGE_FILE_MACHINE_IA64: int = 512
    IMAGE_FILE_MACHINE_M32R: int = -28607
    IMAGE_FILE_MACHINE_M68KMAGIC: int = 616
    IMAGE_FILE_MACHINE_MIPS16: int = 614
    IMAGE_FILE_MACHINE_MIPSFPU: int = 870
    IMAGE_FILE_MACHINE_MIPSFPU16: int = 1126
    IMAGE_FILE_MACHINE_PIC30: int = 4662
    IMAGE_FILE_MACHINE_POWERPC: int = 496
    IMAGE_FILE_MACHINE_POWERPCFP: int = 497
    IMAGE_FILE_MACHINE_R10000: int = 360
    IMAGE_FILE_MACHINE_R3000: int = 354
    IMAGE_FILE_MACHINE_R4000: int = 358
    IMAGE_FILE_MACHINE_RISCV128: int = 20776
    IMAGE_FILE_MACHINE_RISCV32: int = 20530
    IMAGE_FILE_MACHINE_RISCV64: int = 20580
    IMAGE_FILE_MACHINE_SH3: int = 418
    IMAGE_FILE_MACHINE_SH3DSP: int = 419
    IMAGE_FILE_MACHINE_SH4: int = 422
    IMAGE_FILE_MACHINE_SH5: int = 424
    IMAGE_FILE_MACHINE_THUMB: int = 450
    IMAGE_FILE_MACHINE_TI_MSP430: int = 160
    IMAGE_FILE_MACHINE_TI_TMS320C2800: int = 157
    IMAGE_FILE_MACHINE_TI_TMS320C5400: int = 152
    IMAGE_FILE_MACHINE_TI_TMS320C5500: int = 156
    IMAGE_FILE_MACHINE_TI_TMS320C5500_PLUS: int = 161
    IMAGE_FILE_MACHINE_TI_TMS320C6000: int = 153
    IMAGE_FILE_MACHINE_TI_TMS470: int = 151
    IMAGE_FILE_MACHINE_UNKNOWN: int = 0
    IMAGE_FILE_MACHINE_WCEMIPSV2: int = 361
    TICOFF1MAGIC: int = 193
    TICOFF2MAGIC: int = 194



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isMachineTypeDefined(type: int) -> bool:
        """
        Checks to see if the given machine type is defined in this file.
        @param type The machine type to check.
        @return True if the given machine type is defined in this file; otherwise, false.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
