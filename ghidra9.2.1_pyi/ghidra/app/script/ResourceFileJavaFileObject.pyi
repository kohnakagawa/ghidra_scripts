import generic.jar
import java.io
import java.lang
import java.net
import javax.lang.model.element
import javax.tools
import javax.tools.JavaFileObject


class ResourceFileJavaFileObject(object, javax.tools.JavaFileObject):
    """
    A JavaFileObject that works with Ghidra's ResourceFileJavaFileManager.

     This class is used to dynamically compile Ghidra scripts.
    """





    def __init__(self, sourceRoot: generic.jar.ResourceFile, file: generic.jar.ResourceFile, kind: javax.tools.JavaFileObject.Kind):
        """
        Represents a {@link ResourceFile} for a {@link JavaCompiler} via a {@link ResourceFileJavaFileManager}
        @param sourceRoot the root source directory
        @param file the file
        @param kind the kind
        """
        ...



    def delete(self) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getAccessLevel(self) -> javax.lang.model.element.Modifier: ...

    def getCharContent(self, ignoreEncodingErrors: bool) -> java.lang.CharSequence: ...

    def getClass(self) -> java.lang.Class: ...

    def getFile(self) -> generic.jar.ResourceFile:
        """
        @return the {@link ResourceFile} this object represents
        """
        ...

    def getKind(self) -> javax.tools.JavaFileObject.Kind: ...

    def getLastModified(self) -> long: ...

    def getName(self) -> unicode: ...

    def getNestingKind(self) -> javax.lang.model.element.NestingKind: ...

    def hashCode(self) -> int: ...

    def isNameCompatible(self, compatibleName: unicode, testKind: javax.tools.JavaFileObject.Kind) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def openInputStream(self) -> java.io.InputStream: ...

    def openOutputStream(self) -> java.io.OutputStream: ...

    def openReader(self, ignoreEncodingErrors: bool) -> java.io.Reader: ...

    def openWriter(self) -> java.io.Writer: ...

    def toString(self) -> unicode: ...

    def toUri(self) -> java.net.URI: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def accessLevel(self) -> javax.lang.model.element.Modifier: ...

    @property
    def file(self) -> generic.jar.ResourceFile: ...

    @property
    def kind(self) -> javax.tools.JavaFileObject.Kind: ...

    @property
    def lastModified(self) -> long: ...

    @property
    def name(self) -> unicode: ...

    @property
    def nestingKind(self) -> javax.lang.model.element.NestingKind: ...
