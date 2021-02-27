from typing import List
import ghidra.file.formats.iso9660
import ghidra.program.model.data
import java.lang


class ISO9660BootRecordVolumeDescriptor(ghidra.file.formats.iso9660.ISO9660BaseVolume):




    def __init__(self, __a0: ghidra.app.util.bin.BinaryReader): ...



    def equals(self, __a0: object) -> bool: ...

    def getBootIdentifier(self) -> List[int]: ...

    def getBootSystemIdentifier(self) -> List[int]: ...

    def getBootSystemUse(self) -> List[int]: ...

    def getClass(self) -> java.lang.Class: ...

    def getIdentifier(self) -> List[int]: ...

    def getTypeCode(self) -> int: ...

    def getTypeCodeString(self) -> unicode: ...

    def getVersion(self) -> int: ...

    def getVolumeIndex(self) -> long: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def bootIdentifier(self) -> List[int]: ...

    @property
    def bootSystemIdentifier(self) -> List[int]: ...

    @property
    def bootSystemUse(self) -> List[int]: ...