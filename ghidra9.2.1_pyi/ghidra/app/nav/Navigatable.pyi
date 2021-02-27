import ghidra.app.nav
import ghidra.app.util
import ghidra.program.model.listing
import ghidra.program.util
import java.lang
import javax.swing


class Navigatable(object):
    """
    Interface for ComponentProviders to implement if they support basic navigation and selection
     capabilities.  Implementing this interface will provide the provider with navigation history
     and actions that require navigation or selection. (Search Text, Search Memory, Select bytes,
     Select instructions, etc.)
    """

    DEFAULT_NAVIGATABLE_ID: long = -0x1L







    def addNavigatableListener(self, listener: ghidra.app.nav.NavigatableRemovalListener) -> None:
        """
        Adds a listener to be notified if this Navigatable is terminated
        @param listener the listener to be notified when this Navigatable is closed
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getHighlight(self) -> ghidra.program.util.ProgramSelection:
        """
        Returns the current highlight of this Navigatable
        @return the current highlight of this Navigatable
        """
        ...

    def getInstanceID(self) -> long: ...

    def getLocation(self) -> ghidra.program.util.ProgramLocation:
        """
        Returns the current location of this Navigatable
        @return the current location of this Navigatable
        """
        ...

    def getMemento(self) -> ghidra.app.nav.LocationMemento:
        """
        Returns the view state for this navigatable
        @return the view state for this navigatable
        """
        ...

    def getNavigatableIcon(self) -> javax.swing.Icon:
        """
        Returns an icon that represents this Navigatable
        @return the icon
        """
        ...

    def getProgram(self) -> ghidra.program.model.listing.Program:
        """
        Returns the current Program of this Navigatable
        @return the current Program of this Navigatable
        """
        ...

    def getSelection(self) -> ghidra.program.util.ProgramSelection:
        """
        Returns the current selection of this Navigatable
        @return the current selection of this Navigatable
        """
        ...

    def goTo(self, program: ghidra.program.model.listing.Program, location: ghidra.program.util.ProgramLocation) -> bool:
        """
        Commands this navigatable to goto (display) the given program and location
        @param program the program
        @param location the location in that program to display
        @return true if the goto was successful
        """
        ...

    def hashCode(self) -> int: ...

    def isConnected(self) -> bool:
        """
        Returns true if this Navigatable is "connected".  Navigatables are connected if they
         produce and consume location and selection events.
        @return true if this Navigatable is "connected"
        """
        ...

    def isDisposed(self) -> bool:
        """
        Returns true if this navigatable is no longer valid, false if it is still good
        @return true if this navigatable is no longer valid, false if it is still good
        """
        ...

    def isVisible(self) -> bool:
        """
        Returns true if this provider is visible
        @return true if visible
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeHighlightProvider(self, highlightProvider: ghidra.app.util.HighlightProvider, program: ghidra.program.model.listing.Program) -> None:
        """
        Removes the given highlight provider for the given program
        @param highlightProvider the provider
        @param program the program
        """
        ...

    def removeNavigatableListener(self, listener: ghidra.app.nav.NavigatableRemovalListener) -> None:
        """
        Removes a listener to be notified if this Navigatable is terminated.
        @param listener the listener that no longer should be notified when this Navigatable is
                closed.
        """
        ...

    def requestFocus(self) -> None:
        """
        Tells this provider to request focus.
        """
        ...

    def setHighlight(self, highlight: ghidra.program.util.ProgramSelection) -> None:
        """
        Tells this Navigatable to set its highlight to the given highlight
        @param highlight the highlight to set.
        """
        ...

    def setHighlightProvider(self, highlightProvider: ghidra.app.util.HighlightProvider, program: ghidra.program.model.listing.Program) -> None:
        """
        Set the highlight provider for the given program
        @param highlightProvider the provider
        @param program the program
        """
        ...

    def setMemento(self, memento: ghidra.app.nav.LocationMemento) -> None:
        """
        Sets the view state for this navigatable.  This is used later to restore the view state.
        @param memento the state of this navigatable
        """
        ...

    def setSelection(self, selection: ghidra.program.util.ProgramSelection) -> None:
        """
        Tells this Navigatable to set its selection to the given selection
        @param selection the selection to set.
        """
        ...

    def supportsHighlight(self) -> bool:
        """
        Returns true if this navigatable supports highlighting
        @return true if this navigatable supports highlighting
        """
        ...

    def supportsMarkers(self) -> bool:
        """
        Currently only the 'connected' windows support markers
        @return true if this navigatable supports markers
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def connected(self) -> bool: ...

    @property
    def disposed(self) -> bool: ...

    @property
    def highlight(self) -> ghidra.program.util.ProgramSelection: ...

    @highlight.setter
    def highlight(self, value: ghidra.program.util.ProgramSelection) -> None: ...

    @property
    def instanceID(self) -> long: ...

    @property
    def location(self) -> ghidra.program.util.ProgramLocation: ...

    @property
    def memento(self) -> ghidra.app.nav.LocationMemento: ...

    @memento.setter
    def memento(self, value: ghidra.app.nav.LocationMemento) -> None: ...

    @property
    def navigatableIcon(self) -> javax.swing.Icon: ...

    @property
    def program(self) -> ghidra.program.model.listing.Program: ...

    @property
    def selection(self) -> ghidra.program.util.ProgramSelection: ...

    @selection.setter
    def selection(self, value: ghidra.program.util.ProgramSelection) -> None: ...

    @property
    def visible(self) -> bool: ...
