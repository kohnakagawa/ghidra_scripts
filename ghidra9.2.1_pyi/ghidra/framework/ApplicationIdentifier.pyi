import ghidra.framework
import java.lang


class ApplicationIdentifier(object):
    """
    Class to represent an application's unique identifier.  An application identifier is made up
     of an application name, an application version, and an application release name.

     The identifier format is (\.+) - \d\.\d(\.\d)?(\-.+)? _ (\.+)
                              name         version        release name

     Application names will be converted to all lowercase and application release names will be
     converted to all uppercase.  Both will have spaces removed from their names.

     Examples:

     ghidra-7.4_DEV

    """





    @overload
    def __init__(self, identifier: unicode):
        """
        Creates a new {@link ApplicationIdentifier} object from the given string.
        @param identifier An identifier string.
        @throws IllegalArgumentException if the identifier string failed to parse.  The
           exception's message has more detailed information about why it failed.
        """
        ...

    @overload
    def __init__(self, applicationProperties: ghidra.framework.ApplicationProperties):
        """
        Creates a new {@link ApplicationIdentifier} object from an {@link ApplicationProperties}.
        @param applicationProperties An {@link ApplicationProperties}.
        @throws IllegalArgumentException if required elements from the {@link ApplicationProperties}
           were missing or otherwise failed to parse.  The exception's message has more detailed
           information about why it failed.
        """
        ...



    def equals(self, obj: object) -> bool: ...

    def getApplicationName(self) -> unicode:
        """
        Gets the application name.
        @return The application name.
        """
        ...

    def getApplicationReleaseName(self) -> unicode:
        """
        Gets the application release name.
        @return The application release name.
        """
        ...

    def getApplicationVersion(self) -> ghidra.framework.ApplicationVersion:
        """
        Gets the {@link ApplicationVersion application version}.
        @return The {@link ApplicationVersion application version}.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

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
    def applicationName(self) -> unicode: ...

    @property
    def applicationReleaseName(self) -> unicode: ...

    @property
    def applicationVersion(self) -> ghidra.framework.ApplicationVersion: ...
