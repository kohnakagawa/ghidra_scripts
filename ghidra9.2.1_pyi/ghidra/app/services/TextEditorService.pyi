import java.io
import java.lang


class TextEditorService(object):








    def edit(self, name: unicode, inputStream: java.io.InputStream) -> None:
        """
        Shows an text editor component with the contents of the specified {@link InputStream}.
         <p>
        @param name String name of file
        @param inputStream {@link InputStream} with content that should be displayed in the
         edit window.  Stream closed by this service.
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
