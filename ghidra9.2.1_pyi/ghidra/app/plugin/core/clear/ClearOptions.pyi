import java.lang


class ClearOptions(object):




    @overload
    def __init__(self): ...

    @overload
    def __init__(self, __a0: bool): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setClearAnalysisReferences(self, __a0: bool) -> None: ...

    def setClearBookmarks(self, __a0: bool) -> None: ...

    def setClearCode(self, __a0: bool) -> None: ...

    def setClearComments(self, __a0: bool) -> None: ...

    def setClearDefaultReferences(self, __a0: bool) -> None: ...

    def setClearEquates(self, __a0: bool) -> None: ...

    def setClearFunctions(self, __a0: bool) -> None: ...

    def setClearImportReferences(self, __a0: bool) -> None: ...

    def setClearProperties(self, __a0: bool) -> None: ...

    def setClearRegisters(self, __a0: bool) -> None: ...

    def setClearSymbols(self, __a0: bool) -> None: ...

    def setClearUserReferences(self, __a0: bool) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def clearAnalysisReferences(self) -> None: ...  # No getter available.

    @clearAnalysisReferences.setter
    def clearAnalysisReferences(self, value: bool) -> None: ...

    @property
    def clearBookmarks(self) -> None: ...  # No getter available.

    @clearBookmarks.setter
    def clearBookmarks(self, value: bool) -> None: ...

    @property
    def clearCode(self) -> None: ...  # No getter available.

    @clearCode.setter
    def clearCode(self, value: bool) -> None: ...

    @property
    def clearComments(self) -> None: ...  # No getter available.

    @clearComments.setter
    def clearComments(self, value: bool) -> None: ...

    @property
    def clearDefaultReferences(self) -> None: ...  # No getter available.

    @clearDefaultReferences.setter
    def clearDefaultReferences(self, value: bool) -> None: ...

    @property
    def clearEquates(self) -> None: ...  # No getter available.

    @clearEquates.setter
    def clearEquates(self, value: bool) -> None: ...

    @property
    def clearFunctions(self) -> None: ...  # No getter available.

    @clearFunctions.setter
    def clearFunctions(self, value: bool) -> None: ...

    @property
    def clearImportReferences(self) -> None: ...  # No getter available.

    @clearImportReferences.setter
    def clearImportReferences(self, value: bool) -> None: ...

    @property
    def clearProperties(self) -> None: ...  # No getter available.

    @clearProperties.setter
    def clearProperties(self, value: bool) -> None: ...

    @property
    def clearRegisters(self) -> None: ...  # No getter available.

    @clearRegisters.setter
    def clearRegisters(self, value: bool) -> None: ...

    @property
    def clearSymbols(self) -> None: ...  # No getter available.

    @clearSymbols.setter
    def clearSymbols(self, value: bool) -> None: ...

    @property
    def clearUserReferences(self) -> None: ...  # No getter available.

    @clearUserReferences.setter
    def clearUserReferences(self, value: bool) -> None: ...
