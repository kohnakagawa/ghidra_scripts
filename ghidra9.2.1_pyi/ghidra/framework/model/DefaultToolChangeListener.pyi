import java.lang


class DefaultToolChangeListener(object):
    """
    Listener that is notified when the default tool specification changes.
    """









    def defaultToolChanged(self, oldName: unicode, newName: unicode) -> None:
        """
        Notification that the default tool specification changed
        @param oldName name of the old default tool
        @param newName name of the new default tool
        """
        ...

    def equals(self, __a0: object) -> bool: ...

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
