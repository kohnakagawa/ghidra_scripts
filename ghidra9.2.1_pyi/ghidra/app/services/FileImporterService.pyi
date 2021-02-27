from typing import List
import ghidra.framework.model
import java.io
import java.lang


class FileImporterService(object):
    """
    Service for importing files into Ghidra.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def importFile(self, folder: ghidra.framework.model.DomainFolder, file: java.io.File) -> None:
        """
        Imports the given file into the specified Ghidra project folder.
        @param folder the Ghidra project folder to store the imported file.
        @param file the file to import.
        """
        ...

    def importFiles(self, __a0: ghidra.framework.model.DomainFolder, __a1: List[object]) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
