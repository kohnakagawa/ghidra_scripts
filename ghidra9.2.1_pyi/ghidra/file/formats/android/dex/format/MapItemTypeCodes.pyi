import java.lang


class MapItemTypeCodes(object):
    TYPE_ANNOTATIONS_DIRECTORY_ITEM: int = 8198
    TYPE_ANNOTATION_ITEM: int = 8196
    TYPE_ANNOTATION_SET_ITEM: int = 4099
    TYPE_ANNOTATION_SET_REF_LIST: int = 4098
    TYPE_CLASS_DATA_ITEM: int = 8192
    TYPE_CLASS_DEF_ITEM: int = 6
    TYPE_CODE_ITEM: int = 8193
    TYPE_DEBUG_INFO_ITEM: int = 8195
    TYPE_ENCODED_ARRAY_ITEM: int = 8197
    TYPE_FIELD_ID_ITEM: int = 4
    TYPE_HEADER_ITEM: int = 0
    TYPE_MAP_LIST: int = 4096
    TYPE_METHOD_ID_ITEM: int = 5
    TYPE_PROTO_ID_ITEM: int = 3
    TYPE_STRING_DATA_ITEM: int = 8194
    TYPE_STRING_ID_ITEM: int = 1
    TYPE_TYPE_ID_ITEM: int = 2
    TYPE_TYPE_LIST: int = 4097



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def toString(__a0: int) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
