import docking.action
import docking.widgets.fieldpanel
import docking.widgets.fieldpanel.field
import ghidra.app.nav
import ghidra.app.services
import ghidra.app.util
import ghidra.app.util.viewer.format
import ghidra.app.util.viewer.listingpanel
import ghidra.app.util.viewer.util
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.util
import java.lang
import javax.swing


class CodeViewerService(object):
    """
    Service provided by a plugin that shows the listing from a Program, i.e., a
     Code Viewer. The service allows other plugins to add components and
     actions local to the Code Viewer.
    """









    def addButtonPressedListener(self, listener: ghidra.app.services.ButtonPressedListener) -> None:
        """
        Add a listener that is notified when a mouse button is pressed.
        @param listener
        """
        ...

    def addListingDisplayListener(self, listener: ghidra.app.util.viewer.listingpanel.ListingDisplayListener) -> None:
        """
        Adds a listener to be notified when the set of visible addresses change.
        @param listener the listener to be notified;
        """
        ...

    def addLocalAction(self, action: docking.action.DockingAction) -> None:
        """
        Add an action that is local to the Code Viewer.
        @param action local action to add
        """
        ...

    def addMarginProvider(self, marginProvider: ghidra.app.util.viewer.listingpanel.MarginProvider) -> None:
        """
        Add a provider that shows markers in a program for the portion
         that is visible.
        @param marginProvider provider to add
        """
        ...

    def addOverviewProvider(self, overviewProvider: ghidra.app.util.viewer.listingpanel.OverviewProvider) -> None:
        """
        Add a provider that shows an overview of the program.
        @param overviewProvider provider to add
        """
        ...

    def addProgramDropProvider(self, provider: ghidra.app.util.ProgramDropProvider) -> None:
        """
        Add a provider that will be notified for drag and drop actions.
        @param provider for drag and drop
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getAddressIndexMap(self) -> ghidra.app.util.viewer.util.AddressIndexMap:
        """
        Returns the current address-index-map
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getCurrentField(self) -> docking.widgets.fieldpanel.field.Field:
        """
        Returns the current field under the cursor.
        @return the current field under the cursor.
        """
        ...

    def getCurrentFieldTextSelection(self) -> unicode:
        """
        Returns a String representing the current character-based selection of the currently
         selected field.  If there is no selection, or if there is a {@link ProgramSelection}
         (which spans multiple fields), then this method will return null.
         <p>
         To know which field contains the selection,
        @return the currently selected text <b>within a given field</b>
        """
        ...

    def getCurrentLocation(self) -> ghidra.program.util.ProgramLocation:
        """
        Returns the current cursor location.
        @return the current cursor location.
        """
        ...

    def getCurrentSelection(self) -> ghidra.program.util.ProgramSelection:
        """
        Returns the current program selection (which crosses multiple fields).
        @return the current program selection.
        """
        ...

    def getFieldPanel(self) -> docking.widgets.fieldpanel.FieldPanel:
        """
        Return the fieldPanel.
        """
        ...

    def getFormatManager(self) -> ghidra.app.util.viewer.format.FormatManager: ...

    def getListingModel(self) -> ghidra.app.util.viewer.listingpanel.ListingModel:
        """
        Gets the current ListingLayoutModel;
        @return the current ListingLayoutModel;
        """
        ...

    def getListingPanel(self) -> ghidra.app.util.viewer.listingpanel.ListingPanel:
        """
        Get the main Listing panel for the code viewer service.
        @return the listing panel.
        """
        ...

    def getNavigatable(self) -> ghidra.app.nav.Navigatable:
        """
        Gets the navigatable for the code viewer service.
        @return the navigatable for the code viewer service.
        """
        ...

    def getView(self) -> ghidra.program.model.address.AddressSetView:
        """
        Get Current view that the CodeViewer is showing.
        """
        ...

    def goTo(self, loc: ghidra.program.util.ProgramLocation, centerOnScreen: bool) -> bool:
        """
        Commands the code viewer to position the cursor at the given location.
        @param loc the location at which to position the cursor.
        @param centerOnScreen if true, the location will be placed in the center of the display
         window
        @return true if the location exists.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeButtonPressedListener(self, listener: ghidra.app.services.ButtonPressedListener) -> None:
        """
        Remove the button pressed listener.
        @param listener
        """
        ...

    def removeHighlightProvider(self, provider: ghidra.app.util.HighlightProvider, program: ghidra.program.model.listing.Program) -> None:
        """
        Remove the highlight provider.
        @param provider the provider to remove.
        @param program the program associated with the given provider.
        """
        ...

    def removeListingDisplayListener(self, listener: ghidra.app.util.viewer.listingpanel.ListingDisplayListener) -> None:
        """
        Removes listener from being notified when the set of visible addresses change.
        @param listener the listener to be notified;
        """
        ...

    def removeListingPanel(self, listingPanel: ghidra.app.util.viewer.listingpanel.ListingPanel) -> None:
        """
        Remove the given listing panel from the code viewer.
        """
        ...

    def removeLocalAction(self, action: docking.action.DockingAction) -> None:
        """
        Remove the local action from the Code Viewer.
        @param action local action to remove
        """
        ...

    def removeMarginProvider(self, marginProvider: ghidra.app.util.viewer.listingpanel.MarginProvider) -> None:
        """
        Remove a provider that shows markers in a program for the portion
         that is visible.
        @param marginProvider provider to remove
        """
        ...

    def removeOverviewProvider(self, overviewProvider: ghidra.app.util.viewer.listingpanel.OverviewProvider) -> None:
        """
        Remove a provider that shows an overview of the program.
        @param overviewProvider provider to remove
        """
        ...

    def setCoordinatedListingPanelListener(self, listener: ghidra.app.services.CoordinatedListingPanelListener) -> None:
        """
        Set the {@link CoordinatedListingPanelListener} for this listing.
        @param listener the listener to add.
        """
        ...

    def setHighlightProvider(self, provider: ghidra.app.util.HighlightProvider, program: ghidra.program.model.listing.Program) -> None:
        """
        Set the highlight  provider. The existing provider is replaced
         with the given provider.
        @param provider The provider to set.
        @param program The program with which to associate the given provider.
        """
        ...

    def setListingPanel(self, listingPanel: ghidra.app.util.viewer.listingpanel.ListingPanel) -> None:
        """
        Set a listing panel on the code viewer.
        @param listingPanel the panel to add.
        """
        ...

    def setNorthComponent(self, comp: javax.swing.JComponent) -> None:
        """
        Place a component in the North area of the CodeViewer.
        @param comp component to place in the North area of the CodeViewer
        """
        ...

    def toString(self) -> unicode: ...

    def updateDisplay(self) -> None:
        """
        tells the browser to rebuild the display.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def addressIndexMap(self) -> ghidra.app.util.viewer.util.AddressIndexMap: ...

    @property
    def coordinatedListingPanelListener(self) -> None: ...  # No getter available.

    @coordinatedListingPanelListener.setter
    def coordinatedListingPanelListener(self, value: ghidra.app.services.CoordinatedListingPanelListener) -> None: ...

    @property
    def currentField(self) -> docking.widgets.fieldpanel.field.Field: ...

    @property
    def currentFieldTextSelection(self) -> unicode: ...

    @property
    def currentLocation(self) -> ghidra.program.util.ProgramLocation: ...

    @property
    def currentSelection(self) -> ghidra.program.util.ProgramSelection: ...

    @property
    def fieldPanel(self) -> docking.widgets.fieldpanel.FieldPanel: ...

    @property
    def formatManager(self) -> ghidra.app.util.viewer.format.FormatManager: ...

    @property
    def listingModel(self) -> ghidra.app.util.viewer.listingpanel.ListingModel: ...

    @property
    def listingPanel(self) -> ghidra.app.util.viewer.listingpanel.ListingPanel: ...

    @listingPanel.setter
    def listingPanel(self, value: ghidra.app.util.viewer.listingpanel.ListingPanel) -> None: ...

    @property
    def navigatable(self) -> ghidra.app.nav.Navigatable: ...

    @property
    def northComponent(self) -> None: ...  # No getter available.

    @northComponent.setter
    def northComponent(self, value: javax.swing.JComponent) -> None: ...

    @property
    def view(self) -> ghidra.program.model.address.AddressSetView: ...
