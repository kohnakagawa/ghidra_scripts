import ghidra.framework.plugintool
import java.lang


class Location(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode:
        """
        Returns a description for the location.  This should probably describe the significance of the
         location.  For example, if this location is from an Issue, then what is its relationship to the
         issue.
        @return a descrition for the location.
        """
        ...

    def getStringRepresentation(self) -> unicode:
        """
        Returns a displayable representation of this location.
        @return a displayable representation of this location.
        """
        ...

    def go(self, provider: ghidra.framework.plugintool.ServiceProvider) -> bool:
        """
        Will attempt to navigate to the location as appropriate.  For example, it may use the goto service
         to navigate the code browser to a progam and and address.  Or it could launch a browser and
         display a web page.
        @param provider a service provider that this location can use to find a service to help with
         navigation.
        @return true if the navigation was successful, false otherwise.
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
    def description(self) -> unicode: ...

    @property
    def stringRepresentation(self) -> unicode: ...
