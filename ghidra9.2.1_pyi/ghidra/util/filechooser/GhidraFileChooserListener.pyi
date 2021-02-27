import java.lang


class GhidraFileChooserListener(object):
    """
    A listener for notifying when the contents
     of the file chooser model have changed.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def modelChanged(self) -> None:
        """
        Invoked when the contents of the file
         chooser model have changed.
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
