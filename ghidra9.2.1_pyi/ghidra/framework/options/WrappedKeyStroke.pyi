import ghidra.framework.options
import java.lang


class WrappedKeyStroke(object, ghidra.framework.options.WrappedOption):
    """
    Wrapper for a KeyStroke that will get saved as a property in an Options
     object.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getObject(self) -> object: ...

    def getOptionType(self) -> ghidra.framework.options.OptionType: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def readState(self, saveState: ghidra.framework.options.SaveState) -> None:
        """
        Read the components for a Key Stroke from the given
         SaveState object to restore this WrappedKeyStroke.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def writeState(self, saveState: ghidra.framework.options.SaveState) -> None:
        """
        Write the components for the wrapped Key Stroke to the given
         SaveState object.
        """
        ...
