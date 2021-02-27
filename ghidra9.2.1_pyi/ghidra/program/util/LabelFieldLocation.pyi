from typing import List
import ghidra.app.util
import ghidra.framework.options
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.model.symbol
import ghidra.program.util
import java.lang


class LabelFieldLocation(ghidra.program.util.CodeUnitLocation):
    """
    The LableFieldLocation class contains specific location information
     within the LABEL field of a CodeUnitLocation object.
    """





    @overload
    def __init__(self):
        """
        Default constructor needed for restoring
         a label field location from XML
        """
        ...

    @overload
    def __init__(self, s: ghidra.program.model.symbol.Symbol):
        """
        Creates a label field location using the specified symbol
         and an index of 0.
        @param s the symbol to use when creating the location
        """
        ...

    @overload
    def __init__(self, s: ghidra.program.model.symbol.Symbol, row: int, charOffset: int):
        """
        Creates a label field location using the specified symbol
         and the specified field index.
        @param s the symbol to use when creating the location
        @param row the row of the symbol.
        @param charOffset the position within the label string for this location
        """
        ...

    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, addr: ghidra.program.model.address.Address, label: unicode):
        """
        Construct a new LabelFieldLocation where the namespace is global, primary is false, and
         the cursor location is at row 0, column 0;
        @param program the program of the location.
        @param addr the address of the location.
        @param label the name of the symbol for this label location.
        """
        ...

    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, addr: ghidra.program.model.address.Address, label: unicode, namespace: ghidra.program.model.symbol.Namespace, row: int):
        """
        Construct a new LabelFieldLocation.<P>
        @param program the program of the location.
        @param addr address of the location; should not be null
        @param label the label String at this location.
        @param namespace the namespace for the label. Null will default to the global namespace.
        @param row the row in list of labels as displayed by the label field.  Only used for
         program location comparison purposes.
        """
        ...

    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, addr: ghidra.program.model.address.Address, componentPath: List[int], label: unicode, namespace: ghidra.program.model.symbol.Namespace, row: int, charOffset: int):
        """
        Construct a new LabelFieldLocation.
        @param program the program of the location
        @param addr address of the location; should not be null
        @param componentPath array of indexes for each nested data component; the
         index is the data component's index within its parent; may be null
        @param label the label String at this location.
        @param row the row in list of labels as displayed by the label field.  Only used for
         program location comparison purposes.
        @param charOffset the column position within the label string for this location.
        """
        ...



    @overload
    def compareTo(self, other: ghidra.program.util.ProgramLocation) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, obj: object) -> bool: ...

    def getAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the address associated with this location.

         <p>
         Note: this may not be the same as the byte address. For example, in a {@link CodeUnit code
         unit} location this may be the minimum address of the code unit that contains the byte
         address.
        """
        ...

    def getByteAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the byte level address associated with this location.
        """
        ...

    def getCharOffset(self) -> int:
        """
        Returns the character offset in the display item at the (row,col)
        @return the character offset in the display item at the (row,col)
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getColumn(self) -> int:
        """
        Returns the column index of the display piece represented by this location. For most
         locations, there is only one display item per row, in which case this value will be 0.
        """
        ...

    def getComponentPath(self) -> List[int]:
        """
        Returns the componentPath for the {@link CodeUnit code unit}. Null will be returned if the
         object is an {@link Instruction} or a top-level {@link Data} object.
        """
        ...

    @staticmethod
    def getLocation(program: ghidra.program.model.listing.Program, saveState: ghidra.framework.options.SaveState) -> ghidra.program.util.ProgramLocation:
        """
        Get the program location for the given program and save state object.
        @param program the program for the location
        @param saveState the state to restore
        @return the restored program location
        """
        ...

    def getName(self) -> unicode:
        """
        Return the label string at this location.
        """
        ...

    def getProgram(self) -> ghidra.program.model.listing.Program:
        """
        Returns the program associated with this location.
        """
        ...

    def getRefAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the "referred to" address if the location is over an address in some field.
        """
        ...

    def getRow(self) -> int:
        """
        Returns the row within the program location.
        @return the row within the program location.
        """
        ...

    def getSymbol(self) -> ghidra.program.model.symbol.Symbol:
        """
        Returns the symbol at this LabelFieldLocation
         NOTE: currently a null symbol will be returned for default thunk functions
        @return the symbol at this LabelFieldLocation or null if symbol lookup fails
        """
        ...

    def getSymbolPath(self) -> ghidra.app.util.SymbolPath:
        """
        Returns the symbol path which corresponds to the label location
        @return symbol path
        """
        ...

    def hashCode(self) -> int: ...

    def isValid(self, p: ghidra.program.model.listing.Program) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def restoreState(self, p: ghidra.program.model.listing.Program, obj: ghidra.framework.options.SaveState) -> None: ...

    def saveState(self, obj: ghidra.framework.options.SaveState) -> None: ...

    def toString(self) -> unicode:
        """
        Returns a String representation of this location.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def name(self) -> unicode: ...

    @property
    def symbol(self) -> ghidra.program.model.symbol.Symbol: ...

    @property
    def symbolPath(self) -> ghidra.app.util.SymbolPath: ...
