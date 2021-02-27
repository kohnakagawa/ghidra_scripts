import java.io
import java.lang


class DerivedFilePushProducer(object):
    """
    Used by FileSystemService#getDerivedFilePush(FSRL, String, DerivedFilePushProducer, TaskMonitor)
     to produce a derived file from a source file.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def push(self, os: java.io.OutputStream) -> None:
        """
        Callback method intended to be implemented by the caller to
         {@link FileSystemService#getDerivedFilePush(FSRL, String, DerivedFilePushProducer, TaskMonitor)}.
         <p>
         The implementation needs to write bytes to the supplied {@link OutputStream}.
         <p>
        @param os {@link OutputStream} that the implementor should write the bytes to.  Do
         not close the stream when done.
        @throws IOException if there is a problem while writing to the OutputStream.
        @throws CancelledException if the user canceled.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
