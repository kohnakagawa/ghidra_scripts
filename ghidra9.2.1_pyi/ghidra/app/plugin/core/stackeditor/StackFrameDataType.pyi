from typing import List
import ghidra.app.plugin.core.stackeditor
import ghidra.docking.settings
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.program.model.mem
import ghidra.util
import java.lang
import java.net
import javax.swing.event


class StackFrameDataType(ghidra.app.plugin.core.stackeditor.BiDirectionDataType):




    @overload
    def __init__(self, __a0: ghidra.app.plugin.core.stackeditor.StackFrameDataType, __a1: ghidra.program.model.data.DataTypeManager): ...

    @overload
    def __init__(self, __a0: ghidra.program.model.listing.StackFrame, __a1: ghidra.program.model.data.DataTypeManager): ...



    @overload
    def add(self, __a0: ghidra.program.model.data.DataType) -> ghidra.program.model.data.DataTypeComponent: ...

    @overload
    def add(self, __a0: ghidra.program.model.data.DataType, __a1: int) -> ghidra.program.model.data.DataTypeComponent: ...

    @overload
    def add(self, __a0: ghidra.program.model.data.DataType, __a1: unicode, __a2: unicode) -> ghidra.program.model.data.DataTypeComponent: ...

    @overload
    def add(self, __a0: ghidra.program.model.data.DataType, __a1: int, __a2: unicode, __a3: unicode) -> ghidra.program.model.data.DataTypeComponent: ...

    def addBitField(self, __a0: ghidra.program.model.data.DataType, __a1: int, __a2: unicode, __a3: unicode) -> ghidra.program.model.data.DataTypeComponent: ...

    def addNegative(self, __a0: ghidra.program.model.data.DataType, __a1: int, __a2: unicode, __a3: unicode) -> ghidra.program.model.data.DataTypeComponent: ...

    def addParent(self, __a0: ghidra.program.model.data.DataType) -> None: ...

    def addPositive(self, __a0: ghidra.program.model.data.DataType, __a1: int, __a2: unicode, __a3: unicode) -> ghidra.program.model.data.DataTypeComponent: ...

    def adjustInternalAlignment(self) -> None: ...

    def clearComponent(self, __a0: int) -> None: ...

    def clearComponentAt(self, __a0: int) -> None: ...

    def clearFlexibleArrayComponent(self) -> None: ...

    def clone(self, __a0: ghidra.program.model.data.DataTypeManager) -> ghidra.app.plugin.core.stackeditor.BiDirectionDataType: ...

    def copy(self, __a0: ghidra.program.model.data.DataTypeManager) -> ghidra.program.model.data.DataType: ...

    def dataTypeAlignmentChanged(self, __a0: ghidra.program.model.data.DataType) -> None: ...

    def dataTypeDeleted(self, __a0: ghidra.program.model.data.DataType) -> None: ...

    def dataTypeNameChanged(self, __a0: ghidra.program.model.data.DataType, __a1: unicode) -> None: ...

    def dataTypeReplaced(self, __a0: ghidra.program.model.data.DataType, __a1: ghidra.program.model.data.DataType) -> None: ...

    def dataTypeSizeChanged(self, __a0: ghidra.program.model.data.DataType) -> None: ...

    @overload
    def delete(self, __a0: int) -> None: ...

    @overload
    def delete(self, __a0: List[int]) -> None: ...

    def deleteAll(self) -> None: ...

    def deleteAtOffset(self, __a0: int) -> None: ...

    def dependsOn(self, __a0: ghidra.program.model.data.DataType) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getAlignment(self) -> int: ...

    def getBitFieldPacking(self) -> ghidra.program.model.data.BitFieldPacking: ...

    def getCategoryPath(self) -> ghidra.program.model.data.CategoryPath: ...

    def getClass(self) -> java.lang.Class: ...

    def getComponent(self, __a0: int) -> ghidra.program.model.data.DataTypeComponent: ...

    def getComponentAt(self, __a0: int) -> ghidra.program.model.data.DataTypeComponent: ...

    def getComponents(self) -> List[ghidra.program.model.data.DataTypeComponent]: ...

    def getDataOrganization(self) -> ghidra.program.model.data.DataOrganization: ...

    def getDataTypeAt(self, __a0: int) -> ghidra.program.model.data.DataTypeComponent: ...

    def getDataTypeManager(self) -> ghidra.program.model.data.DataTypeManager: ...

    def getDataTypePath(self) -> ghidra.program.model.data.DataTypePath: ...

    def getDefaultAbbreviatedLabelPrefix(self) -> unicode: ...

    @overload
    def getDefaultLabelPrefix(self) -> unicode: ...

    @overload
    def getDefaultLabelPrefix(self, __a0: ghidra.program.model.mem.MemBuffer, __a1: ghidra.docking.settings.Settings, __a2: int, __a3: ghidra.program.model.data.DataTypeDisplayOptions) -> unicode: ...

    def getDefaultName(self, __a0: ghidra.program.model.data.DataTypeComponent) -> unicode: ...

    def getDefaultOffcutLabelPrefix(self, __a0: ghidra.program.model.mem.MemBuffer, __a1: ghidra.docking.settings.Settings, __a2: int, __a3: ghidra.program.model.data.DataTypeDisplayOptions, __a4: int) -> unicode: ...

    def getDefaultSettings(self) -> ghidra.docking.settings.Settings: ...

    def getDefinedComponentAtOffset(self, __a0: int) -> ghidra.program.model.data.DataTypeComponent: ...

    def getDefinedComponentAtOrdinal(self, __a0: int) -> ghidra.program.model.data.DataTypeComponent: ...

    def getDefinedComponents(self) -> List[ghidra.program.model.data.DataTypeComponent]: ...

    def getDescription(self) -> unicode: ...

    def getDisplayName(self) -> unicode: ...

    def getDocs(self) -> java.net.URL: ...

    def getFlexibleArrayComponent(self) -> ghidra.program.model.data.DataTypeComponent: ...

    def getFrameSize(self) -> int: ...

    def getFunction(self) -> ghidra.program.model.listing.Function: ...

    @staticmethod
    def getHexString(__a0: int, __a1: bool) -> unicode: ...

    def getLastChangeTime(self) -> long: ...

    def getLastChangeTimeInSourceArchive(self) -> long: ...

    def getLength(self) -> int: ...

    def getLocalSize(self) -> int: ...

    def getMaxLength(self, __a0: int) -> int: ...

    def getMinimumAlignment(self) -> int: ...

    def getMnemonic(self, __a0: ghidra.docking.settings.Settings) -> unicode: ...

    def getName(self) -> unicode: ...

    def getNegativeLength(self) -> int: ...

    def getNumComponents(self) -> int: ...

    def getNumDefinedComponents(self) -> int: ...

    def getPackingValue(self) -> int: ...

    def getParameterOffset(self) -> int: ...

    def getParameterSize(self) -> int: ...

    def getParents(self) -> List[ghidra.program.model.data.DataType]: ...

    def getPathName(self) -> unicode: ...

    def getPositiveLength(self) -> int: ...

    def getRepresentation(self, __a0: ghidra.program.model.mem.MemBuffer, __a1: ghidra.docking.settings.Settings, __a2: int) -> unicode: ...

    def getReturnAddressOffset(self) -> int: ...

    def getSettingsDefinitions(self) -> List[ghidra.docking.settings.SettingsDefinition]: ...

    def getSourceArchive(self) -> ghidra.program.model.data.SourceArchive: ...

    def getSplitOffset(self) -> int: ...

    def getStackVariables(self) -> List[ghidra.program.model.listing.Variable]: ...

    def getUniversalID(self) -> ghidra.util.UniversalID: ...

    def getValue(self, __a0: ghidra.program.model.mem.MemBuffer, __a1: ghidra.docking.settings.Settings, __a2: int) -> object: ...

    def getValueClass(self, __a0: ghidra.docking.settings.Settings) -> java.lang.Class: ...

    def growStructure(self, __a0: int) -> None: ...

    def growsNegative(self) -> bool: ...

    def hasFlexibleArrayComponent(self) -> bool: ...

    def hashCode(self) -> int: ...

    @overload
    def insert(self, __a0: int, __a1: ghidra.program.model.data.DataType) -> ghidra.program.model.data.DataTypeComponent: ...

    @overload
    def insert(self, __a0: int, __a1: ghidra.program.model.data.DataType, __a2: int) -> ghidra.program.model.data.DataTypeComponent: ...

    @overload
    def insert(self, __a0: int, __a1: ghidra.program.model.data.DataType, __a2: int, __a3: unicode, __a4: unicode) -> ghidra.program.model.data.DataTypeComponent: ...

    @overload
    def insertAtOffset(self, __a0: int, __a1: ghidra.program.model.data.DataType, __a2: int) -> ghidra.program.model.data.DataTypeComponentImpl: ...

    @overload
    def insertAtOffset(self, __a0: int, __a1: ghidra.program.model.data.DataType, __a2: int, __a3: unicode, __a4: unicode) -> ghidra.program.model.data.DataTypeComponentImpl: ...

    def insertBitField(self, __a0: int, __a1: int, __a2: int, __a3: ghidra.program.model.data.DataType, __a4: int, __a5: unicode, __a6: unicode) -> ghidra.program.model.data.DataTypeComponent: ...

    def insertBitFieldAt(self, __a0: int, __a1: int, __a2: int, __a3: ghidra.program.model.data.DataType, __a4: int, __a5: unicode, __a6: unicode) -> ghidra.program.model.data.DataTypeComponentImpl: ...

    def isDefaultAligned(self) -> bool: ...

    def isDeleted(self) -> bool: ...

    def isDynamicallySized(self) -> bool: ...

    def isEquivalent(self, __a0: ghidra.program.model.data.DataType) -> bool: ...

    def isInternallyAligned(self) -> bool: ...

    def isMachineAligned(self) -> bool: ...

    def isNotYetDefined(self) -> bool: ...

    def isPartOf(self, __a0: ghidra.program.model.data.DataType) -> bool: ...

    def isStackVariable(self, __a0: int) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def pack(self, __a0: int) -> None: ...

    def realign(self) -> None: ...

    def removeParent(self, __a0: ghidra.program.model.data.DataType) -> None: ...

    @overload
    def replace(self, __a0: int, __a1: ghidra.program.model.data.DataType, __a2: int) -> ghidra.program.model.data.DataTypeComponent: ...

    @overload
    def replace(self, __a0: int, __a1: ghidra.program.model.data.DataType, __a2: int, __a3: unicode, __a4: unicode) -> ghidra.program.model.data.DataTypeComponent: ...

    def replaceAtOffset(self, __a0: int, __a1: ghidra.program.model.data.DataType, __a2: int, __a3: unicode, __a4: unicode) -> ghidra.program.model.data.DataTypeComponent: ...

    @overload
    def replaceWith(self, __a0: ghidra.program.model.data.Structure) -> None: ...

    @overload
    def replaceWith(self, __a0: ghidra.program.model.data.DataType) -> None: ...

    def setCategoryPath(self, __a0: ghidra.program.model.data.CategoryPath) -> None: ...

    def setComment(self, __a0: int, __a1: unicode) -> bool: ...

    def setDataType(self, __a0: int, __a1: ghidra.program.model.data.DataType, __a2: int) -> ghidra.program.model.data.DataTypeComponent: ...

    def setDefaultSettings(self, __a0: ghidra.docking.settings.Settings) -> None: ...

    def setDescription(self, __a0: unicode) -> None: ...

    def setFlexibleArrayComponent(self, __a0: ghidra.program.model.data.DataType, __a1: unicode, __a2: unicode) -> ghidra.program.model.data.DataTypeComponent: ...

    def setInternallyAligned(self, __a0: bool) -> None: ...

    def setLastChangeTime(self, __a0: long) -> None: ...

    def setLastChangeTimeInSourceArchive(self, __a0: long) -> None: ...

    def setLocalSize(self, __a0: int) -> bool: ...

    def setMinimumAlignment(self, __a0: int) -> None: ...

    @overload
    def setName(self, __a0: unicode) -> None: ...

    @overload
    def setName(self, __a0: int, __a1: unicode) -> bool: ...

    def setNameAndCategory(self, __a0: ghidra.program.model.data.CategoryPath, __a1: unicode) -> None: ...

    def setOffset(self, __a0: int, __a1: int) -> ghidra.program.model.data.DataTypeComponent: ...

    def setPackingValue(self, __a0: int) -> None: ...

    def setParameterSize(self, __a0: int) -> bool: ...

    def setSourceArchive(self, __a0: ghidra.program.model.data.SourceArchive) -> None: ...

    def setToDefaultAlignment(self) -> None: ...

    def setToMachineAlignment(self) -> None: ...

    def setValue(self, __a0: ghidra.program.model.mem.MemBuffer, __a1: ghidra.docking.settings.Settings, __a2: int, __a3: object) -> None: ...

    def stateChanged(self, __a0: javax.swing.event.ChangeEvent) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def frameSize(self) -> int: ...

    @property
    def function(self) -> ghidra.program.model.listing.Function: ...

    @property
    def localSize(self) -> int: ...

    @localSize.setter
    def localSize(self, value: int) -> None: ...

    @property
    def parameterOffset(self) -> int: ...

    @property
    def parameterSize(self) -> int: ...

    @parameterSize.setter
    def parameterSize(self, value: int) -> None: ...

    @property
    def returnAddressOffset(self) -> int: ...

    @property
    def stackVariables(self) -> List[ghidra.program.model.listing.Variable]: ...