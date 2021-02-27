import ghidra.program.model.data
import java.lang


class DataTypeManagerOwner(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDataTypeManager(self) -> ghidra.program.model.data.DataTypeManager:
        """
        Gets the associated data type manager.
        @return the data type manager.
        """
        ...

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

    @property
    def dataTypeManager(self) -> ghidra.program.model.data.DataTypeManager: ...
