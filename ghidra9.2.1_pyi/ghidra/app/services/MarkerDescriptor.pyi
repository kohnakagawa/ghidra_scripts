import ghidra.program.util
import java.lang
import javax.swing


class MarkerDescriptor(object):
    """
    Allows clients to specify how MarkerLocations are navigated, as well as how they
     should be painted
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getIcon(self, loc: ghidra.program.util.MarkerLocation) -> javax.swing.ImageIcon:
        """
        Called to get the icon that corresponds to the given location
        @param loc the marker location
        @return the icon; may be null
        """
        ...

    def getProgramLocation(self, loc: ghidra.program.util.MarkerLocation) -> ghidra.program.util.ProgramLocation:
        """
        Called when the navigation bar to the right of the window is clicked to allow the the
         creator of a Marker an opportunity to provide a more specific ProgramLocation for
         navigation. If null is specified, the client will navigate to the corresponding address.
        @param loc the marker location
        @return the desired location; may be null
        """
        ...

    def getTooltip(self, loc: ghidra.program.util.MarkerLocation) -> unicode:
        """
        Called to get a tool tip for a marker under the cursor in the marker panel
        @param loc the marker location
        @return the tooltip; may be null
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
