from typing import List
import ghidra
import ghidra.util.task
import java.io
import java.lang


class DataTypeArchiveTransformer(object, ghidra.GhidraLaunchable):
    """
    DataTypeArchiveTransformer changes (transforms) a new archive file so that it appears to be
     an updated copy of a previously existing data type archive. This allows us to parse a new
     version of each standard GDT file we supply. This class changes the IDs on the data types
     so they will match the previous version's IDs. This allows the new data type archive and
     its data types to become the associated data types where the previous version data types
     were applied.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def fixupGUI() -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def launch(self, layout: ghidra.GhidraApplicationLayout, args: List[unicode]) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @staticmethod
    def transform(oldFile: java.io.File, newFile: java.io.File, destinationFile: java.io.File, useOldFileID: bool, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
