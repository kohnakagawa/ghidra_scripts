import ghidra.bitpatterns.gui
import ghidra.bitpatterns.info
import java.lang
import javax.swing


class AlignmentPanelBuilder(ghidra.bitpatterns.gui.ContextRegisterFilterablePanelBuilder):




    def __init__(self): ...



    def applyFilterAction(self) -> None: ...

    def buildAlignmentPanel(self) -> javax.swing.JPanel: ...

    def clearFilterAction(self) -> None: ...

    def enableFilterButtons(self, __a0: bool) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getButtonPanel(self) -> javax.swing.JPanel: ...

    def getClass(self) -> java.lang.Class: ...

    def getContextRegisterFilter(self) -> ghidra.bitpatterns.info.ContextRegisterFilter: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def resetModulus(self) -> None: ...

    def setFsReader(self, __a0: ghidra.bitpatterns.info.FileBitPatternInfoReader) -> None: ...

    def toString(self) -> unicode: ...

    def updateAlignmentPanel(self) -> None: ...

    def updateExtentAndClearFilter(self, __a0: ghidra.bitpatterns.info.ContextRegisterExtent) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def fsReader(self) -> None: ...  # No getter available.

    @fsReader.setter
    def fsReader(self, value: ghidra.bitpatterns.info.FileBitPatternInfoReader) -> None: ...