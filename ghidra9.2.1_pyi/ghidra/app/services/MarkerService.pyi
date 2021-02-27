import ghidra.app.services
import ghidra.program.model.address
import ghidra.program.model.listing
import java.awt
import java.lang
import javax.swing
import javax.swing.event


class MarkerService(object):
    """

     Service to manage navigation markers displayed around a scrollable window like the Listing.
     The navigation bar displays the general location of markers for the entire view. The marker bar
     displays a marker at each marked address visible within the view.


     The interface defines priorities for display of markers in Marker Margin and colored bars in
     Navigation Margin. The higher the priority, the more likely the marker/bar will be displayed on
     the top. Areas will always be lower than marker priorities.

      Recommended Usage
     Recommended Usage
     The service used to work independently of Programs.  In order to work effectively this
     service has been changed to associate created markers with individual programs.  Thus, it is
     up to the clients of this class perform lifecycle management of markers created by this
     service.  For example, a client that creates a marker from
     #createAreaMarker(String, String, Program, int, boolean, boolean, boolean, Color) should
     call #removeMarker(MarkerSet, Program) when the markers are no longer used, such as when
     a program has become deactivated.  In this example usage markers are added and removed as the
     user tabs through open programs.
    """

    BOOKMARK_PRIORITY: int = 0
    BREAKPOINT_PRIORITY: int = 50
    CHANGE_PRIORITY: int = -50
    CURSOR_PRIORITY: int = 200
    DIFF_PRIORITY: int = 80
    FUNCTION_COMPARE_CURSOR_PRIORITY: int = 49
    GROUP_PRIORITY: int = -25
    HIGHLIGHT_GROUP: unicode = u'HIGHLIGHT_GROUP'
    HIGHLIGHT_PRIORITY: int = 50
    PROPERTY_PRIORITY: int = 75
    REFERENCE_PRIORITY: int = -10
    SEARCH_PRIORITY: int = 75
    SELECTION_PRIORITY: int = 100







    def addChangeListener(self, listener: javax.swing.event.ChangeListener) -> None:
        """
        Adds a change listener to be notified when markers are added/removed or the addresses in any
         current markerSets are changed
        @param listener the listener
        """
        ...

    @overload
    def createAreaMarker(self, name: unicode, markerDescription: unicode, program: ghidra.program.model.listing.Program, priority: int, showMarkers: bool, showNavigation: bool, colorBackground: bool, color: java.awt.Color) -> ghidra.app.services.MarkerSet:
        """
        Create a Marker display which shows area type markers.
        @param name name of the navigation markers
        @param markerDescription description of the navigation markers
        @param program The program with which the created markers will be associated.
        @param priority to sort out what displays on top, higher is more likely to be on top
        @param showMarkers true indicates to show area markers (on the left side of the browser.)
        @param showNavigation true indicates to show area navigation markers (on the right side of the browser.)
        @param colorBackground if true, then the browser's background color will reflect the marker.
        @param color the color of marked areas.
        @return set of navigation markers
        """
        ...

    @overload
    def createAreaMarker(self, name: unicode, markerDescription: unicode, program: ghidra.program.model.listing.Program, priority: int, showMarkers: bool, showNavigation: bool, colorBackground: bool, color: java.awt.Color, isPreferred: bool) -> ghidra.app.services.MarkerSet:
        """
        Create a Marker display which shows area type markers.
        @param name name of the navigation markers
        @param markerDescription description of the navigation markers
        @param program The program with which the created markers will be associated.
        @param priority to sort out what displays on top, higher is more likely to be on top
        @param showMarkers true indicates to show area markers (on the left side of the browser.)
        @param showNavigation true indicates to show area navigation markers (on the right side of the browser.)
        @param colorBackground if true, then the browser's background color will reflect the marker.
        @param color the color of marked areas.
        @param isPreferred true indicates higher priority than all non-preferred MarkerSets
        @return set of navigation markers
        """
        ...

    @overload
    def createPointMarker(self, name: unicode, markerDescription: unicode, program: ghidra.program.model.listing.Program, priority: int, showMarkers: bool, showNavigation: bool, colorBackground: bool, color: java.awt.Color, icon: javax.swing.ImageIcon) -> ghidra.app.services.MarkerSet:
        """
        Create a Marker display which shows point type markers.
        @param name name of the navigation markers
        @param markerDescription description of the navigation markers
        @param program The program with which the created markers will be associated.
        @param priority to sort out what displays on top, higher is more likely to be on top
        @param showMarkers true indicates to show area markers (on the left side of the browser.)
        @param showNavigation true indicates to show area navigation markers (on the right side of the browser.)
        @param colorBackground if true, then the browser's background color will reflect the marker.
        @param color the color of marked areas in navigation bar
        @param icon icon to display in marker bar
        @return set of navigation markers
        """
        ...

    @overload
    def createPointMarker(self, name: unicode, markerDescription: unicode, program: ghidra.program.model.listing.Program, priority: int, showMarkers: bool, showNavigation: bool, colorBackground: bool, color: java.awt.Color, icon: javax.swing.ImageIcon, isPreferred: bool) -> ghidra.app.services.MarkerSet:
        """
        Create a Marker display which shows point type markers.
        @param name name of the navigation markers
        @param markerDescription description of the navigation markers
        @param program The program with which the created markers will be associated.
        @param priority to sort out what displays on top, higher is more likely to be on top
        @param showMarkers true indicates to show area markers (on the left side of the browser.)
        @param showNavigation true indicates to show area navigation markers (on the right side of the browser.)
        @param colorBackground if true, then the browser's background color will reflect the marker.
        @param color the color of marked areas in navigation bar
        @param icon icon to display in marker bar
        @param isPreferred is prioritized over non-preferred MarkersSets
        @return set of navigation markers
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    @overload
    def getBackgroundColor(self, address: ghidra.program.model.address.Address) -> java.awt.Color:
        """
        Returns the background color associated with the given address.  Each markerSet that supports
         background coloring is checked in priority order to see if it wants to specify a background
         color for the given address.
        @param address the address to check for a background color.
        @return the background color to use for that address or null if no markers contain that address.
        """
        ...

    @overload
    def getBackgroundColor(self, program: ghidra.program.model.listing.Program, address: ghidra.program.model.address.Address) -> java.awt.Color:
        """
        Returns the background color associated with the given program and address. Each markerSet
         that supports background coloring is checked in priority order to see if it wants to specify
         a background color for the given address.

         If {@code program} is the current program, this is equivalent to
          {@link #getBackgroundColor(Address)}.
        @param program the program to check for a background color.
        @param address the address to check for a background color.
        @return the background color to use for that address or null if no markers contain that
                 address.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getMarkerSet(self, name: unicode, program: ghidra.program.model.listing.Program) -> ghidra.app.services.MarkerSet:
        """
        Return the marker set with the given name;
        @param name The name of the marker set for which to search
        @param program The program with which the created markers will be associated.
        @return the markerset with the given name;
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeChangeListener(self, listener: javax.swing.event.ChangeListener) -> None:
        """
        Removes the given change listener from the list of listeners to be notified of changes
        @param listener the listener
        """
        ...

    def removeMarker(self, markerSet: ghidra.app.services.MarkerSet, program: ghidra.program.model.listing.Program) -> None:
        """
        Remove the marker set
        @param markerSet marker set to be removed from navigation bars.
        @param program The program with which the markers are associated.
        """
        ...

    def removeMarkerForGroup(self, groupName: unicode, markerSet: ghidra.app.services.MarkerSet, program: ghidra.program.model.listing.Program) -> None:
        """
        Removes a marker set for a given group name.  If the given marker set is not the marker
         set associated with the given group name, then no action will be taken.
        @param groupName The name associated the marker set with.
        @param markerSet The marker set to add to this service
        @param program The program with which the markers are associated.  May be null if the
                marker is
        @see #setMarkerForGroup(String, MarkerSet, Program)
        """
        ...

    def setMarkerForGroup(self, groupName: unicode, markerSet: ghidra.app.services.MarkerSet, program: ghidra.program.model.listing.Program) -> None:
        """
        Sets a marker set for a given group name.  Any previous marker set associated with the
         given group name will be removed from this marker service.  This method is used to ensure
         that only one marker set is used at any time for a give group.
        @param groupName The name to associate the marker set with.
        @param markerSet The marker set to add to this service
        @param program The program with which the markers are associated.
        @see #removeMarkerForGroup(String, MarkerSet, Program)
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
