import java.lang


class GhidraURLWrappedContent(object):
    """
    GhidraURLWrappedContent provides controlled access to a Ghidra folder/file
     associated with a Ghidra URL.  It is important to note the issuance of this object does
     not guarantee existence of the requested resource.  Any object obtained via the getContent
     method must be released via the release method.  The following rules should be followed
     when using domain folder and files obtained.

     The getContent method may only be invoked once per consumer
     The content must be released when no longer in-use, however it should not be released
     until any derivative domain folders and files are no longer in use as well.
     A read-only or immutable domain object may remain open while the associated domain
     file/folder is released.

    """





    def __init__(self, c: ghidra.framework.protocol.ghidra.GhidraURLConnection): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getContent(self, consumer: object) -> object:
        """
        Get the domain folder or file associated with the Ghidra URL.
         The consumer is responsible for releasing the content object via the release method
         when it is no longer in use.
        @param consumer object which is responsible for releasing the content
        @return domain file or folder
        @throws IOException
        @throws NotFoundException if the Ghidra URL does no correspond to a folder or file
         within the Ghidra repository/project.
        @see #release(Object, Object)
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def release(self, content: object, consumer: object) -> None:
        """
        Indicates the content object previously obtained from this wrapper is
         no longer in-use and the underlying connection may be closed.  A read-only
         or immutable domain object may remain open and in-use after its associated
         domain folder/file has been released.
        @param content
        @param consumer
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
