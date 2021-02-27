import java.lang


class ProcessorInfo(object):
    """
    Miscellanious address space defines for language providers.
     Provides recommended default address space names and IDs.
    """

    BIT_SPACE: unicode = u'BITS'
    CODE_SPACE: unicode = u'CODE'
    CODE_SPACE_ID: int = 0
    DEFAULT_SPACE: unicode = u'MEM'
    EXTMEM_SPACE: unicode = u'EXTMEM'
    EXTMEM_SPACE_ID: int = 8
    INTMEM_SPACE: unicode = u'INTMEM'
    INTMEM_SPACE_ID: int = 3
    SFR_SPACE: unicode = u'SFR'
    SFR_SPACE_ID: int = 4







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
