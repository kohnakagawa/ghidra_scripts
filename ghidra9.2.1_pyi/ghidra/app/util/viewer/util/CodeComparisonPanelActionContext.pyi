import ghidra.app.util.viewer.util
import java.lang


class CodeComparisonPanelActionContext(object):
    """
    Action context for a CodeComparisonPanel.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getCodeComparisonPanel(self) -> ghidra.app.util.viewer.util.CodeComparisonPanel:
        """
        Gets the CodeComparisonPanel associated with this context.
        @return the code comparison panel.
        """
        ...

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

    @property
    def codeComparisonPanel(self) -> ghidra.app.util.viewer.util.CodeComparisonPanel: ...
