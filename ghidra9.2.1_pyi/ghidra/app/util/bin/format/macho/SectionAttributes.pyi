from typing import List
import java.lang


class SectionAttributes(object):
    SECTION_ATTRIBUTES_MASK: int = -256
    SECTION_ATTRIBUTES_SYS: int = 16776960
    SECTION_ATTRIBUTES_USR: int = -16777216
    S_ATTR_EXT_RELOC: int = 512
    S_ATTR_LIVE_SUPPORT: int = 134217728
    S_ATTR_LOC_RELOC: int = 256
    S_ATTR_NO_DEAD_STRIP: int = 268435456
    S_ATTR_NO_TOC: int = 1073741824
    S_ATTR_PURE_INSTRUCTIONS: int = -2147483648
    S_ATTR_SELF_MODIFYING_CODE: int = 67108864
    S_ATTR_SOME_INSTRUCTIONS: int = 1024
    S_ATTR_STRIP_STATIC_SYMS: int = 536870912



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def getAttributeNames(attributes: int) -> List[unicode]: ...

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
