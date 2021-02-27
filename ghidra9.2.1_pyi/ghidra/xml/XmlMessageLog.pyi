import ghidra.app.util.importer
import ghidra.xml
import java.lang


class XmlMessageLog(ghidra.app.util.importer.MessageLog):
    """
    A sub-class of MessageLog to handle appending messages from the XML parser.
    """





    def __init__(self):
        """
        Constructs a new XML message log.
        """
        ...



    def appendException(self, t: java.lang.Throwable) -> None:
        """
        Appends the exception to the log
        @param t the exception to append to the log
        """
        ...

    @overload
    def appendMsg(self, msg: unicode) -> None:
        """
        @see ghidra.app.util.importer.MessageLog#appendMsg(java.lang.String)
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

    def setParser(self, parser: ghidra.xml.XmlPullParser) -> None:
        """
        Sets the XML parser.
        @param parser the XML parser
        """
        ...

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
    def parser(self) -> None: ...  # No getter available.

    @parser.setter
    def parser(self, value: ghidra.xml.XmlPullParser) -> None: ...
