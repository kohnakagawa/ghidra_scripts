from typing import List
import ghidra.app.util.bin.format.pdb
import ghidra.app.util.importer
import ghidra.app.util.pdb
import ghidra.program.model.listing
import ghidra.xml
import java.io
import java.lang


class PdbParser(object):
    onWindows: bool = False




    class PdbFileType(java.lang.Enum):
        PDB: ghidra.app.util.bin.format.pdb.PdbParser.PdbFileType = .pdb
        XML: ghidra.app.util.bin.format.pdb.PdbParser.PdbFileType = .xml







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.pdb.PdbParser.PdbFileType: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.app.util.bin.format.pdb.PdbParser.PdbFileType]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...



    @overload
    def __init__(self, __a0: java.io.File, __a1: ghidra.program.model.listing.Program, __a2: ghidra.app.services.DataTypeManagerService, __a3: bool, __a4: ghidra.util.task.TaskMonitor): ...

    @overload
    def __init__(self, __a0: java.io.File, __a1: ghidra.program.model.listing.Program, __a2: ghidra.app.services.DataTypeManagerService, __a3: ghidra.app.util.pdb.PdbProgramAttributes, __a4: bool, __a5: ghidra.util.task.TaskMonitor): ...



    def applyTo(self, __a0: ghidra.app.util.importer.MessageLog) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    @overload
    @staticmethod
    def findPDB(__a0: ghidra.program.model.listing.Program) -> java.io.File: ...

    @overload
    @staticmethod
    def findPDB(__a0: ghidra.program.model.listing.Program, __a1: bool, __a2: java.io.File) -> java.io.File: ...

    @overload
    @staticmethod
    def findPDB(__a0: ghidra.app.util.pdb.PdbProgramAttributes, __a1: bool, __a2: java.io.File, __a3: ghidra.app.util.bin.format.pdb.PdbParser.PdbFileType) -> java.io.File: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getPdbAttributes(__a0: ghidra.program.model.listing.Program) -> ghidra.app.util.pdb.PdbProgramAttributes: ...

    @overload
    def getPdbXmlMember(self, __a0: ghidra.xml.XmlElement) -> ghidra.app.util.bin.format.pdb.PdbParser.PdbXmlMember: ...

    @overload
    def getPdbXmlMember(self, __a0: ghidra.xml.XmlTreeNode) -> ghidra.app.util.bin.format.pdb.PdbMember: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isAlreadyLoaded(__a0: ghidra.program.model.listing.Program) -> bool: ...

    def isPdbLoaded(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def openDataTypeArchives(self) -> None: ...

    def parse(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def pdbLoaded(self) -> bool: ...
