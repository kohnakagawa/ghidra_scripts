import java.io
import java.lang


class DerivedFileProducer(object):
    """
    Used by FileSystemService#getDerivedFile(FSRL, String, DerivedFileProducer, TaskMonitor)
     to produce a derived file from a source file.

     The InputStream returned from the method will be closed by the caller.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def produceDerivedStream(self, srcFile: java.io.File) -> java.io.InputStream:
        """
        Callback method intended to be implemented by the caller to
         {@link FileSystemService#getDerivedFile(FSRL, String, DerivedFileProducer, TaskMonitor)}.
         <p>
         The implementation needs to return an {@link InputStream} that contains the bytes
         of the derived file.
         <p>
        @param srcFile {@link File} location of the source file (usually in the file cache)
        @return a new {@link InputStream} that will produce all the bytes of the derived file.
        @throws IOException if there is a problem while producing the InputStream.
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
