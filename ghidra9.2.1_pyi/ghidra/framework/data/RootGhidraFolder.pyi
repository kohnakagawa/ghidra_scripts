from typing import List
import ghidra.framework.data
import ghidra.framework.model
import ghidra.util.task
import java.io
import java.lang


class RootGhidraFolder(ghidra.framework.data.GhidraFolder):








    @overload
    def compareTo(self, df: ghidra.framework.model.DomainFolder) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def copyTo(self, newParent: ghidra.framework.model.DomainFolder, monitor: ghidra.util.task.TaskMonitor) -> ghidra.framework.data.GhidraFolder: ...

    @overload
    def createFile(self, fileName: unicode, obj: ghidra.framework.model.DomainObject, monitor: ghidra.util.task.TaskMonitor) -> ghidra.framework.model.DomainFile: ...

    @overload
    def createFile(self, fileName: unicode, packFile: java.io.File, monitor: ghidra.util.task.TaskMonitor) -> ghidra.framework.model.DomainFile: ...

    def createFolder(self, folderName: unicode) -> ghidra.framework.data.GhidraFolder: ...

    def delete(self) -> None: ...

    def equals(self, obj: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFile(self, fileName: unicode) -> ghidra.framework.data.GhidraFile: ...

    def getFiles(self) -> List[ghidra.framework.data.GhidraFile]: ...

    def getFolder(self, folderName: unicode) -> ghidra.framework.data.GhidraFolder: ...

    def getFolders(self) -> List[ghidra.framework.data.GhidraFolder]: ...

    def getName(self) -> unicode: ...

    def getParent(self) -> ghidra.framework.model.DomainFolder: ...

    def getPathname(self) -> unicode: ...

    def getProjectData(self) -> ghidra.framework.data.ProjectFileManager: ...

    def getProjectLocator(self) -> ghidra.framework.model.ProjectLocator: ...

    def hashCode(self) -> int: ...

    def isEmpty(self) -> bool: ...

    def isInWritableProject(self) -> bool: ...

    def moveTo(self, newParent: ghidra.framework.model.DomainFolder) -> ghidra.framework.data.GhidraFolder: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setActive(self) -> None: ...

    def setName(self, newName: unicode) -> ghidra.framework.data.GhidraFolder: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...