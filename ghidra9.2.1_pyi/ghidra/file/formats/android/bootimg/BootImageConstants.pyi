import java.lang


class BootImageConstants(object):
    BOOT_ARGS_SIZE: int = 512
    BOOT_IMAGE_MAGIC: unicode = u'ANDROID!'
    BOOT_IMAGE_MAGIC_BYTES: List[int] = array('b', [65, 78, 68, 82, 79, 73, 68, 33])
    BOOT_IMAGE_MAGIC_SIZE: int = 8
    BOOT_NAME_SIZE: int = 16
    KERNEL: unicode = u'kernel'
    RAMDISK: unicode = u'ramdisk'
    SECOND_STAGE: unicode = u'second stage'



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
