import ghidra.framework.options
import java.lang


class CustomOption(object):
    CUSTOM_OPTION_CLASS_NAME_KEY: unicode = u'CUSTOM_OPTION_CLASS'







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def readState(self, saveState: ghidra.framework.options.SaveState) -> None:
        """
        Concrete subclass of WrappedOption should read all of its
         state from the given saveState object.
        @param saveState container of state information
        """
        ...

    def toString(self) -> unicode:
        """
        CustomOption should implement this method to provide a formatted
         string value of this option value.  The returned value will
         be used in support of the {@link Options#getValueAsString(String)}
         and {@link Options#getDefaultValueAsString(String)}.
        @return option value as string
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def writeState(self, saveState: ghidra.framework.options.SaveState) -> None:
        """
        Concrete subclass of WrappedOption should write all of its
         state to the given saveState object.
        @param saveState container of state information
        """
        ...
