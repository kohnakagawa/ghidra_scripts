import ghidra.app.util
import ghidra.app.util.viewer.options
import ghidra.framework.options
import ghidra.program.model.listing
import ghidra.program.model.symbol
import java.awt
import java.lang


class SymbolInspector(object, ghidra.framework.options.OptionsChangeListener):
    """
    Class for coloring symbols.
    """





    @overload
    def __init__(self, options: ghidra.framework.options.ToolOptions, repaintComp: java.awt.Component):
        """
        Constructs a new symbol inspector
        @param options the options from which to get colors
        @param repaintComp the component to repaint when the options change
        """
        ...

    @overload
    def __init__(self, serviceProvider: ghidra.framework.plugintool.ServiceProvider, repaintComp: java.awt.Component):
        """
        Constructs a new symbol inspector
         It uses the tool to get the CATEGORY_BROWSER_DISPLAY options
        @param serviceProvider a service provider for getting services
        @param repaintComp the component to repaint when the options change
        """
        ...



    def dispose(self) -> None:
        """
        Call this when you are done with this inspector and will not use it again.
         Cleans up listeners, etc.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getColor(self, s: ghidra.program.model.symbol.Symbol) -> java.awt.Color:
        """
        Get the color used to render the given symbol.
        @param s symbol to inspect
        @return Color for the symbol
        """
        ...

    def getColorAndStyle(self, s: ghidra.program.model.symbol.Symbol) -> ghidra.app.util.ColorAndStyle:
        """
        Gets the color and style used to render the given symbol.  Calling this method is
         faster than calling {@link #getColor(Symbol)} and {@link #getStyle(Symbol)}
         separately.
        @param s the symbol
        @return the color and style
        """
        ...

    def getOffcutSymbolColor(self) -> java.awt.Color: ...

    def getOffcutSymbolStyle(self) -> int: ...

    def getProgram(self) -> ghidra.program.model.listing.Program:
        """
        Returns the program in use by this inspector; may be null;
        @return the program in use by this inspector; may be null;
        """
        ...

    def getScreenElement(self, s: ghidra.program.model.symbol.Symbol) -> ghidra.app.util.viewer.options.ScreenElement:
        """
        Get the ScreenElement corresponding to the type of the symbol
        @param s symbol to inspect
        @return the screen element
        """
        ...

    def getStyle(self, s: ghidra.program.model.symbol.Symbol) -> int:
        """
        Get the style used to render the given symbol
        @param s symbol to inspect
        @return the style for the symbol
        """
        ...

    def hashCode(self) -> int: ...

    def isBadReferenceSymbol(self, s: ghidra.program.model.symbol.Symbol) -> bool:
        """
        Returns true if symbol is at a non-existent address
        @param s the symbol to check
        @return boolean true if symbol is bad
        """
        ...

    def isDataSymbol(self, s: ghidra.program.model.symbol.Symbol) -> bool:
        """
        Returns true if the symbol is on a data item.
        @param s the symbol to check
        @return boolean true if s is a data symbol
        """
        ...

    def isDeadCodeSymbol(self, s: ghidra.program.model.symbol.Symbol) -> bool:
        """
        Returns true if the symbol is on "dead" code
        @param s the symbol to check
        @return boolean true if the symbol is on dead code
        """
        ...

    def isEntryPointSymbol(self, s: ghidra.program.model.symbol.Symbol) -> bool:
        """
        Checks if the given symbol is at an external entry point
        @param s the symbol to check
        @return boolean true if the symbol is at an external entry point address.
        """
        ...

    def isExternalSymbol(self, s: ghidra.program.model.symbol.Symbol) -> bool: ...

    def isFunctionSymbol(self, s: ghidra.program.model.symbol.Symbol) -> bool:
        """
        Checks if the symbol is at a function
        @param s the symbol to check.
        @return boolean true if there is a function at the symbol's address.
        """
        ...

    def isGlobalSymbol(self, s: ghidra.program.model.symbol.Symbol) -> bool:
        """
        Checks if the symbol is global or local
        @param s the symbol to check
        @return boolean true if the symbol is global, false if the symbol is
         local.
        """
        ...

    def isInstructionSymbol(self, s: ghidra.program.model.symbol.Symbol) -> bool:
        """
        Checks if the symbol is at or inside an instruction
        @param s the symbol to check
        @return boolean true if the symbol is on an instruction
        """
        ...

    def isLocalSymbol(self, s: ghidra.program.model.symbol.Symbol) -> bool:
        """
        Checks if the symbol is local
        @param s the symbol to check
        @return boolean true if the symbol is local, false if it is global
        """
        ...

    def isNonPrimarySymbol(self, s: ghidra.program.model.symbol.Symbol) -> bool:
        """
        Checks if the symbol is not a primary symbol
        @param s the symbol to check.
        @return boolean true if the symbol is non-primary
        """
        ...

    def isOffcutSymbol(self, s: ghidra.program.model.symbol.Symbol) -> bool:
        """
        Checks if the symbol is offcut
        @param s the symbol to check
        @return boolean true if the symbol is offcut
        """
        ...

    def isPrimarySymbol(self, s: ghidra.program.model.symbol.Symbol) -> bool:
        """
        returns true if the symbol is primary
        @param s the symbol to check
        @return boolean true if the symbol is primary
        """
        ...

    def isSubroutineSymbol(self, s: ghidra.program.model.symbol.Symbol) -> bool:
        """
        Checks if the symbol is at the beginning of a subroutine.
        @param s the symbol to check
        @return boolean true if the symbol is at the beginning of a subroutine.
        """
        ...

    def isVariableSymbol(self, s: ghidra.program.model.symbol.Symbol) -> bool:
        """
        Checks if the symbol is a function variable
        @param s the symbol to check
        @return true if s is a function variable symbol
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def optionsChanged(self, options: ghidra.framework.options.ToolOptions, name: unicode, oldValue: object, newValue: object) -> None: ...

    def setProgram(self, p: ghidra.program.model.listing.Program) -> None:
        """
        Associates a program with this symbol inspector
        @param p the program for inspecting symbols
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
    def offcutSymbolColor(self) -> java.awt.Color: ...

    @property
    def offcutSymbolStyle(self) -> int: ...

    @property
    def program(self) -> ghidra.program.model.listing.Program: ...

    @program.setter
    def program(self, value: ghidra.program.model.listing.Program) -> None: ...
