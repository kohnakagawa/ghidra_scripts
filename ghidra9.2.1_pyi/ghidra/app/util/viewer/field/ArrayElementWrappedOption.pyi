import ghidra.framework.options
import java.lang


class ArrayElementWrappedOption(object, ghidra.framework.options.CustomOption):
    CUSTOM_OPTION_CLASS_NAME_KEY: unicode = u'CUSTOM_OPTION_CLASS'



    def __init__(self): ...



    def equals(self, obj: object) -> bool: ...

    def getArrayElementsPerLine(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def readState(self, saveState: ghidra.framework.options.SaveState) -> None: ...

    def setArrayElementsPerLine(self, arrayElementsPerLine: int) -> None: ...

    def setShowMultipleArrayElementPerLine(self, b: bool) -> None: ...

    def showMultipleArrayElementPerLine(self) -> bool: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def writeState(self, saveState: ghidra.framework.options.SaveState) -> None: ...

    @property
    def arrayElementsPerLine(self) -> int: ...

    @arrayElementsPerLine.setter
    def arrayElementsPerLine(self, value: int) -> None: ...