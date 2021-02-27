from typing import List
import ghidra.app.plugin.core.spaceview
import java.lang


class PixelType(java.lang.Enum):
    CODE_FLOW: ghidra.app.plugin.core.spaceview.PixelType = CODE_FLOW
    CODE_MEMORY: ghidra.app.plugin.core.spaceview.PixelType = CODE_MEMORY
    CODE_NORMAL: ghidra.app.plugin.core.spaceview.PixelType = CODE_NORMAL
    CODE_SPECIAL: ghidra.app.plugin.core.spaceview.PixelType = CODE_SPECIAL
    DEF_DATA0: ghidra.app.plugin.core.spaceview.PixelType = DEF_DATA0
    DEF_DATA1: ghidra.app.plugin.core.spaceview.PixelType = DEF_DATA1
    DEF_DATA2: ghidra.app.plugin.core.spaceview.PixelType = DEF_DATA2
    DEF_DATA3: ghidra.app.plugin.core.spaceview.PixelType = DEF_DATA3
    DEF_DATA4: ghidra.app.plugin.core.spaceview.PixelType = DEF_DATA4
    DEF_DATA5: ghidra.app.plugin.core.spaceview.PixelType = DEF_DATA5
    DEF_DATA6: ghidra.app.plugin.core.spaceview.PixelType = DEF_DATA6
    DEF_DATA7: ghidra.app.plugin.core.spaceview.PixelType = DEF_DATA7
    ERROR: ghidra.app.plugin.core.spaceview.PixelType = ERROR
    EXTERNAL: ghidra.app.plugin.core.spaceview.PixelType = EXTERNAL
    FUN_CODE_FLOW: ghidra.app.plugin.core.spaceview.PixelType = FUN_CODE_FLOW
    FUN_CODE_MEMORY: ghidra.app.plugin.core.spaceview.PixelType = FUN_CODE_MEMORY
    FUN_CODE_NORMAL: ghidra.app.plugin.core.spaceview.PixelType = FUN_CODE_NORMAL
    FUN_CODE_SPECIAL: ghidra.app.plugin.core.spaceview.PixelType = FUN_CODE_SPECIAL
    HIGHLIGHTED: ghidra.app.plugin.core.spaceview.PixelType = HIGHLIGHTED
    SELECTED: ghidra.app.plugin.core.spaceview.PixelType = SELECTED
    SEL_AND_HIGH: ghidra.app.plugin.core.spaceview.PixelType = SEL_AND_HIGH
    UNDEF_DATA0: ghidra.app.plugin.core.spaceview.PixelType = UNDEF_DATA0
    UNDEF_DATA1: ghidra.app.plugin.core.spaceview.PixelType = UNDEF_DATA1
    UNDEF_DATA2: ghidra.app.plugin.core.spaceview.PixelType = UNDEF_DATA2
    UNDEF_DATA3: ghidra.app.plugin.core.spaceview.PixelType = UNDEF_DATA3
    UNDEF_DATA4: ghidra.app.plugin.core.spaceview.PixelType = UNDEF_DATA4
    UNDEF_DATA5: ghidra.app.plugin.core.spaceview.PixelType = UNDEF_DATA5
    UNDEF_DATA6: ghidra.app.plugin.core.spaceview.PixelType = UNDEF_DATA6
    UNDEF_DATA7: ghidra.app.plugin.core.spaceview.PixelType = UNDEF_DATA7
    UNINIT_DATA: ghidra.app.plugin.core.spaceview.PixelType = UNINIT_DATA
    UNINIT_UNUSED: ghidra.app.plugin.core.spaceview.PixelType = UNINIT_UNUSED
    UNUSED_TYPE: ghidra.app.plugin.core.spaceview.PixelType = UNUSED_TYPE







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDeclaringClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ordinal(self) -> int: ...

    def toString(self) -> unicode: ...

    def type(self) -> int: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.app.plugin.core.spaceview.PixelType: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.plugin.core.spaceview.PixelType]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
