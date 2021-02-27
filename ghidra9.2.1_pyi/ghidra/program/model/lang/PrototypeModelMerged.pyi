from typing import List
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.lang
import ghidra.program.model.lang.ParamList
import ghidra.program.model.listing
import ghidra.xml
import java.lang


class PrototypeModelMerged(ghidra.program.model.lang.PrototypeModel):
    """
    This model serves as a placeholder for multiple model
     Currently all the models being selected between must share the same output model
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getArgLocation(self, argIndex: int, params: List[ghidra.program.model.listing.Parameter], dataType: ghidra.program.model.data.DataType, program: ghidra.program.model.listing.Program) -> ghidra.program.model.listing.VariableStorage:
        """
        Get the preferred parameter location for a specified parameter specified by argIndex
         which will be added/inserted within the set of existing function params.
         If existing parameters use custom storage, this method should not be used.
        @param params existing set parameters to which the parameter specified by
         argIndex will be added/inserted be appended (may be null).
        @param dataType dataType associated with next parameter location or null
         for a default undefined type.
        @param program
        @return parameter location or {@link VariableStorage#UNASSIGNED_STORAGE} if
         unable to determine suitable location
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getExtrapop(self) -> int: ...

    def getGenericCallingConvention(self) -> ghidra.program.model.data.GenericCallingConvention: ...

    def getInputListType(self) -> ghidra.program.model.lang.InputListType: ...

    def getModel(self, i: int) -> ghidra.program.model.lang.PrototypeModel: ...

    def getName(self) -> unicode: ...

    def getNextArgLocation(self, params: List[ghidra.program.model.listing.Parameter], dataType: ghidra.program.model.data.DataType, program: ghidra.program.model.listing.Program) -> ghidra.program.model.listing.VariableStorage:
        """
        Get the preferred parameter location for a new parameter which will appended
         to the end of an existing set of params.  If existing parameters use custom
         storage, this method should not be used.
        @param params existing set parameters to which the next parameter will
         be appended. (may be null)
        @param dataType dataType associated with next parameter location or null
         for a default undefined type.
        @param program
        @return next parameter location or {@link VariableStorage#UNASSIGNED_STORAGE} if
         unable to determine suitable location
        """
        ...

    def getPotentialInputRegisterStorage(self, prog: ghidra.program.model.listing.Program) -> List[ghidra.program.model.listing.VariableStorage]: ...

    def getReturnLocation(self, dataType: ghidra.program.model.data.DataType, program: ghidra.program.model.listing.Program) -> ghidra.program.model.listing.VariableStorage:
        """
        @deprecated Get the preferred return location given the specified dataType.
         In truth, there is no one location.  The routines that use this method tend
         to want the default storage location for integer or pointer return values.
        @param dataType first parameter dataType or null for a default
         undefined type.
        @param program
        @return return location or {@link VariableStorage#UNASSIGNED_STORAGE} if
         unable to determine suitable location
        """
        ...

    def getStackParameterAlignment(self) -> int: ...

    def getStackParameterOffset(self) -> long: ...

    def getStackshift(self) -> int: ...

    def getStorageLocations(self, program: ghidra.program.model.listing.Program, dataTypes: List[ghidra.program.model.data.DataType], addAutoParams: bool) -> List[ghidra.program.model.listing.VariableStorage]:
        """
        Compute the variable storage for a given function and set of return/parameter datatypes
         defined by an array of data types.
        @param program
        @param dataTypes return/parameter datatypes (first element is always the return datatype,
         i.e., minimum array length is 1)
        @param addAutoParams TODO
        @return dynamic storage locations orders by ordinal where first element corresponds to
         return storage. The returned array may also include additional auto-parameter storage
         locations.
        """
        ...

    def hasThisPointer(self) -> bool: ...

    def hashCode(self) -> int: ...

    def isConstructor(self) -> bool: ...

    def isMerged(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def numModels(self) -> int: ...

    def possibleInputParamWithSlot(self, loc: ghidra.program.model.address.Address, size: int, res: ghidra.program.model.lang.ParamList.WithSlotRec) -> bool: ...

    def possibleOutputParamWithSlot(self, loc: ghidra.program.model.address.Address, size: int, res: ghidra.program.model.lang.ParamList.WithSlotRec) -> bool: ...

    @overload
    def restoreXml(self, parser: ghidra.xml.XmlPullParser, cspec: ghidra.program.model.lang.CompilerSpec, normalstack: bool) -> None: ...

    @overload
    def restoreXml(self, __a0: ghidra.xml.XmlPullParser, __a1: List[object], __a2: bool) -> None: ...

    def selectModel(self, params: List[ghidra.program.model.listing.Parameter]) -> ghidra.program.model.lang.PrototypeModel: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def merged(self) -> bool: ...
