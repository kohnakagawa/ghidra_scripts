from typing import List
import docking.widgets
import ghidra.app.util.datatype
import ghidra.program.model.data
import java.awt.event
import java.lang
import java.util
import javax.swing
import javax.swing.event
import javax.swing.tree


class DataTypeSelectionEditor(javax.swing.AbstractCellEditor):
    """
    An editor that is used to show the DropDownSelectionTextField for the entering of
     data types by name and offers the user of a completion window.  This editor also provides a
     browse button that when pressed will show a data type tree so that the user may browse a tree
     of known data types.

     The typical usage of this class is in conjunction with the DataTypeChooserDialog.   The
     dialog uses this editor as part of its DataType selection process.  Users seeking a dialog
     that allows users to choose DataTypes are encouraged to use that dialog.  If you wish to add
     this editor to a widget directly, then see below.

     Stand Alone Usage
     In order to use this component directly you need to call #getEditorComponent().  This
     will give you a Component for editing.

     In order to know when changes are made to the component you need to add a DocumentListener
     via the #addDocumentListener(DocumentListener) method.  The added listener will be
     notified as the user enters text into the editor's text field.  Then, to determine when there
     is as valid DataType in the field you may call #validateUserSelection().
    """





    @overload
    def __init__(self, service: ghidra.app.services.DataTypeManagerService, maxSize: int, allowedDataTypes: ghidra.util.data.DataTypeParser.AllowedDataTypes): ...

    @overload
    def __init__(self, serviceProvider: ghidra.framework.plugintool.ServiceProvider, maxSize: int, allowedDataTypes: ghidra.util.data.DataTypeParser.AllowedDataTypes): ...



    def addCellEditorListener(self, __a0: javax.swing.event.CellEditorListener) -> None: ...

    def addDocumentListener(self, listener: javax.swing.event.DocumentListener) -> None:
        """
        Adds a document listener to the text field editing component of this editor so that users
         can be notified when the text contents of the editor change.  You may verify whether the
         text changes represent a valid DataType by calling {@link #validateUserSelection()}.
        @param listener the listener to add.
        @see #validateUserSelection()
        """
        ...

    def addFocusListener(self, listener: java.awt.event.FocusListener) -> None: ...

    def cancelCellEditing(self) -> None: ...

    def containsValidDataType(self) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getBrowseButton(self) -> javax.swing.JButton: ...

    def getCellEditorListeners(self) -> List[javax.swing.event.CellEditorListener]: ...

    def getCellEditorValue(self) -> object:
        """
        @see javax.swing.CellEditor#getCellEditorValue()
        """
        ...

    def getCellEditorValueAsDataType(self) -> ghidra.program.model.data.DataType: ...

    def getCellEditorValueAsText(self) -> unicode:
        """
        Returns the text value of the editor's text field.
        @return the text value of the editor's text field.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDropDownTextField(self) -> docking.widgets.DropDownSelectionTextField: ...

    def getEditorComponent(self) -> javax.swing.JComponent:
        """
        Returns the component that allows the user to edit.
        @return the component that allows the user to edit.
        """
        ...

    def getNavigationDirection(self) -> ghidra.app.util.datatype.NavigationDirection:
        """
        Returns the direction of the user triggered navigation; null if the user did not trigger
         navigation out of this component.
        """
        ...

    def hashCode(self) -> int: ...

    def isCellEditable(self, __a0: java.util.EventObject) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeCellEditorListener(self, __a0: javax.swing.event.CellEditorListener) -> None: ...

    def removeDocumentListener(self, listener: javax.swing.event.DocumentListener) -> None:
        """
        Removes a previously added document listener.
        @param listener the listener to remove.s
        """
        ...

    def removeFocusListener(self, listener: java.awt.event.FocusListener) -> None: ...

    def requestFocus(self) -> None: ...

    def setCellEditorValue(self, dataType: ghidra.program.model.data.DataType) -> None:
        """
        Sets the value to be edited on this cell editor.
        @param dataType The data type which is to be edited.
        """
        ...

    def setCellEditorValueAsText(self, text: unicode) -> None: ...

    def setConsumeEnterKeyPress(self, consume: bool) -> None:
        """
        @see DropDownSelectionTextField#setConsumeEnterKeyPress(boolean)
        """
        ...

    def setDefaultSelectedTreePath(self, path: javax.swing.tree.TreePath) -> None:
        """
        Sets the initially selected node in the data type tree that the user can choose to
         show.
        @param path The path to set
        """
        ...

    def setPreferredDataTypeManager(self, dataTypeManager: ghidra.program.model.data.DataTypeManager) -> None:
        """
        Sets the {@link DataTypeManager} to use when the chooser is forced to parse the given
         data type text to resolve the data type.  If the users chooses a type, then this value
         is not used.  Note that setting this value does not restrict the parser to just the
         given value, but rather the given value is the preferred manager and is thus searched
         first.
        @param dataTypeManager the preferred data type manager
        """
        ...

    def setTabCommitsEdit(self, doesCommit: bool) -> None: ...

    def shouldSelectCell(self, __a0: java.util.EventObject) -> bool: ...

    def stopCellEditing(self) -> bool: ...

    def toString(self) -> unicode: ...

    def validateUserSelection(self) -> bool:
        """
        Returns true if the current value of the data type editor is a know data type.
        @return true if the current value of the data type editor is a know data type.
        @throws InvalidDataTypeException If the current text in the editor's text field could not
                 be parsed into a valid DataType
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def browseButton(self) -> javax.swing.JButton: ...

    @property
    def cellEditorValue(self) -> object: ...

    @property
    def cellEditorValueAsDataType(self) -> ghidra.program.model.data.DataType: ...

    @property
    def cellEditorValueAsText(self) -> unicode: ...

    @cellEditorValueAsText.setter
    def cellEditorValueAsText(self, value: unicode) -> None: ...

    @property
    def consumeEnterKeyPress(self) -> None: ...  # No getter available.

    @consumeEnterKeyPress.setter
    def consumeEnterKeyPress(self, value: bool) -> None: ...

    @property
    def defaultSelectedTreePath(self) -> None: ...  # No getter available.

    @defaultSelectedTreePath.setter
    def defaultSelectedTreePath(self, value: javax.swing.tree.TreePath) -> None: ...

    @property
    def dropDownTextField(self) -> docking.widgets.DropDownSelectionTextField: ...

    @property
    def editorComponent(self) -> javax.swing.JComponent: ...

    @property
    def navigationDirection(self) -> ghidra.app.util.datatype.NavigationDirection: ...

    @property
    def preferredDataTypeManager(self) -> None: ...  # No getter available.

    @preferredDataTypeManager.setter
    def preferredDataTypeManager(self, value: ghidra.program.model.data.DataTypeManager) -> None: ...

    @property
    def tabCommitsEdit(self) -> None: ...  # No getter available.

    @tabCommitsEdit.setter
    def tabCommitsEdit(self, value: bool) -> None: ...
