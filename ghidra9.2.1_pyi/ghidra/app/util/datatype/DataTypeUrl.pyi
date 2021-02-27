import ghidra.app.services
import ghidra.program.model.data
import ghidra.util
import java.lang


class DataTypeUrl(object):
    """
    A class to produce and parse URLs of the form:

     where the first number is the ID of the DataTypeManager and the second number is
     the DataType ID.
    """





    @overload
    def __init__(self, url: unicode):
        """
        Constructs a url from the given url string
        @param url the url
        @throws IllegalArgumentException if the url does not match the expected {@link #URL_PATTERN}
                 or if there is an issue parsing the id within the given url
        """
        ...

    @overload
    def __init__(self, dt: ghidra.program.model.data.DataType):
        """
        Constructs a url from the given data type
        @param dt the data type; cannot be null
        """
        ...



    def equals(self, obj: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDataType(self, service: ghidra.app.services.DataTypeManagerService) -> ghidra.program.model.data.DataType:
        """
        Uses the given service and its {@link DataTypeManager}s to find the data type
         represented by this url
        @param service the service
        @return the data type; null if there was an error restoring the type, such as if the
                 parent {@link DataTypeManager} has been closed
        """
        ...

    def getDataTypeId(self) -> ghidra.util.UniversalID: ...

    def getDataTypeManagerId(self) -> ghidra.util.UniversalID: ...

    def getDataTypeName(self) -> unicode: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def dataTypeId(self) -> ghidra.util.UniversalID: ...

    @property
    def dataTypeManagerId(self) -> ghidra.util.UniversalID: ...

    @property
    def dataTypeName(self) -> unicode: ...
