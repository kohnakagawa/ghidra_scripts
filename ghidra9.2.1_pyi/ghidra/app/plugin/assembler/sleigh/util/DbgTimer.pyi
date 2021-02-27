from typing import List
import ghidra.app.plugin.assembler.sleigh.util.DbgTimer
import java.io
import java.lang
import java.util


class DbgTimer(java.io.PrintStream):
    """
    A debugging, timing, and diagnostic tool

     TODO: I should probably remove this and rely on the Msg.trace() method, or at the very least,
     refactor this to use that.
    """

    ACTIVE: ghidra.app.plugin.assembler.sleigh.util.DbgTimer = ghidra.app.plugin.assembler.sleigh.util.DbgTimer@45b9aca5
    INACTIVE: ghidra.app.plugin.assembler.sleigh.util.DbgTimer = ghidra.app.plugin.assembler.sleigh.util.DbgTimer$2@4f4196f2




    class DbgCtx(object, java.lang.AutoCloseable):








        def close(self) -> None: ...

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






    class TabbingOutputStream(java.io.OutputStream):








        def close(self) -> None: ...

        def equals(self, __a0: object) -> bool: ...

        def flush(self) -> None: ...

        def getClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        @staticmethod
        def nullOutputStream() -> java.io.OutputStream: ...

        def toString(self) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...

        @overload
        def write(self, __a0: int) -> None: ...

        @overload
        def write(self, __a0: List[int]) -> None: ...

        @overload
        def write(self, __a0: List[int], __a1: int, __a2: int) -> None: ...



    @overload
    def __init__(self):
        """
        Create a new debugging timer, wrapping standard out
        """
        ...

    @overload
    def __init__(self, out: java.io.OutputStream):
        """
        Create a new debugging timer, wrapping the given output stream
        @param out the stream
        """
        ...



    @overload
    def append(self, __a0: int) -> java.lang.Appendable: ...

    @overload
    def append(self, __a0: java.lang.CharSequence) -> java.lang.Appendable: ...

    @overload
    def append(self, __a0: java.lang.CharSequence, __a1: int, __a2: int) -> java.lang.Appendable: ...

    def checkError(self) -> bool: ...

    def close(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def flush(self) -> None: ...

    @overload
    def format(self, __a0: unicode, __a1: List[object]) -> java.io.PrintStream: ...

    @overload
    def format(self, __a0: java.util.Locale, __a1: unicode, __a2: List[object]) -> java.io.PrintStream: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def nullOutputStream() -> java.io.OutputStream: ...

    @overload
    def print(self, __a0: long) -> None: ...

    @overload
    def print(self, __a0: int) -> None: ...

    @overload
    def print(self, __a0: int) -> None: ...

    @overload
    def print(self, __a0: float) -> None: ...

    @overload
    def print(self, __a0: float) -> None: ...

    @overload
    def print(self, __a0: bool) -> None: ...

    @overload
    def print(self, __a0: unicode) -> None: ...

    @overload
    def print(self, __a0: List[int]) -> None: ...

    @overload
    def print(self, __a0: object) -> None: ...

    @overload
    def printf(self, __a0: unicode, __a1: List[object]) -> java.io.PrintStream: ...

    @overload
    def printf(self, __a0: java.util.Locale, __a1: unicode, __a2: List[object]) -> java.io.PrintStream: ...

    @overload
    def println(self) -> None: ...

    @overload
    def println(self, __a0: long) -> None: ...

    @overload
    def println(self, __a0: int) -> None: ...

    @overload
    def println(self, __a0: int) -> None: ...

    @overload
    def println(self, __a0: float) -> None: ...

    @overload
    def println(self, __a0: float) -> None: ...

    @overload
    def println(self, __a0: bool) -> None: ...

    @overload
    def println(self, __a0: unicode) -> None: ...

    @overload
    def println(self, __a0: List[int]) -> None: ...

    @overload
    def println(self, __a0: object) -> None: ...

    def resetOutputStream(self, s: ghidra.app.plugin.assembler.sleigh.util.DbgTimer.TabbingOutputStream) -> ghidra.app.plugin.assembler.sleigh.util.DbgTimer.TabbingOutputStream:
        """
        Put the original tabbing stream back
        @see #setOutputStream(OutputStream)
        @param s the original wrapped stream
        @return the replacement stream, wrapped in a tabbing stream
        """
        ...

    def setOutputStream(self, s: java.io.OutputStream) -> ghidra.app.plugin.assembler.sleigh.util.DbgTimer.TabbingOutputStream:
        """
        Replace the wrapped output stream (usually temporarily)
        @see #resetOutputStream(TabbingOutputStream)
        @param s the replacement stream
        @return the original stream, wrapped in a tabbing stream
        """
        ...

    def start(self, message: object) -> ghidra.app.plugin.assembler.sleigh.util.DbgTimer.DbgCtx:
        """
        Start a new, possibly long-running, task
        @param message the message to print when the task begins
        @return a context to close when the task ends

         This is meant to be used idiomatically, as in a try-with-resources block:
         <pre>
         {@code
         try (DbgCtx dc = dbg.start("Twiddling the frobs:")) {
             // do some classy twiddling
         } // this will automatically print done and the time elapsed within the try block
         }
         </pre>

         This idiom is preferred because the task will be stopped even if an error occurs, if the
         method returns from within the block, etc.
        """
        ...

    def stop(self) -> None:
        """
        Stop the current task

         This will print done and the elapsed time since the start of the task. The "current task" is
         determined from the stack.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @overload
    def write(self, __a0: int) -> None: ...

    @overload
    def write(self, __a0: List[int]) -> None: ...

    @overload
    def write(self, __a0: List[int], __a1: int, __a2: int) -> None: ...

    @property
    def outputStream(self) -> None: ...  # No getter available.

    @outputStream.setter
    def outputStream(self, value: java.io.OutputStream) -> None: ...
