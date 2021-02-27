import java.lang


class DataValidationOptions(object):
    """
    Holds options for controlling how validation is performed when determining whether or not to
     create data structures at a particular location.
    """





    @overload
    def __init__(self):
        """
        Creates a DataValidationOptions object with the default values.
        """
        ...

    @overload
    def __init__(self, validationOptions: ghidra.app.util.datatype.microsoft.DataValidationOptions):
        """
        Copy constructor
        @param validationOptions the data validation options to copy
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setIgnoreDefinedData(self, ignoreDefinedData: bool) -> None:
        """
        Sets whether or not existing defined data should invalidate the creation of new data.
        @param ignoreDefinedData false indicates existing defined data, where the data would be
         created, should cause validation to fail.
        """
        ...

    def setIgnoreInstructions(self, ignoreInstructions: bool) -> None:
        """
        Sets whether or not existing instructions should invalidate the creation of new data.
        @param ignoreInstructions false indicates existing instructions, where the data would be
         created, should cause validation to fail.
        """
        ...

    def setValidateReferredToData(self, validateReferredToData: bool) -> None:
        """
        Sets whether or not to validate follow on data that is referred to by the current
         new structure.
        @param validateReferredToData true indicates follow on data should be validated.
        """
        ...

    def shouldIgnoreDefinedData(self) -> bool:
        """
        An option indicating whether or not existing defined data should make the location invalid
         for new data.
         <br>Default is true.
        @return false if existing defined data should cause the creation of new data to be invalid.
        """
        ...

    def shouldIgnoreInstructions(self) -> bool:
        """
        An option indicating whether or not existing instructions should make the location invalid
         for new data.
         <br>Default is false.
        @return false if existing instructions should cause the creation of new data to be invalid.
        """
        ...

    def shouldValidateReferredToData(self) -> bool:
        """
        An option indicating whether or not to follow references to other data and validate those too.
         If this is set to true then the data is only valid if its referred to data is also valid.
         <br>Default is true.
        @return true if structures should be validated for referred to data.
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
    def ignoreDefinedData(self) -> None: ...  # No getter available.

    @ignoreDefinedData.setter
    def ignoreDefinedData(self, value: bool) -> None: ...

    @property
    def ignoreInstructions(self) -> None: ...  # No getter available.

    @ignoreInstructions.setter
    def ignoreInstructions(self, value: bool) -> None: ...

    @property
    def validateReferredToData(self) -> None: ...  # No getter available.

    @validateReferredToData.setter
    def validateReferredToData(self, value: bool) -> None: ...
