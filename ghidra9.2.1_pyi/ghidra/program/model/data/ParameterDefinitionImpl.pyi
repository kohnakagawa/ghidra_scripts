import ghidra.program.model.data
import ghidra.program.model.listing
import java.lang


class ParameterDefinitionImpl(object, ghidra.program.model.data.ParameterDefinition):




    def __init__(self, name: unicode, dataType: ghidra.program.model.data.DataType, comment: unicode):
        """
        Constructs a new ParameterImp with an unassigned ordinal.  The ordinal will be
         established by the function definition.
        @param name the name of the parameter.
        @param dataType the fixed-length datatype of the parameter
        @param comment the comment to store about this parameter.
        @throws IllegalArgumentException if invalid parameter datatype specified
        """
        ...



    @overload
    def compareTo(self, p: ghidra.program.model.data.ParameterDefinition) -> int:
        """
        @see java.lang.Comparable#compareTo(java.lang.Object)
        """
        ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getComment(self) -> unicode: ...

    def getDataType(self) -> ghidra.program.model.data.DataType: ...

    def getLength(self) -> int: ...

    def getName(self) -> unicode: ...

    def getOrdinal(self) -> int: ...

    def hashCode(self) -> int: ...

    @overload
    def isEquivalent(self, parm: ghidra.program.model.data.ParameterDefinition) -> bool: ...

    @overload
    def isEquivalent(self, variable: ghidra.program.model.listing.Variable) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setComment(self, comment: unicode) -> None: ...

    def setDataType(self, type: ghidra.program.model.data.DataType) -> None: ...

    def setName(self, name: unicode) -> None: ...

    def toString(self) -> unicode: ...

    @staticmethod
    def validateDataType(dataType: ghidra.program.model.data.DataType, dtMgr: ghidra.program.model.data.DataTypeManager, isReturn: bool) -> ghidra.program.model.data.DataType:
        """
        Validate the specified datatype based upon its use as a parameter or return type.
         Ensure that the datatype has been cloned to the specified datatype manager (dtMgr).
        @param dataType datatype to be validated
        @param dtMgr target datatype manager
        @param isReturn true if checking return datatype, false if parameter datatype.
        @return datatype suitable for use within the target {@link FunctionDefinition}.
        @throws IllegalArgumentException if invalid datatype specified
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def comment(self) -> unicode: ...

    @comment.setter
    def comment(self, value: unicode) -> None: ...

    @property
    def dataType(self) -> ghidra.program.model.data.DataType: ...

    @dataType.setter
    def dataType(self, value: ghidra.program.model.data.DataType) -> None: ...

    @property
    def length(self) -> int: ...

    @property
    def name(self) -> unicode: ...

    @name.setter
    def name(self, value: unicode) -> None: ...

    @property
    def ordinal(self) -> int: ...
