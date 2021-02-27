import ghidra.app.decompiler
import java.io
import java.lang


class DecompilerDisposer(object):








    @overload
    @staticmethod
    def dispose(decompiler: ghidra.app.decompiler.DecompInterface) -> None:
        """
        Calls dispose in the given decompiler from a background thread.
         <p>
         Note:<br>
         A class to handle the rare case where the {@link DecompInterface}'s
         synchronized methods are blocking
         while a decompile operation has died and maintained the lock.  In that scenario, calling
         dispose on this class will eventually try to enter a synchronized method that will
         remain blocked forever.
         <p>
         I examined the uses of dispose() on the {@link DecompInterface} and
         determined that calling dispose() is a
         final operation, which means that you don't have to wait.  Further, after calling
         dispose() on this class, you should no longer use it.
        """
        ...

    @overload
    @staticmethod
    def dispose(process: java.lang.Process, ouputStream: java.io.OutputStream, inputStream: java.io.InputStream) -> None:
        """
        Disposes the given Process and related streams from a background thread.  This is necessary
         due to a low-probability deadlock that occurs in the JVM.
        @param process The process to destroy.
        @param ouputStream The output stream to close
        @param inputStream The input stream to close
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
