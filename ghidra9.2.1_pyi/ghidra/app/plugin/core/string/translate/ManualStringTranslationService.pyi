from typing import List
import ghidra.app.services
import ghidra.program.model.listing
import ghidra.program.util
import ghidra.util
import java.lang


class ManualStringTranslationService(object, ghidra.app.services.StringTranslationService):




    def __init__(self): ...



    @staticmethod
    def createStringTranslationServiceHelpLocation(__a0: java.lang.Class, __a1: ghidra.app.services.StringTranslationService) -> ghidra.util.HelpLocation: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getHelpLocation(self) -> ghidra.util.HelpLocation: ...

    def getTranslationServiceName(self) -> unicode: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def setTranslatedValue(__a0: ghidra.program.model.listing.Program, __a1: ghidra.program.util.ProgramLocation, __a2: unicode) -> None: ...

    def toString(self) -> unicode: ...

    def translate(self, __a0: ghidra.program.model.listing.Program, __a1: List[object]) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def helpLocation(self) -> ghidra.util.HelpLocation: ...

    @property
    def translationServiceName(self) -> unicode: ...