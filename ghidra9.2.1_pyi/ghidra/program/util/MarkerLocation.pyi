import ghidra.app.services
import ghidra.program.model.address
import ghidra.program.model.listing
import java.io
import java.lang


class MarkerLocation(object, java.io.Serializable):
    """
    Marker location in the tool navigation bars
    """





    def __init__(self, markers: ghidra.app.services.MarkerSet, program: ghidra.program.model.listing.Program, addr: ghidra.program.model.address.Address, x: int, y: int):
        """
        Construct a new MarkerLocation.
        @param markers marker manager service
        @param program program containing the address
        @param addr address of the location
        @param x x position of the popup point on the screen
        @param y y position of the popup point on the screen
        """
        ...



    def equals(self, obj: object) -> bool: ...

    def getAddr(self) -> ghidra.program.model.address.Address:
        """
        Returns the address.
        @return the address for this marker location
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getMarkerManager(self) -> ghidra.app.services.MarkerSet:
        """
        Returns the Marker Manager.
        @return the marker manager
        """
        ...

    def getProgram(self) -> ghidra.program.model.listing.Program:
        """
        Returns the program.
        @return the program for this marker location
        """
        ...

    def getX(self) -> int:
        """
        Returns the X screen location of the popup point.
        @return the X coordinate for the screen location.
        """
        ...

    def getY(self) -> int:
        """
        Returns the Y screen location of the popup point.
        @return the Y coordinate for the screen location.
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

    @property
    def addr(self) -> ghidra.program.model.address.Address: ...

    @property
    def markerManager(self) -> ghidra.app.services.MarkerSet: ...

    @property
    def program(self) -> ghidra.program.model.listing.Program: ...

    @property
    def x(self) -> int: ...

    @property
    def y(self) -> int: ...
