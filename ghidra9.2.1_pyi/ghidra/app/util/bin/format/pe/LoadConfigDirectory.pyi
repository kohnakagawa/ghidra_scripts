import ghidra.app.util.bin
import ghidra.app.util.bin.format.pe.LoadConfigDirectory
import ghidra.program.model.data
import java.lang


class LoadConfigDirectory(object, ghidra.app.util.bin.StructConverter):
    """
    A class to represent the IMAGE_LOAD_CONFIG_DIRECTORY
     data structure which is defined in winnt.h.
    """

    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    NAME32: unicode = u'IMAGE_LOAD_CONFIG_DIRECTORY32'
    NAME64: unicode = u'IMAGE_LOAD_CONFIG_DIRECTORY64'
    POINTER: ghidra.program.model.data.DataType = pointer
    QWORD: ghidra.program.model.data.DataType = qword
    STRING: ghidra.program.model.data.DataType = string
    UTF16: ghidra.program.model.data.DataType = unicode
    UTF8: ghidra.program.model.data.DataType = string-utf8
    VOID: ghidra.program.model.data.DataType = void
    WORD: ghidra.program.model.data.DataType = word



    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getCfgCheckFunctionPointer(self) -> long:
        """
        Gets the ControlFlowGuard check function pointer address.
        @return The ControlFlowGuard check function pointer address.
           Could be 0 if ControlFlowGuard is not being used.
        """
        ...

    def getCfgDispatchFunctionPointer(self) -> long:
        """
        Gets the ControlFlowGuard dispatch function pointer address.
        @return The ControlFlowGuard dispatch function pointer address.
           Could be 0 if ControlFlowGuard is not being used.
        """
        ...

    def getCfgFunctionCount(self) -> long:
        """
        Gets the ControlFlowGuard function count.
        @return The ControlFlowGuard function count.  Could be 0 if ControlFlowGuard is
           not being used.
        """
        ...

    def getCfgFunctionTablePointer(self) -> long:
        """
        Gets the ControlFlowGuard function table pointer address.
        @return The ControlFlowGuard function table function pointer address.
           Could be 0 if ControlFlowGuard is not being used.
        """
        ...

    def getCfgGuardFlags(self) -> ghidra.app.util.bin.format.pe.LoadConfigDirectory.GuardFlags:
        """
        Gets the ControlFlowGuard {@link GuardFlags}.
        @return The ControlFlowGuard {@link GuardFlags}.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getCriticalSectionDefaultTimeout(self) -> int:
        """
        Returns the critical section default time-out value.
        @return the critical section default time-out value
        """
        ...

    def getRfgFailureRoutine(self) -> long:
        """
        Gets the ReturnFlowGuard failure routine address.
        @return The ReturnFlowGuard failure routine address.
           Could be 0 if ReturnFlowGuard is not being used.
        """
        ...

    def getRfgFailureRoutineFunctionPointer(self) -> long:
        """
        Gets the ReturnFlowGuard failure routine function pointer address.
        @return The ReturnFlowGuard failure routine function pointer address.
           Could be 0 if ReturnFlowGuard is not being used.
        """
        ...

    def getRfgVerifyStackPointerFunctionPointer(self) -> long:
        """
        Gets the ReturnFlowGuard verify stack pointer function pointer address.
        @return The ReturnFlowGuard verify stack pointer function pointer address.
           Could be 0 if ReturnFlowGuard is not being used.
        """
        ...

    def getSeHandlerCount(self) -> long:
        """
        Gets the safe exception handler table count.
        @return the safe exception handler table count.
        """
        ...

    def getSeHandlerTable(self) -> long:
        """
        Gets the safe exception handler table.
        @return the safe exception handler table.
        """
        ...

    def getSize(self) -> int:
        """
        Returns the size (in bytes) of this structure.
        @return the size (in bytes) of this structure
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def cfgCheckFunctionPointer(self) -> long: ...

    @property
    def cfgDispatchFunctionPointer(self) -> long: ...

    @property
    def cfgFunctionCount(self) -> long: ...

    @property
    def cfgFunctionTablePointer(self) -> long: ...

    @property
    def cfgGuardFlags(self) -> ghidra.app.util.bin.format.pe.LoadConfigDirectory.GuardFlags: ...

    @property
    def criticalSectionDefaultTimeout(self) -> int: ...

    @property
    def rfgFailureRoutine(self) -> long: ...

    @property
    def rfgFailureRoutineFunctionPointer(self) -> long: ...

    @property
    def rfgVerifyStackPointerFunctionPointer(self) -> long: ...

    @property
    def seHandlerCount(self) -> long: ...

    @property
    def seHandlerTable(self) -> long: ...

    @property
    def size(self) -> int: ...
