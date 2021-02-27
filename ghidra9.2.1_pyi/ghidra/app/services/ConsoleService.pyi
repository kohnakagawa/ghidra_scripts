import java.io
import java.lang


class ConsoleService(object):
    """
    Generic console interface allowing any plugin to print
     messages to console window.
    """









    def addErrorMessage(self, originator: unicode, message: unicode) -> None:
        """
        Appends an error message to the console text area.
         The message should be rendered is such a way as to denote
         that it is an error. For example, display in "red".
        @param originator a descriptive name of the message creator
        @param message the message to appear in the console
        """
        ...

    def addException(self, originator: unicode, exc: java.lang.Exception) -> None:
        """
        Appends an exception to the console text area.
        @param originator a descriptive name of the message creator
        @param exc the exception
        """
        ...

    def addMessage(self, originator: unicode, message: unicode) -> None:
        """
        Appends message to the console text area.

         For example:
            "originator&gt; message"
        @param originator a descriptive name of the message creator
        @param message the message to appear in the console
        """
        ...

    def clearMessages(self) -> None:
        """
        Clears all messages from the console.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getStdErr(self) -> java.io.PrintWriter:
        """
        Returns a print writer object to use as standard error.
        @return a print writer object to use as standard error
        """
        ...

    def getStdOut(self) -> java.io.PrintWriter:
        """
        Returns a print writer object to use as standard output.
        @return a print writer object to use as standard output
        """
        ...

    def getText(self, offset: int, length: int) -> unicode:
        """
        Fetches the text contained within the given portion
         of the console.

         Please note:
         Support for this method is optional
         based on the underlying console
         implementation. If this method cannot be supported,
         please throw {@link UnsupportedOperationException}.
        @param offset the offset into the console representing the desired start of the text &gt;= 0
        @param length the length of the desired string &gt;= 0
        @return the text, in a String of length &gt;= 0
        @throws UnsupportedOperationException
        """
        ...

    def getTextLength(self) -> int:
        """
        Returns number of characters of currently
         in the console.
         If the console is cleared, this number is reset.

         Please note:
         Support for this method is optional
         based on the underlying console
         implementation. If this method cannot be supported,
         please throw {@link UnsupportedOperationException}.
        @return number of characters &gt;= 0
        @throws UnsupportedOperationException
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def print(self, msg: unicode) -> None:
        """
        Prints the message into the console.
        @param msg the messages to print into the console
        """
        ...

    def printError(self, errmsg: unicode) -> None:
        """
        Prints the error message into the console.
         It will be displayed in red.
        @param errmsg the error message to print into the console
        """
        ...

    def println(self, msg: unicode) -> None:
        """
        Prints the messages into the console followed by a line feed.
        @param msg the message to print into the console
        """
        ...

    def printlnError(self, errmsg: unicode) -> None:
        """
        Prints the error message into the console followed by a line feed.
         It will be displayed in red.
        @param errmsg the error message to print into the console
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
    def stdErr(self) -> java.io.PrintWriter: ...

    @property
    def stdOut(self) -> java.io.PrintWriter: ...

    @property
    def textLength(self) -> int: ...
