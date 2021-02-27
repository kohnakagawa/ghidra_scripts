from typing import List
import ghidra.app.plugin.core.navigation.locationreferences
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.program.util
import ghidra.util.datastruct
import ghidra.util.task
import java.lang
import java.util
import java.util.function


class ReferenceUtils(object):
    CONTEXT_CALLOUT_END: unicode = u'|]'
    CONTEXT_CALLOUT_END_REGEX: unicode = u'\\|\\]'
    CONTEXT_CALLOUT_START: unicode = u'[|'
    CONTEXT_CALLOUT_START_REGEX: unicode = u'\\[\\|'







    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def findDataTypeMatchesInDefinedData(__a0: ghidra.util.datastruct.Accumulator, __a1: ghidra.program.model.listing.Program, __a2: java.util.function.Predicate, __a3: unicode, __a4: ghidra.util.task.TaskMonitor) -> None: ...

    @overload
    @staticmethod
    def findDataTypeReferences(__a0: ghidra.util.datastruct.Accumulator, __a1: ghidra.program.model.data.DataType, __a2: unicode, __a3: ghidra.program.model.listing.Program, __a4: ghidra.util.task.TaskMonitor) -> None: ...

    @overload
    @staticmethod
    def findDataTypeReferences(__a0: ghidra.util.datastruct.Accumulator, __a1: ghidra.program.model.data.DataType, __a2: unicode, __a3: ghidra.program.model.listing.Program, __a4: bool, __a5: ghidra.util.task.TaskMonitor) -> None: ...

    @overload
    @staticmethod
    def getBaseDataType(__a0: ghidra.program.model.data.DataType) -> ghidra.program.model.data.DataType: ...

    @overload
    @staticmethod
    def getBaseDataType(__a0: ghidra.program.model.data.DataType, __a1: bool) -> ghidra.program.model.data.DataType: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getLocationDescriptor(__a0: ghidra.program.util.ProgramLocation) -> ghidra.app.plugin.core.navigation.locationreferences.LocationDescriptor: ...

    @staticmethod
    def getReferenceAddresses(__a0: ghidra.program.util.ProgramLocation, __a1: ghidra.util.task.TaskMonitor) -> java.util.Set: ...

    @staticmethod
    def getReferences(__a0: ghidra.util.datastruct.Accumulator, __a1: ghidra.program.util.ProgramLocation, __a2: ghidra.util.task.TaskMonitor) -> None: ...

    @staticmethod
    def getVariableReferences(__a0: ghidra.util.datastruct.Accumulator, __a1: ghidra.program.model.listing.Program, __a2: ghidra.program.model.listing.Variable) -> None: ...

    @staticmethod
    def getVariables(__a0: ghidra.program.model.listing.Function, __a1: bool) -> List[object]: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isOffcut(__a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.Address) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
