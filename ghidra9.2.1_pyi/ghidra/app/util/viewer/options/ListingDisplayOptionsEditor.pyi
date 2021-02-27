import ghidra.framework.options
import java.beans
import java.lang
import javax.swing


class ListingDisplayOptionsEditor(object, ghidra.framework.options.OptionsEditor):
    """
    Class for editing Listing display properties.
    """

    DEFAULT_FONT: java.awt.Font = java.awt.Font[family=Monospaced,name=Monospaced,style=plain,size=12]



    def __init__(self, options: ghidra.framework.options.Options):
        """
        Constructs a new ListingDisplayOptionsEditor.
        @param options the options object to edit
        """
        ...



    def apply(self) -> None: ...

    def cancel(self) -> None: ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getEditorComponent(self, editableOptions: ghidra.framework.options.Options, editorStateFactory: ghidra.framework.options.EditorStateFactory) -> javax.swing.JComponent: ...

    def hashCode(self) -> int: ...

    def isResizable(self) -> bool:
        """
        Returns true if this component has "good" resizing behavior.  Components
         that do not have this property will be placed in a scrolled pane.
        @return true if resizable
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def reload(self) -> None: ...

    def setOptionsPropertyChangeListener(self, listener: java.beans.PropertyChangeListener) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def resizable(self) -> bool: ...
