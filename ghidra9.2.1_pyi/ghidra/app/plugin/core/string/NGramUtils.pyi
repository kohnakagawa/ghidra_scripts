from typing import List
import ghidra.app.plugin.core.string
import java.io
import java.lang


class NGramUtils(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getLastLoadedTrigramModel() -> unicode: ...

    @staticmethod
    def getLastLoadedTrigramModelPath() -> unicode: ...

    @staticmethod
    def getMinimumStringLength() -> int: ...

    @staticmethod
    def getModelType() -> unicode: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isLowerCaseModel() -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def scoreString(__a0: ghidra.app.plugin.core.string.StringAndScores) -> None: ...

    @staticmethod
    def scoreStrings(__a0: List[object]) -> None: ...

    @overload
    @staticmethod
    def startNewSession(__a0: ghidra.app.plugin.core.string.StringModel) -> None: ...

    @overload
    @staticmethod
    def startNewSession(__a0: java.io.File) -> None: ...

    @overload
    @staticmethod
    def startNewSession(__a0: unicode, __a1: bool) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
