from typing import List
import ghidra.program.model.data
import java.io
import java.lang


class DataTypeConflictException(java.lang.RuntimeException):
    """
    Exception thrown when an attempt is made to add a data type to a category
     and the category has a data type by that name but the types do not
     match.
    """





    @overload
    def __init__(self):
        """
        Construct a new DataTypeConflictException with no message
        """
        ...

    @overload
    def __init__(self, msg: unicode):
        """
        Construct a new DataTypeConflictException with the given message
        @param msg the exception message
        """
        ...

    @overload
    def __init__(self, dt1: ghidra.program.model.data.DataType, dt2: ghidra.program.model.data.DataType):
        """
        Construct a new DataTypeConflictException with the given datatypes.
         The message will indicate there is a conflict between the two data types.
        @param dt1 the first of the two conflicting data types.
         (The new data type.)
        @param dt2 the second of the two conflicting data types.
         (The existing data type.)
        """
        ...



    def addSuppressed(self, __a0: java.lang.Throwable) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def fillInStackTrace(self) -> java.lang.Throwable: ...

    def getCause(self) -> java.lang.Throwable: ...

    def getClass(self) -> java.lang.Class: ...

    def getConflictingDataTypes(self) -> List[ghidra.program.model.data.DataType]:
        """
        Returns the conflicting data types in a Data Type array of size 2.
         The first entry is the first data type in conflict.
         The second entry is the second data type in conflict.
         <P>Note: These values can be null. They are only known if this
         object was created using the constructor that has the conflicting
         data types as parameters.
        @return the two conflicting data types or nulls.
        """
        ...

    def getLocalizedMessage(self) -> unicode: ...

    def getMessage(self) -> unicode: ...

    def getStackTrace(self) -> List[java.lang.StackTraceElement]: ...

    def getSuppressed(self) -> List[java.lang.Throwable]: ...

    def hashCode(self) -> int: ...

    def initCause(self, __a0: java.lang.Throwable) -> java.lang.Throwable: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def printStackTrace(self) -> None: ...

    @overload
    def printStackTrace(self, __a0: java.io.PrintStream) -> None: ...

    @overload
    def printStackTrace(self, __a0: java.io.PrintWriter) -> None: ...

    def setStackTrace(self, __a0: List[java.lang.StackTraceElement]) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def conflictingDataTypes(self) -> List[ghidra.program.model.data.DataType]: ...
