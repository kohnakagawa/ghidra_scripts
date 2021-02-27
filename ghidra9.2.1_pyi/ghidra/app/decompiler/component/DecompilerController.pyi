import docking.widgets.fieldpanel.support
import ghidra.app.decompiler
import ghidra.app.decompiler.component
import ghidra.program.model.listing
import ghidra.program.model.pcode
import ghidra.program.util
import java.io
import java.lang
import utility.function


class DecompilerController(object):
    """
    Coordinates the interactions between the DecompilerProvider, DecompilerPanel, and the DecompilerManager
    """





    def __init__(self, handler: ghidra.app.decompiler.component.DecompilerCallbackHandler, options: ghidra.app.decompiler.DecompileOptions, clipboard: ghidra.app.plugin.core.decompile.DecompilerClipboardProvider): ...



    def clear(self) -> None:
        """
        clears all internal state and releases all resources.  Called when the provider is no
         longer visible or the currently displayed program is closed.
        """
        ...

    def clearCache(self) -> None: ...

    def display(self, program: ghidra.program.model.listing.Program, location: ghidra.program.util.ProgramLocation, viewerPosition: docking.widgets.fieldpanel.support.ViewerPosition) -> None:
        """
        Shows the function containing the given location in the decompilerPanel.  Also, positions the
         decompilerPanel's cursor to the closest equivalent position. If the decompilerPanel is
         already displaying the function, then only the cursor is repositioned.  To force a
         re-decompile use {@link #refreshDisplay(Program, ProgramLocation, File)}.
        @param program the program for the given location
        @param location the location containing the function to be displayed and the location in
         that function to position the cursor.
        @param viewerPosition the viewer position
        """
        ...

    def dispose(self) -> None:
        """
        Called by the provider when the provider is disposed.  Once dispose is called, it should
         never be used again.
        """
        ...

    def doWhenNotBusy(self, c: utility.function.Callback) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def exportLocation(self) -> None: ...

    def getCCodeModel(self) -> ghidra.app.decompiler.ClangTokenGroup: ...

    def getClass(self) -> java.lang.Class: ...

    def getDecompileData(self) -> ghidra.app.decompiler.component.DecompileData: ...

    def getDecompilerPanel(self) -> ghidra.app.decompiler.component.DecompilerPanel: ...

    def getFunction(self) -> ghidra.program.model.listing.Function: ...

    def getHighFunction(self) -> ghidra.program.model.pcode.HighFunction: ...

    def getLocation(self) -> ghidra.program.util.ProgramLocation: ...

    def getProgram(self) -> ghidra.program.model.listing.Program: ...

    def hasDecompileResults(self) -> bool: ...

    def hashCode(self) -> int: ...

    def isDecompiling(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def programClosed(self, closedProgram: ghidra.program.model.listing.Program) -> None: ...

    def refreshDisplay(self, program: ghidra.program.model.listing.Program, location: ghidra.program.util.ProgramLocation, debugFile: java.io.File) -> None:
        """
        Always decompiles the function containing the given location before positioning the
         decompilerPanel's cursor to the closest equivalent position.
        @param program the program for the given location
        @param location the location containing the function to be displayed and the location in
         that function to position the cursor.
        @param debugFile the debug file
        """
        ...

    def resetDecompiler(self) -> None:
        """
        Resets the native decompiler process.  Call this method when the decompiler's view
         of a program has been invalidated, such as when a new overlay space has been added.
        """
        ...

    def setDecompileData(self, decompileData: ghidra.app.decompiler.component.DecompileData) -> None:
        """
        Called by the DecompilerManager to update the currently displayed DecompileData
        @param decompileData the new data
        """
        ...

    def setMouseNavigationEnabled(self, enabled: bool) -> None: ...

    def setOptions(self, decompilerOptions: ghidra.app.decompiler.DecompileOptions) -> None:
        """
        Sets new decompiler options and triggers a new decompile.
        @param decompilerOptions the options
        """
        ...

    def setSelection(self, selection: ghidra.program.util.ProgramSelection) -> None: ...

    def setStatusMessage(self, message: unicode) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def CCodeModel(self) -> ghidra.app.decompiler.ClangTokenGroup: ...

    @property
    def decompileData(self) -> ghidra.app.decompiler.component.DecompileData: ...

    @decompileData.setter
    def decompileData(self, value: ghidra.app.decompiler.component.DecompileData) -> None: ...

    @property
    def decompilerPanel(self) -> ghidra.app.decompiler.component.DecompilerPanel: ...

    @property
    def decompiling(self) -> bool: ...

    @property
    def function(self) -> ghidra.program.model.listing.Function: ...

    @property
    def highFunction(self) -> ghidra.program.model.pcode.HighFunction: ...

    @property
    def location(self) -> ghidra.program.util.ProgramLocation: ...

    @property
    def mouseNavigationEnabled(self) -> None: ...  # No getter available.

    @mouseNavigationEnabled.setter
    def mouseNavigationEnabled(self, value: bool) -> None: ...

    @property
    def options(self) -> None: ...  # No getter available.

    @options.setter
    def options(self, value: ghidra.app.decompiler.DecompileOptions) -> None: ...

    @property
    def program(self) -> ghidra.program.model.listing.Program: ...

    @property
    def selection(self) -> None: ...  # No getter available.

    @selection.setter
    def selection(self, value: ghidra.program.util.ProgramSelection) -> None: ...

    @property
    def statusMessage(self) -> None: ...  # No getter available.

    @statusMessage.setter
    def statusMessage(self, value: unicode) -> None: ...
