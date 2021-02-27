import ghidra.app.util.importer
import java.lang


class MessageLog(object):
    """
    A simple class to handle logging messages and exceptions.  A maximum message count size
     constraint can be set to clip messages after a certain number, but still keep incrementing
     a running total.

     In addition to logging messages, clients can also set a status message.  This message may
     later used as the primary error message when reporting to the user.
    """





    def __init__(self): ...



    def appendException(self, t: java.lang.Throwable) -> None:
        """
        Appends the exception to the log
        @param t the exception to append to the log
        """
        ...

    @overload
    def appendMsg(self, message: unicode) -> None:
        """
        Appends the message to the log
        @param message the message
        """
        ...

    @overload
    def appendMsg(self, lineNum: int, message: unicode) -> None:
        """
        Appends the message and line number to the log
        @param lineNum the line number that generated the message
        @param message the message
        """
        ...

    @overload
    def appendMsg(self, originator: unicode, message: unicode) -> None:
        """
        Appends the message to the log
        @param originator the originator of the message
        @param message the message
        """
        ...

    def clear(self) -> None:
        """
        Clears all messages from this log and resets the count
        """
        ...

    def clearStatus(self) -> None:
        """
        Clear status message
        """
        ...

    def copyFrom(self, log: ghidra.app.util.importer.MessageLog) -> None:
        """
        Copies the contents of one message log into this one
        @param log the log to copy from
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def error(self, originator: unicode, message: unicode) -> None:
        """
        Readable method for appending error messages to the log.

         <p>Currently does nothing different than {@link #appendMsg(String, String)}.
        @param originator the originator of the message
        @param message the message
        @deprecated use {@link #appendMsg(String)}
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getStatus(self) -> unicode:
        """
        Returns a stored status message
        @return stored status message
        """
        ...

    def hasMessages(self) -> bool:
        """
        Returns true if this log has messages
        @return true if this log has messages
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setStatus(self, status: unicode) -> None:
        """
        Stores a status message that can be used elsewhere (i.e., populate warning dialogs)
        @param status the status message
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def write(self, owner: java.lang.Class, messageHeader: unicode) -> None:
        """
        Writes this log's contents to the application log
        @param owner the owning class whose name will appear in the log message
        @param messageHeader the message header that will appear before the log messages
        """
        ...

    @property
    def status(self) -> unicode: ...

    @status.setter
    def status(self, value: unicode) -> None: ...
