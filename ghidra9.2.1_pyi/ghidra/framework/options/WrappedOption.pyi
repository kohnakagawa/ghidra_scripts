import ghidra.framework.options
import java.lang


class WrappedOption(object):
    """
    Wrapper class for an object that represents a property value and is
     saved as a set of primitives.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getObject(self) -> object:
        """
        Get the object that is the property value.
        """
        ...

    def getOptionType(self) -> ghidra.framework.options.OptionType: ...

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

    def toString(self) -> unicode: ...

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

    @property
    def object(self) -> object: ...

    @property
    def optionType(self) -> ghidra.framework.options.OptionType: ...
