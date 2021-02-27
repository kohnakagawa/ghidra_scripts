from typing import List
import ghidra.app.util
import ghidra.app.util.viewer.format
import ghidra.framework.options
import ghidra.framework.plugintool
import ghidra.program.model.listing
import java.lang


class FormatManager(object, ghidra.framework.options.OptionsChangeListener):
    """
    Class to manage the set of format models.
    """

    ARRAY_DISPLAY_DESCRIPTION: unicode = u'Adjusts the Array Field display'
    ARRAY_DISPLAY_OPTIONS: unicode = u'Array Options.Array Display Options'
    ARRAY_OPTIONS_GROUP: unicode = u'Array Options'
    HIGHLIGHT_ALT_COLOR_NAME: unicode = u'Cursor Text Highlight.Alternate Highlight Color'
    HIGHLIGHT_COLOR_NAME: unicode = u'Cursor Text Highlight.Highlight Color'



    def __init__(self, displayOptions: ghidra.framework.options.ToolOptions, fieldOptions: ghidra.framework.options.ToolOptions):
        """
        Constructs a new FormatManager.
        @param displayOptions the Options containing display options (color, fonts, etc)
        @param fieldOptions the Options contains specific field options.
        """
        ...



    def addFormatModelListener(self, listener: ghidra.app.util.viewer.format.FormatModelListener) -> None:
        """
        Adds a listener to be notified when a format changes.
        @param listener the listener to be added.
        """
        ...

    def addHighlightProvider(self, provider: ghidra.app.util.HighlightProvider) -> None:
        """
        Adds a HighlightProvider
        @param provider the provider to use.
        @see #removeHighlightProvider(HighlightProvider)
        @see #getHighlightProviders()
        """
        ...

    def createClone(self) -> ghidra.app.util.viewer.format.FormatManager: ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getCodeUnitFormat(self) -> ghidra.app.util.viewer.format.FieldFormatModel:
        """
        Returns the format model for a code unit.
        """
        ...

    def getDisplayOptions(self) -> ghidra.framework.options.ToolOptions:
        """
        Returns the Options used for display properties.
        """
        ...

    def getDividerModel(self) -> ghidra.app.util.viewer.format.FieldFormatModel:
        """
        Returns the format model for the address break (divider)
        """
        ...

    def getFieldOptions(self) -> ghidra.framework.options.ToolOptions:
        """
        Returns the Options used for field specific properties.
        """
        ...

    def getFormatHighlightProvider(self) -> ghidra.app.util.HighlightProvider:
        """
        Returns the {@link HighlightProvider} that should be used when creating {@link FieldFactory}
         objects.
        """
        ...

    def getFunctionFormat(self) -> ghidra.app.util.viewer.format.FieldFormatModel:
        """
        Returns the format model for the function signature
        """
        ...

    def getFunctionVarFormat(self) -> ghidra.app.util.viewer.format.FieldFormatModel:
        """
        Returns the format model for the function variables.
        """
        ...

    def getHighlightProviders(self) -> List[ghidra.app.util.HighlightProvider]:
        """
        Gets all {@link HighlightProvider}s installed on this FormatManager via the
         {@link #addHighlightProvider(HighlightProvider)}.
        @return all {@link HighlightProvider}s installed on this FormatManager.
        """
        ...

    def getMaxNumRows(self) -> int:
        """
        Returns the maximum number of possible rows in a layout. This would only
         occur if some address had every possible type of information to be displayed.
        """
        ...

    def getMaxRowCount(self) -> int: ...

    def getMaxWidth(self) -> int:
        """
        Returns the width of the widest model in this manager.
        """
        ...

    def getModel(self, index: int) -> ghidra.app.util.viewer.format.FieldFormatModel:
        """
        Returns the format model for the given index.
        @param index the index of the format model to return.
        """
        ...

    def getNumModels(self) -> int:
        """
        Returns the total number of model in the format manager.
        """
        ...

    def getOpenDataFormat(self, data: ghidra.program.model.listing.Data) -> ghidra.app.util.viewer.format.FieldFormatModel:
        """
        Returns the format model to use for the internals of open structures.
        @param data the data code unit to get the format model for.
        """
        ...

    def getPlateFormat(self) -> ghidra.app.util.viewer.format.FieldFormatModel:
        """
        Returns the format model for the plate field
        """
        ...

    def getServiceProvider(self) -> ghidra.framework.plugintool.ServiceProvider: ...

    def hashCode(self) -> int: ...

    def modelChanged(self, model: ghidra.app.util.viewer.format.FieldFormatModel) -> None:
        """
        Notifies listeners that the given model has changed.
        @param model the format model that changed.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def optionsChanged(self, options: ghidra.framework.options.ToolOptions, name: unicode, oldValue: object, newValue: object) -> None: ...

    def readState(self, saveState: ghidra.framework.options.SaveState) -> None:
        """
        Restores the state of this LayoutController from the given SaveState
         object.
        @param saveState the SaveState to read from.
        """
        ...

    def removeFormatModleListener(self, listener: ghidra.app.util.viewer.format.FormatModelListener) -> None:
        """
        Removes the given listener from the list of listeners to be notified of a
         format change.
        @param listener the listener to be removed.
        """
        ...

    def removeHighlightProvider(self, provider: ghidra.app.util.HighlightProvider) -> None:
        """
        Removes the provider
        @param provider the provider to remove.
        @see #addHighlightProvider(HighlightProvider)
        """
        ...

    def saveState(self, saveState: ghidra.framework.options.SaveState) -> None:
        """
        Saves the state of this LayoutManager to the SaveState object.
        @param saveState the SaveState object to write to.
        """
        ...

    def setDefaultFormat(self, modelID: int) -> None:
        """
        Resets the model with the given id to its default format.
        @param modelID the id of the model to reset.
        """
        ...

    def setDefaultFormats(self) -> None:
        """
        Resets all format models to their default format.
        """
        ...

    def setServiceProvider(self, provider: ghidra.framework.plugintool.ServiceProvider) -> None:
        """
        Sets the service provider used by the field factory objects.
        @param provider the service provider
        """
        ...

    def toString(self) -> unicode: ...

    def update(self) -> None:
        """
        update all listeners that a model has changed.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def codeUnitFormat(self) -> ghidra.app.util.viewer.format.FieldFormatModel: ...

    @property
    def defaultFormat(self) -> None: ...  # No getter available.

    @defaultFormat.setter
    def defaultFormat(self, value: int) -> None: ...

    @property
    def displayOptions(self) -> ghidra.framework.options.ToolOptions: ...

    @property
    def dividerModel(self) -> ghidra.app.util.viewer.format.FieldFormatModel: ...

    @property
    def fieldOptions(self) -> ghidra.framework.options.ToolOptions: ...

    @property
    def formatHighlightProvider(self) -> ghidra.app.util.HighlightProvider: ...

    @property
    def functionFormat(self) -> ghidra.app.util.viewer.format.FieldFormatModel: ...

    @property
    def functionVarFormat(self) -> ghidra.app.util.viewer.format.FieldFormatModel: ...

    @property
    def highlightProviders(self) -> List[object]: ...

    @property
    def maxNumRows(self) -> int: ...

    @property
    def maxRowCount(self) -> int: ...

    @property
    def maxWidth(self) -> int: ...

    @property
    def numModels(self) -> int: ...

    @property
    def plateFormat(self) -> ghidra.app.util.viewer.format.FieldFormatModel: ...

    @property
    def serviceProvider(self) -> ghidra.framework.plugintool.ServiceProvider: ...

    @serviceProvider.setter
    def serviceProvider(self, value: ghidra.framework.plugintool.ServiceProvider) -> None: ...
