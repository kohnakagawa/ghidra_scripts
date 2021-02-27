import java.lang


class DataTypeArchiveChangeManager(object):
    """
    Interface to define event types and the method to generate an
     event within Program.
    """

    DOCR_CATEGORY_ADDED: int = 100
    DOCR_CATEGORY_MOVED: int = 103
    DOCR_CATEGORY_REMOVED: int = 101
    DOCR_CATEGORY_RENAMED: int = 102
    DOCR_CUSTOM_FORMAT_ADDED: int = 163
    DOCR_CUSTOM_FORMAT_REMOVED: int = 164
    DOCR_DATA_TYPE_ADDED: int = 104
    DOCR_DATA_TYPE_CHANGED: int = 108
    DOCR_DATA_TYPE_MOVED: int = 107
    DOCR_DATA_TYPE_REMOVED: int = 105
    DOCR_DATA_TYPE_RENAMED: int = 106
    DOCR_DATA_TYPE_REPLACED: int = 110
    DOCR_DATA_TYPE_SETTING_CHANGED: int = 109







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setChanged(self, type: int, oldValue: object, newValue: object) -> None:
        """
        Mark the state of a Data Type Archive as having changed and generate
         the event of the specified type.  Any or all parameters may be null.
        @param type event type
        @param oldValue original value or an Object that is related to
         the event
        @param newValue new value or an Object that is related to the
         the event
        """
        ...

    def setObjChanged(self, type: int, affectedObj: object, oldValue: object, newValue: object) -> None:
        """
        Mark the state of a Data Type Archive as having changed and generate
         the event of the specified type.  Any or all parameters may be null.
        @param type event type
        @param affectedObj object that is the subject of the event
        @param oldValue original value or an Object that is related to
         the event
        @param newValue new value or an Object that is related to the
         the event
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
