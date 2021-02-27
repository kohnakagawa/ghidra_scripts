import java.lang


class VTChangeManager(object):
    DOCR_VT_ASSOCIATION_ADDED: int = 1025
    DOCR_VT_ASSOCIATION_MARKUP_STATUS_CHANGED: int = 1027
    DOCR_VT_ASSOCIATION_REMOVED: int = 1026
    DOCR_VT_ASSOCIATION_STATUS_CHANGED: int = 1021
    DOCR_VT_MARKUP_ITEM_DESTINATION_CHANGED: int = 1031
    DOCR_VT_MARKUP_ITEM_STATUS_CHANGED: int = 1030
    DOCR_VT_MATCH_ADDED: int = 1022
    DOCR_VT_MATCH_DELETED: int = 1023
    DOCR_VT_MATCH_SET_ADDED: int = 1010
    DOCR_VT_MATCH_TAG_CHANGED: int = 1024
    DOCR_VT_TAG_ADDED: int = 1040
    DOCR_VT_TAG_REMOVED: int = 1041
    DOCR_VT_VOTE_COUNT_CHANGED: int = 1050







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setChanged(self, __a0: int, __a1: object, __a2: object) -> None: ...

    def setObjectChanged(self, __a0: int, __a1: object, __a2: object, __a3: object) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
