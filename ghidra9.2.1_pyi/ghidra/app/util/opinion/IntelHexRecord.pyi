from typing import List
import java.lang


class IntelHexRecord(object):
    DATA_RECORD_TYPE: int = 0
    END_OF_FILE_RECORD_TYPE: int = 1
    EXTENDED_LINEAR_ADDRESS_RECORD_TYPE: int = 4
    EXTENDED_SEGMENT_ADDRESS_RECORD_TYPE: int = 2
    MAX_RECORD_LENGTH: int = 255
    START_LINEAR_ADDRESS_RECORD_TYPE: int = 5
    START_SEGMENT_ADDRESS_RECORD: int = 3



    @overload
    def __init__(self, recordLength: int, loadOffset: int, recordType: int, data: List[int]):
        """
        Only use this constructor when writing...it computes the checksum for you (cheating)!
        @param recordLength
        @param loadOffset
        @param recordType
        @param data
        """
        ...

    @overload
    def __init__(self, recordLength: int, loadOffset: int, recordType: int, data: List[int], checksum: int):
        """
        Use this constructor when reading, so you know if the record's checksum is correct.
        @param recordLength
        @param loadOffset
        @param recordType
        @param data
        @param checksum
        """
        ...



    def equals(self, obj: object) -> bool: ...

    def format(self) -> unicode: ...

    def getActualChecksum(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getData(self) -> List[int]: ...

    def getDataString(self) -> unicode: ...

    def getLoadOffset(self) -> int: ...

    def getRecordLength(self) -> int: ...

    def getRecordType(self) -> int: ...

    def getReportedChecksum(self) -> int: ...

    def hashCode(self) -> int: ...

    def isReportedChecksumCorrect(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def actualChecksum(self) -> int: ...

    @property
    def data(self) -> List[int]: ...

    @property
    def dataString(self) -> unicode: ...

    @property
    def loadOffset(self) -> int: ...

    @property
    def recordLength(self) -> int: ...

    @property
    def recordType(self) -> int: ...

    @property
    def reportedChecksum(self) -> int: ...

    @property
    def reportedChecksumCorrect(self) -> bool: ...
