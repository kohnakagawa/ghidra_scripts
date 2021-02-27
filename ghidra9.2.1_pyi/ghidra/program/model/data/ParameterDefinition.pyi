import ghidra.program.model.data
import ghidra.program.model.listing
import java.lang


class ParameterDefinition(java.lang.Comparable, object):
    """
    ParameterDefinition specifies a parameter which can be
     used to specify a function definition.
    """









    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getComment(self) -> unicode:
        """
        Get the Comment for this variable
        @return the comment
        """
        ...

    def getDataType(self) -> ghidra.program.model.data.DataType:
        """
        Get the Data Type of this variable
        @return the data type of the variable
        """
        ...

    def getLength(self) -> int:
        """
        Get the length of this variable
        @return the length of the variable
        """
        ...

    def getName(self) -> unicode:
        """
        Get the Name of this variable.
        @return the name of the variable or null if no name has been specified.
        """
        ...

    def getOrdinal(self) -> int:
        """
        Get the parameter ordinal
        @return the ordinal (index) of this parameter within the function signature.
        """
        ...

    def hashCode(self) -> int: ...

    @overload
    def isEquivalent(self, parm: ghidra.program.model.data.ParameterDefinition) -> bool:
        """
        Determine if parm is equivalent to this parameter definition by both ordinal
         and datatype.  Name is not considered relevant.
        @param parm parameter definition to be compared with this parameter definition.
        @return true if the specified parameter definition represents the same parameter
         by ordinal and dataType.
        """
        ...

    @overload
    def isEquivalent(self, variable: ghidra.program.model.listing.Variable) -> bool:
        """
        Determine if a variable corresponds to a parameter which is equivalent to
         this parameter definition by both ordinal and datatype.  Name is not considered
         relevant.
        @param variable variable to be compared with this parameter definition.
        @return true if the specified variable represents the same parameter by ordinal
         and dataType.  False will always be returned if specified variable is
         not a {@link Parameter}.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setComment(self, comment: unicode) -> None:
        """
        Set the comment for this variable
        @param comment the comment
        """
        ...

    def setDataType(self, type: ghidra.program.model.data.DataType) -> None:
        """
        Set the Data Type of this variable.
        @param type dataType the fixed-length datatype of the parameter
        @throws IllegalArgumentException if invalid parameter datatype specified
        """
        ...

    def setName(self, name: unicode) -> None:
        """
        Set the name of this variable.
        @param name the name
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
