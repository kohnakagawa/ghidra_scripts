import ghidra.util
import java.lang


class StatusListener(object):
    """
    StatusListener is a general purpose status listener
     responsible for displaying and/or recording status messages
    """









    def clearStatusText(self) -> None:
        """
        Clear the current status - same as setStatusText("")
         without being recorded
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def setStatusText(self, text: unicode) -> None:
        """
        Set the current status as type INFO
        @param text status text
        """
        ...

    @overload
    def setStatusText(self, text: unicode, type: ghidra.util.MessageType) -> None:
        """
        Set the current status as the specified type
        @param text status text
        @param type status type
        """
        ...

    @overload
    def setStatusText(self, text: unicode, type: ghidra.util.MessageType, alert: bool) -> None:
        """
        Set the current status as the specified type
        @param text status text
        @param type status type
        @param alert true to grab the user's attention
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def statusText(self) -> None: ...  # No getter available.

    @statusText.setter
    def statusText(self, value: unicode) -> None: ...
