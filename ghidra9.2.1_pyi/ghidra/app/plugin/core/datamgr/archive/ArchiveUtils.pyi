from typing import List
import ghidra.app.plugin.core.datamgr.archive
import java.awt
import java.lang


class ArchiveUtils(object):








    @overload
    @staticmethod
    def canClose(__a0: ghidra.app.plugin.core.datamgr.archive.Archive, __a1: java.awt.Component) -> bool: ...

    @overload
    @staticmethod
    def canClose(__a0: List[object], __a1: java.awt.Component) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def lockArchive(__a0: ghidra.app.plugin.core.datamgr.archive.FileArchive) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def save(__a0: java.awt.Component, __a1: ghidra.app.plugin.core.datamgr.archive.Archive) -> None: ...

    @staticmethod
    def saveAs(__a0: java.awt.Component, __a1: ghidra.app.plugin.core.datamgr.archive.FileArchive) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
