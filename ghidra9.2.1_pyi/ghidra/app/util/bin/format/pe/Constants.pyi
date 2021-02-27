import java.lang


class Constants(object):
    """
    Constants used in the data structures of the PE.
    """

    IMAGE_ARCHIVE_END: unicode = u'`\n'
    IMAGE_ARCHIVE_LINKER_MEMBER: unicode = u'/               '
    IMAGE_ARCHIVE_LONGNAMES_MEMBER: unicode = u'//              '
    IMAGE_ARCHIVE_PAD: unicode = u'\n'
    IMAGE_ARCHIVE_START: unicode = u'!<arch>\n'
    IMAGE_ARCHIVE_START_SIZE: int = 8
    IMAGE_NT_OPTIONAL_HDR32_MAGIC: int = 267
    IMAGE_NT_OPTIONAL_HDR64_MAGIC: int = 523
    IMAGE_NT_SIGNATURE: int = 17744
    IMAGE_ORDINAL_FLAG32: long = 0x80000000L
    IMAGE_ORDINAL_FLAG64: long = -0x8000000000000000L
    IMAGE_OS2_SIGNATURE: int = 17742
    IMAGE_OS2_SIGNATURE_LE: int = 17740
    IMAGE_ROM_OPTIONAL_HDR_MAGIC: int = 263
    IMAGE_SIZEOF_NT_OPTIONAL32_HEADER: int = 224
    IMAGE_SIZEOF_NT_OPTIONAL64_HEADER: int = 240
    IMAGE_SIZEOF_ROM_OPTIONAL_HEADER: int = 56
    IMAGE_SIZEOF_STD_OPTIONAL_HEADER: int = 28
    IMAGE_VXD_SIGNATURE: int = 17740







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
