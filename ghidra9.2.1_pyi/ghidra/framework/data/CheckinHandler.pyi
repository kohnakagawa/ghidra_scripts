import java.lang


class CheckinHandler(object):
    """
    CheckinHandler facilitates application callbacks during
     the check-in of a DomainFile.
    """









    def createKeepFile(self) -> bool:
        """
        Returns true if the system should create a keep file copy of the user's check-in file.
        @throws CancelledException thrown if user cancels the check-in
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getComment(self) -> unicode:
        """
        Returns the check-in comment.
        @return the check-in comment
        @throws CancelledException thrown if user cancels the check-in
        """
        ...

    def hashCode(self) -> int: ...

    def keepCheckedOut(self) -> bool:
        """
        Returns true if check-out state should be retained.
        @return true if check-out state should be retained
        @throws CancelledException thrown if user cancels the check-in
        """
        ...

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
    def comment(self) -> unicode: ...
