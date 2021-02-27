import java.lang


class DataApplyOptions(object):
    """
    Holds options for the commands for creating new data structures.
    """





    @overload
    def __init__(self):
        """
        Creates an DataApplyOptions object with the default values.
        """
        ...

    @overload
    def __init__(self, dataApplyOptions: ghidra.app.util.datatype.microsoft.DataApplyOptions):
        """
        Copy constructor
        @param dataApplyOptions the data apply options to copy
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setClearDefinedData(self, clearDefinedData: bool) -> None:
        """
        Sets whether or not to clear existing defined data in order to create new data.
        @param clearDefinedData true indicates existing defined data should be cleared to create
         the new data.
        """
        ...

    def setClearInstructions(self, clearInstructions: bool) -> None:
        """
        Sets whether or not to clear existing instructions in order to create new data.
        @param clearInstructions true indicates existing instructions should be cleared to create
         the new data.
        """
        ...

    def setCreateBookmarks(self, createBookmarks: bool) -> None:
        """
        Sets whether or not to create bookmarks for problems encountered while trying to create
         an new structure or information associated with it.
        @param createBookmarks true indicates error bookmarks should be created.
        """
        ...

    def setCreateComments(self, createComments: bool) -> None:
        """
        Sets whether or not to create comments for problems encountered while trying to create
         a new structure or information associated with it.
        @param createComments true indicates comments for the data should be created.
        """
        ...

    def setCreateFunction(self, createFunction: bool) -> None:
        """
        Sets whether or not to disassemble and create a function that is referred to
         by the current new structure.
        @param createFunction true indicates a function should be created.
        """
        ...

    def setCreateLabel(self, createLabel: bool) -> None:
        """
        Sets whether or not to create labels for follow on data or a function that is referred to
         by the current new structure.
        @param createLabel true indicates a label should be created.
        """
        ...

    def setFollowData(self, followData: bool) -> None:
        """
        Sets whether or not to create follow on data that is referred to by the new structure.
        @param followData true indicates follow on data should be created.
        """
        ...

    def shouldClearDefinedData(self) -> bool:
        """
        An option indicating whether or not to clear existing defined data in order to create
         new data.
         <br>Default is false.
        @return true if existing defined data should be cleared to create the new data.
        """
        ...

    def shouldClearInstructions(self) -> bool:
        """
        An option indicating whether or not to clear existing instructions in order to create
         new data.
         <br>Default is false.
        @return true if existing instructions should be cleared to create the new data.
        """
        ...

    def shouldCreateBookmarks(self) -> bool:
        """
        An option indicating whether or not to create bookmarks indicating any problems that
         occurred while creating the current structure or information associated with it.
         <br>Default is true.
        @return true if error bookmarks should be created.
        """
        ...

    def shouldCreateComments(self) -> bool:
        """
        An option indicating whether or not to create comments indicating any problems that
         occurred while creating the data or information associated with it.
         <br>Default is true.
        @return true if error comments should be created.
        """
        ...

    def shouldCreateFunction(self) -> bool:
        """
        An option indicating whether or not to disassemble and create a function that is referred
         to by your current structure.
         <br>Default is true.
        @return true if referred to functions should be created.
        """
        ...

    def shouldCreateLabel(self) -> bool:
        """
        An option indicating whether or not to create a label for the new data or for a
         referred to data or function.
         <br>Default is true.
        @return true if a label should be created for this data or for referred to structures
         and functions.
        """
        ...

    def shouldFollowData(self) -> bool:
        """
        An option indicating whether or not to create data that is referred to by the data structure.
         <br>Default is true.
        @return true if structures should be created for referred to data.
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
    def clearDefinedData(self) -> None: ...  # No getter available.

    @clearDefinedData.setter
    def clearDefinedData(self, value: bool) -> None: ...

    @property
    def clearInstructions(self) -> None: ...  # No getter available.

    @clearInstructions.setter
    def clearInstructions(self, value: bool) -> None: ...

    @property
    def createBookmarks(self) -> None: ...  # No getter available.

    @createBookmarks.setter
    def createBookmarks(self, value: bool) -> None: ...

    @property
    def createComments(self) -> None: ...  # No getter available.

    @createComments.setter
    def createComments(self, value: bool) -> None: ...

    @property
    def createFunction(self) -> None: ...  # No getter available.

    @createFunction.setter
    def createFunction(self, value: bool) -> None: ...

    @property
    def createLabel(self) -> None: ...  # No getter available.

    @createLabel.setter
    def createLabel(self, value: bool) -> None: ...

    @property
    def followData(self) -> None: ...  # No getter available.

    @followData.setter
    def followData(self, value: bool) -> None: ...
