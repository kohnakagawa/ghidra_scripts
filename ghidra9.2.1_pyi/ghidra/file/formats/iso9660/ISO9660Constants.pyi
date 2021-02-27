import java.lang


class ISO9660Constants(object):
    APPLICATION_USED_LENGTH: int = 512
    ASSOCIATED_FILE_FLAG: int = 2
    BAD_TYPE: int = -2
    BOOT_SYSTEM_USE_LENGTH: int = 1977
    DATE_TIME_LENGTH_17: int = 17
    DATE_TIME_LENGTH_7: int = 7
    DIRECTORY_FLAG: int = 1
    EXTENDED_ATTRIBUTE_RECORD_INFO_FLAG: int = 3
    FILE_STRUCTURE_VERISON: int = 1
    HIDDEN_FILE_FLAG: int = 0
    IDENTIFIER_LENGTH_128: int = 128
    IDENTIFIER_LENGTH_32: int = 32
    IDENTIFIER_LENGTH_36: int = 36
    IDENTIFIER_LENGTH_37: int = 37
    IDENTIFIER_LENGTH_38: int = 38
    MAGIC_BYTES: List[int] = array('b', [67, 68, 48, 48, 49])
    MAGIC_STRING: unicode = u'CD001'
    MIN_ISO_LENGTH1: int = 34816
    MIN_ISO_LENGTH2: int = 36864
    MIN_ISO_LENGTH3: int = 38912
    NOT_FINAL_DIRECTORY_RECORD_FLAG: int = 5
    OWNER_GROUP_PERMISSIONS_FLAG: int = 4
    RESERVED_SIZE: int = 653
    SECTOR_LENGTH: int = 2048
    SIGNATURE_OFFSET1_0x8001: int = 32769
    SIGNATURE_OFFSET2_0x8801: int = 34817
    SIGNATURE_OFFSET3_0x9001: int = 36865
    UNUSED_SPACER_LEN_32: int = 32
    UNUSED_SPACER_LEN_512: int = 512
    VOLUME_DESC_BOOT_RECORD: int = 0
    VOLUME_DESC_PRIMARY_VOLUME_DESC: int = 1
    VOLUME_DESC_SET_TERMINATOR: int = -1
    VOLUME_DESC_SUPPL_VOLUME_DESC: int = 2
    VOLUME_PARTITION_DESC: int = 3



    def __init__(self): ...



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
