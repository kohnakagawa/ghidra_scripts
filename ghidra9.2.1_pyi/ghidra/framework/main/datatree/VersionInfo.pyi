import java.io
import java.lang


class VersionInfo(object, java.io.Serializable):
    """
    Version info that is inside of the VersionInfoTransferable;
     must be serializable.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDomainFilePath(self) -> unicode:
        """
        Get the path to the domain file.
        """
        ...

    def getVersionNumber(self) -> int:
        """
        Get the version number.
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
    def domainFilePath(self) -> unicode: ...

    @property
    def versionNumber(self) -> int: ...
