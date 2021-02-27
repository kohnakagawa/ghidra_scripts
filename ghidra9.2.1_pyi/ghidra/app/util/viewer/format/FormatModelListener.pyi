import ghidra.app.util.viewer.format
import java.lang


class FormatModelListener(object):
    """
    Interface for listeners to format model changes.
    """









    def equals(self, __a0: object) -> bool: ...

    def formatModelAdded(self, model: ghidra.app.util.viewer.format.FieldFormatModel) -> None:
        """
        Notifies that a new format model was added to the format manager.
        @param model the new model.
        """
        ...

    def formatModelChanged(self, model: ghidra.app.util.viewer.format.FieldFormatModel) -> None:
        """
        Notifies that the given format model was changed.
        @param model the model that was changed.
        """
        ...

    def formatModelRemoved(self, model: ghidra.app.util.viewer.format.FieldFormatModel) -> None:
        """
        Notifies that a format model was removed.
        @param model the model that was removed.
        """
        ...

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
