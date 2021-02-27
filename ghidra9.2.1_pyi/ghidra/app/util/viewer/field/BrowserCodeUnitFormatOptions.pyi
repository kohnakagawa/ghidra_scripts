import ghidra.framework.options
import ghidra.program.model.listing
import ghidra.program.model.listing.CodeUnitFormatOptions
import java.lang
import javax.swing.event


class BrowserCodeUnitFormatOptions(ghidra.program.model.listing.CodeUnitFormatOptions, ghidra.framework.options.OptionsChangeListener):








    def addChangeListener(self, listener: javax.swing.event.ChangeListener) -> None:
        """
        Add format change listener.
         Listeners will only be notified if autoUpdate was true when instantiated.
        @param listener the listener
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def followReferencedPointers(self) -> bool:
        """
        Get current state of the Follow Referenced Pointers option.
        @return true if operand pointer read of indirect references will be followed and
         non-dynamic pointer referenced symbol will be rendered in place of pointer label.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getShowBlockNameOption(self) -> ghidra.program.model.listing.CodeUnitFormatOptions.ShowBlockName:
        """
        Get current ShowBlockName option
        @return ShowBlockName option
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def optionsChanged(self, options: ghidra.framework.options.ToolOptions, optionName: unicode, oldValue: object, newValue: object) -> None: ...

    def removeChangeListener(self, listener: javax.swing.event.ChangeListener) -> None:
        """
        Remove format change listener
        @param listener the listener
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
