import java.lang


class MachConstants(object):
    DATA_TYPE_CATEGORY: unicode = u'/MachO'
    MH_CIGAM: int = -822415874
    MH_CIGAM_64: int = -805638658
    MH_MAGIC: int = -17958194
    MH_MAGIC_64: int = -17958193
    NAME_LENGTH: int = 16



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isMagic(magic: int) -> bool:
        """
        Convenience method for matching the magic number
        @param magic the magic number read from the file
        @return true if the magic number matches
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
