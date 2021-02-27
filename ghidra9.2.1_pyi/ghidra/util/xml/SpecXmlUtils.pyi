import java.io
import java.lang
import org.xml.sax


class SpecXmlUtils(object):
    """
    Utilities for encoding and decoding XML datatypes for use in specification files that
     are validated by RelaxNG.  This currently includes the SLEIGH/Decompiler configuration files.
     I.e.
     		.ldef files
     		.pspec files
     		.cspec files
     		.sla files

      Philosophy here is to use and enforce datatype encodings from XML schemas
      to try to be as standard as possible and facilitate use of relax grammars etc.  But in decoding
      possibly be a little more open to deal with resources generated outside of our control.
    """





    def __init__(self): ...



    @staticmethod
    def decodeBoolean(val: unicode) -> bool: ...

    @staticmethod
    def decodeInt(intString: unicode) -> int: ...

    @staticmethod
    def decodeLong(longString: unicode) -> long: ...

    @staticmethod
    def encodeBoolean(val: bool) -> unicode: ...

    @staticmethod
    def encodeBooleanAttribute(buf: java.lang.StringBuilder, nm: unicode, val: bool) -> None: ...

    @staticmethod
    def encodeDoubleAttribute(buf: java.lang.StringBuilder, nm: unicode, val: float) -> None: ...

    @staticmethod
    def encodeSignedInteger(val: long) -> unicode: ...

    @staticmethod
    def encodeSignedIntegerAttribute(buf: java.lang.StringBuilder, nm: unicode, val: long) -> None: ...

    @staticmethod
    def encodeStringAttribute(buf: java.lang.StringBuilder, nm: unicode, val: unicode) -> None: ...

    @staticmethod
    def encodeUnsignedInteger(val: long) -> unicode: ...

    @staticmethod
    def encodeUnsignedIntegerAttribute(buf: java.lang.StringBuilder, nm: unicode, val: long) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getXmlHandler() -> org.xml.sax.ErrorHandler: ...

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

    @staticmethod
    def xmlEscape(buf: java.lang.StringBuilder, val: unicode) -> None: ...

    @staticmethod
    def xmlEscapeAttribute(buf: java.lang.StringBuilder, nm: unicode, val: unicode) -> None: ...

    @staticmethod
    def xmlEscapeWriter(writer: java.io.Writer, val: unicode) -> None: ...
