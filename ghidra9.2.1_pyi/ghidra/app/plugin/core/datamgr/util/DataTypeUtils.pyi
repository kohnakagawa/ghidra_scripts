from typing import List
import ghidra.app.services
import ghidra.program.model.data
import java.awt
import java.lang
import javax.swing


class DataTypeUtils(object):








    @staticmethod
    def copyToNamedBaseDataType(__a0: ghidra.program.model.data.DataType, __a1: ghidra.program.model.data.DataTypeManager) -> ghidra.program.model.data.DataType: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def getBaseDataType(__a0: ghidra.program.model.data.DataType) -> ghidra.program.model.data.DataType: ...

    @staticmethod
    def getBuiltInIcon(__a0: bool) -> javax.swing.Icon: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getClosedArchiveFolder(__a0: bool) -> javax.swing.Icon: ...

    @staticmethod
    def getClosedFolderIcon(__a0: bool) -> javax.swing.Icon: ...

    @staticmethod
    def getExactMatchingDataTypes(__a0: unicode, __a1: ghidra.app.services.DataTypeQueryService) -> List[object]: ...

    @staticmethod
    def getFavoriteIcon(__a0: bool) -> javax.swing.Icon: ...

    @staticmethod
    def getHighlightIcon(__a0: javax.swing.Icon) -> javax.swing.Icon: ...

    @staticmethod
    def getIconForDataType(__a0: ghidra.program.model.data.DataType, __a1: bool) -> javax.swing.Icon: ...

    @staticmethod
    def getNamedBaseDataType(__a0: ghidra.program.model.data.DataType) -> ghidra.program.model.data.DataType: ...

    @staticmethod
    def getOpenArchiveFolder(__a0: bool) -> javax.swing.Icon: ...

    @staticmethod
    def getOpenFolderIcon(__a0: bool) -> javax.swing.Icon: ...

    @staticmethod
    def getRootIcon(__a0: bool) -> javax.swing.Icon: ...

    @staticmethod
    def getStartsWithMatchingDataTypes(__a0: unicode, __a1: ghidra.app.services.DataTypeQueryService) -> List[object]: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def prepareSearchText(__a0: unicode) -> unicode: ...

    @staticmethod
    def showUnmodifiableArchiveErrorMessage(__a0: java.awt.Component, __a1: unicode, __a2: ghidra.program.model.data.DataTypeManager) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
