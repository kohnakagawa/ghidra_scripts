import ghidra.program.model.lang
import java.lang


class SelectLanguagePanelListener(object):
    """
    A listener for the SelectLanguagePanel
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def selectIDValidation(self, langID: ghidra.program.model.lang.LanguageID, compilerSpecID: ghidra.program.model.lang.CompilerSpecID) -> None:
        """
        This method is invoked every time a languauge is selected.
         NOTE: the language could be null.
        @param langID the selected language id.
        @param compilerSpecID the selected compiler spec id.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
