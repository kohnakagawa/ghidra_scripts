import java.lang


class EntryDescriptorID(object):
    ENTRY_AFP_FILE_INFO: int = 13
    ENTRY_COMMENT: int = 4
    ENTRY_DATA_FORK: int = 1
    ENTRY_DIRECTORY_ID: int = 14
    ENTRY_FILE_DATE_INFO: int = 7
    ENTRY_FINDER_INFO: int = 8
    ENTRY_ICON_BW: int = 5
    ENTRY_ICON_COLOR: int = 6
    ENTRY_MAC_FILE_INFO: int = 9
    ENTRY_MSDOS_FILE_INFO: int = 11
    ENTRY_PRODOS_FILE_INFO: int = 10
    ENTRY_REAL_NAME: int = 3
    ENTRY_RESOURCE_FORK: int = 2
    ENTRY_SHORT_NAME: int = 12



    def __init__(self): ...



    @staticmethod
    def convertEntryIdToName(entryID: int) -> unicode: ...

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
