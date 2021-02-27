from typing import List
import ghidra.program.model.data
import java.lang
import javax.swing


class CycleGroup(object):
    """
    Class to define a set of dataTypes that a single action can cycle through.
    """

    ALL_CYCLE_GROUPS: List[object] = [ghidra.program.model.data.CycleGroup$ByteCycleGroup@679de454, ghidra.program.model.data.CycleGroup$FloatCycleGroup@e6856e7, ghidra.program.model.data.CycleGroup$StringCycleGroup@27310335]
    BYTE_CYCLE_GROUP: ghidra.program.model.data.CycleGroup = ghidra.program.model.data.CycleGroup$ByteCycleGroup@679de454
    FLOAT_CYCLE_GROUP: ghidra.program.model.data.CycleGroup = ghidra.program.model.data.CycleGroup$FloatCycleGroup@e6856e7
    STRING_CYCLE_GROUP: ghidra.program.model.data.CycleGroup = ghidra.program.model.data.CycleGroup$StringCycleGroup@27310335



    @overload
    def __init__(self, name: unicode):
        """
        Construct empty group no name, data types or keystroke.
        """
        ...

    @overload
    def __init__(self, name: unicode, dataTypes: List[ghidra.program.model.data.DataType], keyStroke: javax.swing.KeyStroke):
        """
        Constructs a new cycle group with the given dataTypes.
        @param name cycle group name which will be the suggested action name
         for those plugins which implement a cycle group action.
        @param dataTypes data types in the group
        @param keyStroke default key stroke for the action to cycle through the
         data types
        """
        ...

    @overload
    def __init__(self, name: unicode, dt: ghidra.program.model.data.DataType, keyStroke: javax.swing.KeyStroke):
        """
        Constructor cycle group with one data type.
        @param name cycle group name which will be the suggested action name
         for those plugins which implement a cycle group action.
        @param dt single data type for the group
        @param keyStroke default key stroke for the action to cycle through the
         data types
        """
        ...



    def addDataType(self, dt: ghidra.program.model.data.DataType) -> None:
        """
        Add a data type to this group.
        @param dt the datatype to be added.
        """
        ...

    def addFirst(self, dt: ghidra.program.model.data.DataType) -> None:
        """
        Add the data type as the first in the list.
        @param dt the dataType to be added.
        """
        ...

    def contains(self, dt: ghidra.program.model.data.DataType) -> bool:
        """
        Return true if the given data type is in this cycle group.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDataTypes(self) -> List[ghidra.program.model.data.DataType]:
        """
        Get the data types in this group.
        """
        ...

    def getDefaultKeyStroke(self) -> javax.swing.KeyStroke: ...

    def getName(self) -> unicode:
        """
        @return cycle group name.
        """
        ...

    def getNextDataType(self, currentDataType: ghidra.program.model.data.DataType, stackPointers: bool) -> ghidra.program.model.data.DataType:
        """
        Get next data-type which should be used
        @param currentDataType current data type to which this cycle group is to be applied
        @param stackPointers if true and currentDataType is a pointer, the pointer's
         base type will be cycled
        @return next data-type
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeDataType(self, dt: ghidra.program.model.data.DataType) -> None:
        """
        Remove the data type from this group.
        @param dt the dataType to remove.
        """
        ...

    def removeFirst(self) -> None:
        """
        Remove first data type in the list.
        """
        ...

    def removeLast(self) -> None:
        """
        Remove the last data type in the list.
        """
        ...

    def size(self) -> int:
        """
        Returns number of types in group
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def dataTypes(self) -> List[ghidra.program.model.data.DataType]: ...

    @property
    def defaultKeyStroke(self) -> javax.swing.KeyStroke: ...

    @property
    def name(self) -> unicode: ...
