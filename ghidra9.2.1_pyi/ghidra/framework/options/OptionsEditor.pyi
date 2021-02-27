import ghidra.framework.options
import java.beans
import java.lang
import javax.swing


class OptionsEditor(object):
    """
    Interface to define methods for an editor that supplies its own
     component to be displayed in the OptionsDialog.
    """









    def apply(self) -> None:
        """
        Apply the changes.
        """
        ...

    def cancel(self) -> None:
        """
        Cancel the changes.
        """
        ...

    def dispose(self) -> None:
        """
        Dispose this editor
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getEditorComponent(self, options: ghidra.framework.options.Options, editorStateFactory: ghidra.framework.options.EditorStateFactory) -> javax.swing.JComponent:
        """
        Get the editor component.
        @param options The editable options that for which a GUI component will be created
        @param editorStateFactory The factory that will provide state objects this options editor
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def reload(self) -> None:
        """
        A signal to reload the GUI widgets in the component created by this editor.  This will
         happen when the options change out from under the editor, such as when the user restores
         the default options values.
        """
        ...

    def setOptionsPropertyChangeListener(self, listener: java.beans.PropertyChangeListener) -> None:
        """
        Sets the options change listener
        @param listener
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
