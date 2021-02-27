import ghidra.app.plugin.core.datamgr.archive
import ghidra.framework.model
import ghidra.program.model.data
import java.awt
import java.lang
import javax.swing


class DomainFileArchive(ghidra.app.plugin.core.datamgr.archive.Archive, object):








    def close(self) -> None: ...

    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDataTypeManager(self) -> ghidra.program.model.data.DataTypeManager: ...

    def getDomainFile(self) -> ghidra.framework.model.DomainFile: ...

    def getDomainObject(self) -> ghidra.framework.model.DomainObject: ...

    def getIcon(self, __a0: bool) -> javax.swing.ImageIcon: ...

    def getName(self) -> unicode: ...

    def hashCode(self) -> int: ...

    def isChanged(self) -> bool: ...

    def isModifiable(self) -> bool: ...

    def isSavable(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def save(self) -> None: ...

    def saveAs(self, __a0: java.awt.Component) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def changed(self) -> bool: ...

    @property
    def dataTypeManager(self) -> ghidra.program.model.data.DataTypeManager: ...

    @property
    def domainFile(self) -> ghidra.framework.model.DomainFile: ...

    @property
    def domainObject(self) -> ghidra.framework.model.DomainObject: ...

    @property
    def modifiable(self) -> bool: ...

    @property
    def name(self) -> unicode: ...

    @property
    def savable(self) -> bool: ...
