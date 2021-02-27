from typing import List
import ghidra.program.model.data
import java.lang


class CharsetInfo(object):
    """
    Additional information about Charset that
     Ghidra needs to be able to create Ghidra string datatype instances.

     See charset_info.xml to specify a custom charset.
    """

    USASCII: unicode = u'US-ASCII'
    UTF16: unicode = u'UTF-16'
    UTF32: unicode = u'UTF-32'
    UTF8: unicode = u'UTF-8'







    def equals(self, __a0: object) -> bool: ...

    def getCharsetCharSize(self, charsetName: unicode) -> int:
        """
        Returns the number of bytes that the specified charset needs to specify a
         character.
        @param charsetName charset name
        @return number of bytes in a character, ie. 1, 2, 4, etc, defaults to 1
                 if charset is unknown or not specified in config file.
        """
        ...

    def getCharsetNames(self) -> List[unicode]:
        """
        Returns an array list of the currently configured charsets.
        @return String[] of current configured charsets.
        """
        ...

    def getCharsetNamesWithCharSize(self, size: int) -> List[unicode]:
        """
        Returns list of {@link Charset}s that encode with the number of bytes specified.
        @param size the number of bytes for the {@link Charset} encoding.
        @return Charsets that encode one byte characters.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getInstance() -> ghidra.program.model.data.CharsetInfo:
        """
        Get the global singleton instance of this {@link CharsetInfo}.
        @return global singleton instance
        """
        ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isBOMCharset(charsetName: unicode) -> bool:
        """
        @param charsetName name of charset
        @return true if the supported multi-byte charset does not specify LE or
                 BE
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def reinitializeWithUserDefinedCharsets() -> None:
        """
        Reinitialize registered Charsets and include user defined Charsets
         specified in charset_info.xml.
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
    def charsetNames(self) -> List[unicode]: ...
