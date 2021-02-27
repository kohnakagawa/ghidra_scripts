import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.util
import java.lang


class ChangeManagerAdapter(object, ghidra.program.util.ChangeManager):
    """
    Empty implementation for a ChangeManager.
    """

    DOCR_ADDRESS_SET_PROPERTY_MAP_ADDED: int = 166
    DOCR_ADDRESS_SET_PROPERTY_MAP_CHANGED: int = 168
    DOCR_ADDRESS_SET_PROPERTY_MAP_REMOVED: int = 167
    DOCR_BOOKMARK_ADDED: int = 122
    DOCR_BOOKMARK_CHANGED: int = 124
    DOCR_BOOKMARK_REMOVED: int = 123
    DOCR_BOOKMARK_TYPE_ADDED: int = 120
    DOCR_BOOKMARK_TYPE_REMOVED: int = 121
    DOCR_CATEGORY_ADDED: int = 100
    DOCR_CATEGORY_MOVED: int = 103
    DOCR_CATEGORY_REMOVED: int = 101
    DOCR_CATEGORY_RENAMED: int = 102
    DOCR_CODE_ADDED: int = 30
    DOCR_CODE_MOVED: int = 32
    DOCR_CODE_REMOVED: int = 31
    DOCR_CODE_REPLACED: int = 35
    DOCR_CODE_UNIT_PROPERTY_ALL_REMOVED: int = 37
    DOCR_CODE_UNIT_PROPERTY_CHANGED: int = 36
    DOCR_CODE_UNIT_PROPERTY_RANGE_REMOVED: int = 38
    DOCR_CODE_UNIT_USER_DATA_CHANGED: int = 200
    DOCR_COMPOSITE_ADDED: int = 33
    DOCR_COMPOSITE_REMOVED: int = 34
    DOCR_CUSTOM_FORMAT_ADDED: int = 164
    DOCR_CUSTOM_FORMAT_REMOVED: int = 165
    DOCR_DATA_TYPE_ADDED: int = 104
    DOCR_DATA_TYPE_CHANGED: int = 108
    DOCR_DATA_TYPE_MOVED: int = 107
    DOCR_DATA_TYPE_REMOVED: int = 105
    DOCR_DATA_TYPE_RENAMED: int = 106
    DOCR_DATA_TYPE_REPLACED: int = 110
    DOCR_DATA_TYPE_SETTING_CHANGED: int = 109
    DOCR_DOCUMENT_CHANGED: int = 80
    DOCR_EOL_COMMENT_CHANGED: int = 90
    DOCR_EQUATE_ADDED: int = 70
    DOCR_EQUATE_REFERENCE_ADDED: int = 72
    DOCR_EQUATE_REFERENCE_REMOVED: int = 73
    DOCR_EQUATE_REMOVED: int = 71
    DOCR_EQUATE_RENAMED: int = 74
    DOCR_EXTERNAL_ENTRY_POINT_ADDED: int = 47
    DOCR_EXTERNAL_ENTRY_POINT_REMOVED: int = 48
    DOCR_EXTERNAL_NAME_ADDED: int = 66
    DOCR_EXTERNAL_NAME_CHANGED: int = 68
    DOCR_EXTERNAL_NAME_REMOVED: int = 67
    DOCR_EXTERNAL_PATH_CHANGED: int = 65
    DOCR_EXTERNAL_REFERENCE_ADDED: int = 160
    DOCR_EXTERNAL_REFERENCE_REMOVED: int = 161
    DOCR_FALLTHROUGH_CHANGED: int = 162
    DOCR_FLOWOVERRIDE_CHANGED: int = 163
    DOCR_FRAGMENT_MOVED: int = 87
    DOCR_FUNCTION_ADDED: int = 150
    DOCR_FUNCTION_BODY_CHANGED: int = 155
    DOCR_FUNCTION_CHANGED: int = 152
    DOCR_FUNCTION_REMOVED: int = 151
    DOCR_FUNCTION_TAG_CHANGED: int = 147
    DOCR_FUNCTION_TAG_CREATED: int = 148
    DOCR_FUNCTION_TAG_DELETED: int = 149
    DOCR_GROUP_ADDED: int = 81
    DOCR_GROUP_ALIAS_CHANGED: int = 85
    DOCR_GROUP_COMMENT_CHANGED: int = 84
    DOCR_GROUP_REMOVED: int = 82
    DOCR_GROUP_RENAMED: int = 83
    DOCR_GROUP_REPARENTED: int = 88
    DOCR_IMAGE_BASE_CHANGED: int = 27
    DOCR_INT_ADDRESS_SET_PROPERTY_MAP_ADDED: int = 170
    DOCR_INT_ADDRESS_SET_PROPERTY_MAP_CHANGED: int = 172
    DOCR_INT_ADDRESS_SET_PROPERTY_MAP_REMOVED: int = 171
    DOCR_LANGUAGE_CHANGED: int = 130
    DOCR_MEMORY_BLOCKS_JOINED: int = 25
    DOCR_MEMORY_BLOCK_ADDED: int = 20
    DOCR_MEMORY_BLOCK_CHANGED: int = 22
    DOCR_MEMORY_BLOCK_MOVED: int = 23
    DOCR_MEMORY_BLOCK_REMOVED: int = 21
    DOCR_MEMORY_BLOCK_SPLIT: int = 24
    DOCR_MEMORY_BYTES_CHANGED: int = 26
    DOCR_MEM_REFERENCE_ADDED: int = 60
    DOCR_MEM_REFERENCE_REMOVED: int = 61
    DOCR_MEM_REF_PRIMARY_REMOVED: int = 64
    DOCR_MEM_REF_PRIMARY_SET: int = 63
    DOCR_MEM_REF_TYPE_CHANGED: int = 62
    DOCR_MODULE_REORDERED: int = 86
    DOCR_OBJECT_CREATED: int = 132
    DOCR_PLATE_COMMENT_CHANGED: int = 95
    DOCR_POST_COMMENT_CHANGED: int = 92
    DOCR_PRE_COMMENT_CHANGED: int = 91
    DOCR_REGISTER_VALUES_CHANGED: int = 131
    DOCR_REPEATABLE_COMMENT_ADDED: int = 94
    DOCR_REPEATABLE_COMMENT_CHANGED: int = 96
    DOCR_REPEATABLE_COMMENT_CREATED: int = 93
    DOCR_REPEATABLE_COMMENT_DELETED: int = 98
    DOCR_REPEATABLE_COMMENT_REMOVED: int = 97
    DOCR_SOURCE_ARCHIVE_ADDED: int = 111
    DOCR_SOURCE_ARCHIVE_CHANGED: int = 112
    DOCR_SYMBOL_ADDED: int = 40
    DOCR_SYMBOL_ADDRESS_CHANGED: int = 53
    DOCR_SYMBOL_ANCHORED_FLAG_CHANGED: int = 43
    DOCR_SYMBOL_ASSOCIATION_ADDED: int = 50
    DOCR_SYMBOL_ASSOCIATION_REMOVED: int = 51
    DOCR_SYMBOL_DATA_CHANGED: int = 52
    DOCR_SYMBOL_REMOVED: int = 41
    DOCR_SYMBOL_RENAMED: int = 46
    DOCR_SYMBOL_SCOPE_CHANGED: int = 49
    DOCR_SYMBOL_SET_AS_PRIMARY: int = 45
    DOCR_SYMBOL_SOURCE_CHANGED: int = 42
    DOCR_TAG_ADDED_TO_FUNCTION: int = 156
    DOCR_TAG_REMOVED_FROM_FUNCTION: int = 157
    DOCR_TREE_CREATED: int = 141
    DOCR_TREE_REMOVED: int = 142
    DOCR_TREE_RENAMED: int = 143
    DOCR_TREE_RESTORED: int = 140
    DOCR_USER_DATA_CHANGED: int = 201
    DOCR_VARIABLE_REFERENCE_ADDED: int = 153
    DOCR_VARIABLE_REFERENCE_REMOVED: int = 154
    FUNCTION_CHANGED_CALL_FIXUP: int = 4
    FUNCTION_CHANGED_INLINE: int = 2
    FUNCTION_CHANGED_NORETURN: int = 3
    FUNCTION_CHANGED_PARAMETERS: int = 6
    FUNCTION_CHANGED_PURGE: int = 1
    FUNCTION_CHANGED_RETURN: int = 5
    FUNCTION_CHANGED_THUNK: int = 7



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def setChanged(self, type: int, oldValue: object, newValue: object) -> None: ...

    @overload
    def setChanged(self, type: int, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address, oldValue: object, newValue: object) -> None: ...

    @overload
    def setObjChanged(self, type: int, affectedObj: object, oldValue: object, newValue: object) -> None: ...

    @overload
    def setObjChanged(self, type: int, subType: int, affectedObj: object, oldValue: object, newValue: object) -> None: ...

    @overload
    def setObjChanged(self, type: int, addr: ghidra.program.model.address.Address, affectedObj: object, oldValue: object, newValue: object) -> None: ...

    @overload
    def setObjChanged(self, type: int, addrSet: ghidra.program.model.address.AddressSetView, affectedObj: object, oldValue: object, newValue: object) -> None: ...

    @overload
    def setObjChanged(self, type: int, subType: int, addr: ghidra.program.model.address.Address, affectedObj: object, oldValue: object, newValue: object) -> None: ...

    def setPropertyChanged(self, propertyName: unicode, codeUnitAddr: ghidra.program.model.address.Address, oldValue: object, newValue: object) -> None: ...

    def setPropertyRangeRemoved(self, propertyName: unicode, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> None: ...

    def setRegisterValuesChanged(self, register: ghidra.program.model.lang.Register, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
