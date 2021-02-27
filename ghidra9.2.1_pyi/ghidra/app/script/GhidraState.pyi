import ghidra.app.script
import ghidra.framework.model
import ghidra.framework.plugintool
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.util
import java.lang
import java.util


class GhidraState(object):
    """
    Represents the current state of a Ghidra tool
    """





    @overload
    def __init__(self, state: ghidra.app.script.GhidraState): ...

    @overload
    def __init__(self, tool: ghidra.framework.plugintool.PluginTool, project: ghidra.framework.model.Project, program: ghidra.program.model.listing.Program, location: ghidra.program.util.ProgramLocation, selection: ghidra.program.util.ProgramSelection, highlight: ghidra.program.util.ProgramSelection):
        """
        Constructs a new Ghidra state.
        @param tool the current tool
        @param project the current project
        @param program the current program
        @param location the current location
        @param selection the current selection
        @param highlight the current highlight
        """
        ...



    @overload
    def addEnvironmentVar(self, name: unicode, value: long) -> None: ...

    @overload
    def addEnvironmentVar(self, name: unicode, value: int) -> None: ...

    @overload
    def addEnvironmentVar(self, name: unicode, value: int) -> None: ...

    @overload
    def addEnvironmentVar(self, name: unicode, value: int) -> None: ...

    @overload
    def addEnvironmentVar(self, name: unicode, value: float) -> None: ...

    @overload
    def addEnvironmentVar(self, name: unicode, value: float) -> None: ...

    @overload
    def addEnvironmentVar(self, name: unicode, value: object) -> None: ...

    def addParameter(self, key: unicode, label: unicode, type: int, defaultValue: object) -> None: ...

    def displayParameterGatherer(self, title: unicode) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getCurrentAddress(self) -> ghidra.program.model.address.Address:
        """
        @return the address of the current location
        """
        ...

    def getCurrentHighlight(self) -> ghidra.program.util.ProgramSelection:
        """
        @return the currently highlighted selection
        """
        ...

    def getCurrentLocation(self) -> ghidra.program.util.ProgramLocation:
        """
        @return the current location
        """
        ...

    def getCurrentProgram(self) -> ghidra.program.model.listing.Program:
        """
        Returns the current program.
        @return the current program
        """
        ...

    def getCurrentSelection(self) -> ghidra.program.util.ProgramSelection:
        """
        @return the current selection
        """
        ...

    def getEnvironmentNames(self) -> java.util.Set: ...

    def getEnvironmentVar(self, name: unicode) -> object: ...

    def getParamPanel(self) -> ghidra.app.script.GatherParamPanel: ...

    def getProject(self) -> ghidra.framework.model.Project:
        """
        Returns the current project.
        @return the current project
        """
        ...

    def getTool(self) -> ghidra.framework.plugintool.PluginTool:
        """
        Returns the current tool.
        @return the current tool
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeEnvironmentVar(self, name: unicode) -> None: ...

    def setCurrentAddress(self, address: ghidra.program.model.address.Address) -> None:
        """
        If it differs, set the current location to the given address and fire a {@link ProgramLocationPluginEvent}.
        @param address the address
        """
        ...

    def setCurrentHighlight(self, highlight: ghidra.program.util.ProgramSelection) -> None:
        """
        Set the currently highlighted selection and fire a {@link ProgramHighlightPluginEvent}.
        @param highlight the selection
        """
        ...

    def setCurrentLocation(self, location: ghidra.program.util.ProgramLocation) -> None:
        """
        If it differs, set the current location and fire a {@link ProgramLocationPluginEvent}.
        @param location
        """
        ...

    def setCurrentProgram(self, program: ghidra.program.model.listing.Program) -> None:
        """
        Sets the current program.
        @param program the new program object
        """
        ...

    def setCurrentSelection(self, selection: ghidra.program.util.ProgramSelection) -> None:
        """
        Set the current selection and fire a {@link ProgramSelectionPluginEvent}.
        @param selection the selection
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
    def currentAddress(self) -> ghidra.program.model.address.Address: ...

    @currentAddress.setter
    def currentAddress(self, value: ghidra.program.model.address.Address) -> None: ...

    @property
    def currentHighlight(self) -> ghidra.program.util.ProgramSelection: ...

    @currentHighlight.setter
    def currentHighlight(self, value: ghidra.program.util.ProgramSelection) -> None: ...

    @property
    def currentLocation(self) -> ghidra.program.util.ProgramLocation: ...

    @currentLocation.setter
    def currentLocation(self, value: ghidra.program.util.ProgramLocation) -> None: ...

    @property
    def currentProgram(self) -> ghidra.program.model.listing.Program: ...

    @currentProgram.setter
    def currentProgram(self, value: ghidra.program.model.listing.Program) -> None: ...

    @property
    def currentSelection(self) -> ghidra.program.util.ProgramSelection: ...

    @currentSelection.setter
    def currentSelection(self, value: ghidra.program.util.ProgramSelection) -> None: ...

    @property
    def environmentNames(self) -> java.util.Set: ...

    @property
    def paramPanel(self) -> ghidra.app.script.GatherParamPanel: ...

    @property
    def project(self) -> ghidra.framework.model.Project: ...

    @property
    def tool(self) -> ghidra.framework.plugintool.PluginTool: ...
