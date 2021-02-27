import ghidra.framework.options
import java.lang


class WrappedColor(object, ghidra.framework.options.WrappedOption):
    """
    An wrapper object for registering Colors as options.
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
        Reads the saved Color information and reconstructs the Color.
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
        Saves the Color information so that it can be reconstructed.
        """
        ...
