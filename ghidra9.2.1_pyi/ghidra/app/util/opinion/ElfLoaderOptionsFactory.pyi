from typing import List
import java.lang


class ElfLoaderOptionsFactory(object):
    IMAGE64_BASE_DEFAULT: long = 0x100000L
    IMAGE_BASE_DEFAULT: long = 0x10000L
    IMAGE_BASE_OPTION_NAME: unicode = u'Image Base'
    IMAGE_DATA_IMAGE_BASE_OPTION_NAME: unicode = u'Data Image Base'
    INCLUDE_OTHER_BLOCKS: unicode = u'Import Non-Loaded Data'
    PERFORM_RELOCATIONS_NAME: unicode = u'Perform Symbol Relocations'
    RESOLVE_EXTERNAL_SYMBOLS_DEFAULT: bool = True
    RESOLVE_EXTERNAL_SYMBOLS_OPTION_NAME: unicode = u'Fixup Unresolved External Symbols'







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getDataImageBaseOption(__a0: List[object]) -> unicode: ...

    @staticmethod
    def getImageBaseOption(__a0: List[object]) -> unicode: ...

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
