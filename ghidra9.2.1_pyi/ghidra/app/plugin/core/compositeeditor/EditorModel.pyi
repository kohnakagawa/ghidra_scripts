import ghidra.app.plugin.core.compositeeditor
import ghidra.program.model.data
import ghidra.util.task
import java.lang


class EditorModel(object):








    @overload
    def add(self, __a0: ghidra.program.model.data.DataType) -> ghidra.program.model.data.DataTypeComponent: ...

    @overload
    def add(self, __a0: int, __a1: ghidra.program.model.data.DataType) -> ghidra.program.model.data.DataTypeComponent: ...

    @overload
    def add(self, __a0: int, __a1: ghidra.program.model.data.DataType, __a2: int) -> ghidra.program.model.data.DataTypeComponent: ...

    def addCompositeEditorModelListener(self, __a0: ghidra.app.plugin.core.compositeeditor.CompositeEditorModelListener) -> None: ...

    def apply(self) -> bool: ...

    def beginEditingField(self, __a0: int, __a1: int) -> bool: ...

    def clearComponent(self, __a0: int) -> None: ...

    def clearSelectedComponents(self) -> None: ...

    def createArray(self) -> None: ...

    def cycleDataType(self, __a0: ghidra.program.model.data.CycleGroup) -> None: ...

    def deleteSelectedComponents(self, __a0: ghidra.util.task.TaskMonitor) -> None: ...

    def dispose(self) -> None: ...

    def duplicateMultiple(self, __a0: int, __a1: int, __a2: ghidra.util.task.TaskMonitor) -> None: ...

    def endEditingField(self) -> bool: ...

    def endFieldEditing(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFirstEditableColumn(self, __a0: int) -> int: ...

    def getLastNumBytes(self) -> int: ...

    def getLastNumDuplicates(self) -> int: ...

    def getLastNumElements(self) -> int: ...

    def getMaxAddLength(self, __a0: int) -> int: ...

    def getMaxDuplicates(self, __a0: int) -> int: ...

    def getMaxElements(self) -> int: ...

    def getMaxReplaceLength(self, __a0: int) -> int: ...

    def getProvider(self) -> ghidra.app.plugin.core.compositeeditor.CompositeEditorProvider: ...

    def hasChanges(self) -> bool: ...

    def hashCode(self) -> int: ...

    @overload
    def insert(self, __a0: ghidra.program.model.data.DataType) -> ghidra.program.model.data.DataTypeComponent: ...

    @overload
    def insert(self, __a0: int, __a1: ghidra.program.model.data.DataType) -> ghidra.program.model.data.DataTypeComponent: ...

    @overload
    def insert(self, __a0: int, __a1: ghidra.program.model.data.DataType, __a2: int) -> ghidra.program.model.data.DataTypeComponent: ...

    @overload
    def isAddAllowed(self, __a0: ghidra.program.model.data.DataType) -> bool: ...

    @overload
    def isAddAllowed(self, __a0: int, __a1: ghidra.program.model.data.DataType) -> bool: ...

    def isArrayAllowed(self) -> bool: ...

    def isBitFieldAllowed(self) -> bool: ...

    def isClearAllowed(self) -> bool: ...

    def isCycleAllowed(self, __a0: ghidra.program.model.data.CycleGroup) -> bool: ...

    def isDeleteAllowed(self) -> bool: ...

    def isDuplicateAllowed(self) -> bool: ...

    def isEditComponentAllowed(self) -> bool: ...

    def isEditFieldAllowed(self, __a0: int, __a1: int) -> bool: ...

    def isEditingField(self) -> bool: ...

    def isInsertAllowed(self, __a0: int, __a1: ghidra.program.model.data.DataType) -> bool: ...

    def isMoveDownAllowed(self) -> bool: ...

    def isMoveUpAllowed(self) -> bool: ...

    def isReplaceAllowed(self, __a0: int, __a1: ghidra.program.model.data.DataType) -> bool: ...

    def isShowingUndefinedBytes(self) -> bool: ...

    def isUnpackageAllowed(self) -> bool: ...

    def load(self, __a0: ghidra.program.model.data.Composite, __a1: bool) -> None: ...

    def moveDown(self) -> bool: ...

    def moveUp(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeCompositeEditorModelListener(self, __a0: ghidra.app.plugin.core.compositeeditor.CompositeEditorModelListener) -> None: ...

    def replace(self, __a0: int, __a1: ghidra.program.model.data.DataType, __a2: int) -> ghidra.program.model.data.DataTypeComponent: ...

    def resolve(self, __a0: ghidra.program.model.data.DataType) -> ghidra.program.model.data.DataType: ...

    def setComponentComment(self, __a0: int, __a1: unicode) -> None: ...

    def setComponentDataType(self, __a0: int, __a1: object) -> None: ...

    def setComponentDataTypeInstance(self, __a0: int, __a1: ghidra.program.model.data.DataTypeInstance) -> None: ...

    def setComponentName(self, __a0: int, __a1: unicode) -> None: ...

    def setDescription(self, __a0: unicode) -> None: ...

    def setName(self, __a0: unicode) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def arrayAllowed(self) -> bool: ...

    @property
    def bitFieldAllowed(self) -> bool: ...

    @property
    def clearAllowed(self) -> bool: ...

    @property
    def deleteAllowed(self) -> bool: ...

    @property
    def description(self) -> None: ...  # No getter available.

    @description.setter
    def description(self, value: unicode) -> None: ...

    @property
    def duplicateAllowed(self) -> bool: ...

    @property
    def editComponentAllowed(self) -> bool: ...

    @property
    def editingField(self) -> bool: ...

    @property
    def lastNumBytes(self) -> int: ...

    @property
    def lastNumDuplicates(self) -> int: ...

    @property
    def lastNumElements(self) -> int: ...

    @property
    def maxElements(self) -> int: ...

    @property
    def moveDownAllowed(self) -> bool: ...

    @property
    def moveUpAllowed(self) -> bool: ...

    @property
    def name(self) -> None: ...  # No getter available.

    @name.setter
    def name(self, value: unicode) -> None: ...

    @property
    def provider(self) -> ghidra.app.plugin.core.compositeeditor.CompositeEditorProvider: ...

    @property
    def showingUndefinedBytes(self) -> bool: ...

    @property
    def unpackageAllowed(self) -> bool: ...
