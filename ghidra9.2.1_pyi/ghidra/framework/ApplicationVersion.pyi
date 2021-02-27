import ghidra.framework
import java.lang


class ApplicationVersion(object, java.lang.Comparable):
    """
    Class to represent an application's version information.

     The version format is \d\.\d(\.\d)?(\-.+)?

     Note: this class has a natural ordering that is inconsistent with equals (the tag
     part of the version is disregarded in the #compareTo(ApplicationVersion) method).

     Examples:

     7.4
     7.4.1
     7.4.1-BETA

    """





    def __init__(self, version: unicode):
        """
        Creates a new {@link ApplicationVersion} object from the given version string.
        @param version A version string.
        @throws IllegalArgumentException if the version string failed to parse.  The
           exception's message has more detailed information about why it failed.
        """
        ...



    @overload
    def compareTo(self, other: ghidra.framework.ApplicationVersion) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, obj: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getMajor(self) -> int:
        """
        Gets the major version.
        @return The major version.
        """
        ...

    def getMinor(self) -> int:
        """
        Gets the minor version.
        @return The minor version.
        """
        ...

    def getPatch(self) -> int:
        """
        Gets the patch version.
        @return The patch version.
        """
        ...

    def getTag(self) -> unicode:
        """
        Gets the tag.
        @return The tag.  Could be the empty string.
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
    def major(self) -> int: ...

    @property
    def minor(self) -> int: ...

    @property
    def patch(self) -> int: ...

    @property
    def tag(self) -> unicode: ...
