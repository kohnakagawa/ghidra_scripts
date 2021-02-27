import ghidra.app.util.html
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.program.model.symbol
import java.lang


class ToolTipUtils(object):
    """
    A utility class that creates tool tip text for given data types.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getHTMLRepresentation(dataType: ghidra.program.model.data.DataType) -> ghidra.app.util.html.HTMLDataTypeRepresentation:
        """
        Return dataType details as HTML.
        @param dataType the dataType to be represented
        @return dataType details formatted as HTML
        """
        ...

    @overload
    @staticmethod
    def getToolTipText(dataType: ghidra.program.model.data.DataType) -> unicode:
        """
        Examines the give <code>dataType</code> and creates a tool tip for it,
         depending upon its actual class type.
        @param dataType The data type from which a tool tip will be
                 created.
        @return tool tip text for the given data type.
        """
        ...

    @overload
    @staticmethod
    def getToolTipText(function: ghidra.program.model.listing.Function, includeSymbolDetails: bool) -> unicode:
        """
        Return an HTML formatted rendering of a function
        @param function the function
        @param includeSymbolDetails true to include details of the symbol
        @return tool tip text for the given function
        """
        ...

    @overload
    @staticmethod
    def getToolTipText(extLoc: ghidra.program.model.symbol.ExternalLocation, includeSymbolDetails: bool) -> unicode:
        """
        Return an HTML formatted rendering of an external location/function.
        @param extLoc the location
        @param includeSymbolDetails true to include details of the symbol
        @return tool tip text for the given external location/function
        """
        ...

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
