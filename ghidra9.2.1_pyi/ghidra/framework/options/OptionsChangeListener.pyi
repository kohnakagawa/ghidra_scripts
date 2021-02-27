import ghidra.framework.options
import java.lang


class OptionsChangeListener(object):
    """
    Interface for notifying listeners when options change.

     Register with ToolOptions#addOptionsChangeListener(OptionsChangeListener).
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def optionsChanged(self, options: ghidra.framework.options.ToolOptions, optionName: unicode, oldValue: object, newValue: object) -> None:
        """
        Notification that an option changed.
         <p>
         Note: to reject an options change, you can throw a
         {@link OptionsVetoException}.
        @param options options object containing the property that changed
        @param optionName name of option that changed
        @param oldValue old value of the option
        @param newValue new value of the option
        @throws OptionsVetoException if a change is rejected
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
