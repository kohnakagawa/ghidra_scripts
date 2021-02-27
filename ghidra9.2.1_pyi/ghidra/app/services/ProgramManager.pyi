from typing import List
import ghidra.framework.model
import ghidra.program.model.address
import ghidra.program.model.listing
import java.awt
import java.lang
import java.net


class ProgramManager(object):
    """
    Service for managing programs. Multiple programs may be open in a tool,
     but only one is active at any given time.
    """

    OPEN_CURRENT: int = 1
    OPEN_HIDDEN: int = 0
    OPEN_VISIBLE: int = 2







    def closeAllPrograms(self, ignoreChanges: bool) -> bool:
        """
        Closes all open programs in this tool.  If this tool is the only tool with a program
         open and that program has changes, then the user will be prompted to close each such file.
         (Providing the ignoreChanges flag is false)
        @param ignoreChanges if true, the programs will be closed without saving changes.
        @return true if all programs were closed. Returns false if the user canceled the close
         while being prompted to save.
        """
        ...

    def closeOtherPrograms(self, ignoreChanges: bool) -> bool:
        """
        Closes all open programs in this tool except the current program.
         If this tool is the only tool with a program open and that program has changes,
         then the user will be prompted to close each such file.
         (Providing the ignoreChanges flag is false)
        @param ignoreChanges if true, the programs will be closed without saving changes.
        @return true if all other programs were closed. Returns false if the user canceled the close
         while being prompted to save.
        """
        ...

    @overload
    def closeProgram(self) -> bool:
        """
        Closes the currently active program
        @return true if the close is successful.
         false if the close fails or if there is no program currently active.
        """
        ...

    @overload
    def closeProgram(self, program: ghidra.program.model.listing.Program, ignoreChanges: bool) -> bool:
        """
        Closes the given program with the option of saving any changes.  The exact behavior of
         this method depends on several factors.  First of all, if any other tool has this program
         open, then the program is closed for this tool only and the user is not prompted to
         save the program regardless of the ignoreChanges flag.  Otherwise, if ignoreChanges is
         false and changes have been made, the user is prompted to save the program.
        @param program the program to close.
        @param ignoreChanges if true, the program is closed without saving any changes.
        @return true if the program was closed. Returns false if the user canceled the close
         while being prompted to save. Also returns false if the program passed in as a parameter
         is null.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getAllOpenPrograms(self) -> List[ghidra.program.model.listing.Program]:
        """
        Returns a list of all open program.s
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getCurrentProgram(self) -> ghidra.program.model.listing.Program:
        """
        Return the program that is currently active.
        @return may return null if no program is open
        """
        ...

    def getProgram(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Program:
        """
        Returns the first program in the list of open programs that contains the given address.
         Programs are searched in the order they were opened within a given priority.
         Program are initially opened with the PRIORITY_NORMAL priority, but can be set to have
         PRIORITY_HIGH or PRIORITY_LOW.
        @param addr the address for which to search.
        @return the first program that can be found to contain the given address.
        """
        ...

    def hashCode(self) -> int: ...

    def isLocked(self) -> bool:
        """
        Returns true if program manager
        @return
        """
        ...

    def isVisible(self, program: ghidra.program.model.listing.Program) -> bool:
        """
        Returns true if the specified program is open and considiered visible to
         the user.
        @param program
        @return true if the specified program is open and considiered visible to
         the user
        """
        ...

    def lockDown(self, state: bool) -> None:
        """
        Allows program manager state to be locked/unlocked.
         While locked, the program manager will not support opening
         additional programs.
        @param state locked if true, unlocked if false
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def openProgram(self, domainFile: ghidra.framework.model.DomainFile) -> ghidra.program.model.listing.Program:
        """
        Open the program for the given domainFile.  Once open it will
         become the active program.
        @param domainFile domain file that has the program
        @return null if the user canceled the "open" for the new program
        """
        ...

    @overload
    def openProgram(self, program: ghidra.program.model.listing.Program) -> None:
        """
        Opens the program to the tool.  In this case the program is already open, but this tool
         may not have it registered as open. The program is made the active program.
        @param program the program to register as open with the tool.
        """
        ...

    @overload
    def openProgram(self, df: ghidra.framework.model.DomainFile, version: int) -> ghidra.program.model.listing.Program:
        """
        Opens the specified version of the program represented by the given DomainFile. This
         method should be used for shared DomainFiles. The newly opened file will be made the
         active program.
        @param df the DomainFile to open
        @param version the version of the Program to open
        @return the opened program or null if the given version does not exist.
        """
        ...

    @overload
    def openProgram(self, program: ghidra.program.model.listing.Program, state: int) -> None:
        """
        Open the specified program in te tool.
        @param program
        @param state initial open state (OPEN_HIDDEN, OPEN_CURRENT, OPEN_VISIBLE).
         The visibility states will be ignored if the program is already open.
        """
        ...

    @overload
    def openProgram(self, ghidraURL: java.net.URL, state: int) -> ghidra.program.model.listing.Program:
        """
        Open the program corresponding to the given url.  Once open it will
         become
        @param ghidraURL valid server-based program URL
        @param state initial open state (OPEN_HIDDEN, OPEN_CURRENT, OPEN_VISIBLE).
         The visibility states will be ignored if the program is already open.
        @return null if the user canceled the "open" for the new program or an error
         occurred and was displayed.
        @see GhidraURL
        """
        ...

    @overload
    def openProgram(self, program: ghidra.program.model.listing.Program, current: bool) -> None:
        """
        Opens the program to the tool.  In this case the program is already open, but this tool
         may not have it registered as open. The program is made the active program.
        @param program the program to register as open with the tool.
        @param current if true, the program is made the current active program. If false, then
         the program is made active only if it the first open program in the tool.
        @deprecated use openProgram(Program program, int state) instead.
        """
        ...

    @overload
    def openProgram(self, domainFile: ghidra.framework.model.DomainFile, dialogParent: java.awt.Component) -> ghidra.program.model.listing.Program: ...

    @overload
    def openProgram(self, domainFile: ghidra.framework.model.DomainFile, version: int, state: int) -> ghidra.program.model.listing.Program:
        """
        Open the program for the given domainFile
        @param domainFile domain file that has the program
        @param version the version of the Program to open. Specify
         DomainFile.DEFAULT_VERSION for file update mode.
        @param state initial open state (OPEN_HIDDEN, OPEN_CURRENT, OPEN_VISIBLE).
         The visibility states will be ignored if the program is already open.
        @return null if the user canceled the "open" for the new program or an error
         occurred and was displayed.
        """
        ...

    def releaseProgram(self, program: ghidra.program.model.listing.Program, persistentOwner: object) -> None:
        """
        Release the persistent ownership of a program.
         The program will automatically be closed if it is hidden or was
         marked as temporary.  If any of these closures corresponds to a
         program with changes the user will be given an opportunity to
         save or keep the program open.
         If persistentOwner is not the correct owner, the method will
         have no affect.
        @param program
        @param persistentOwner
        """
        ...

    def setCurrentProgram(self, p: ghidra.program.model.listing.Program) -> None:
        """
        Sets the given program to be the current active program in the tool.
        @param p the program to make active.
        """
        ...

    def setPersistentOwner(self, program: ghidra.program.model.listing.Program, owner: object) -> bool:
        """
        Establish a persistent owner on an open program.
         This will cause the program manager to simply make a program
         hidden if it is closed.
        @param program
        @param owner
        @return true if program is open and another object is not already the owner,
         or the specified owner is already the owner.
        @see #releaseProgram(Program, Object)
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
    def allOpenPrograms(self) -> List[ghidra.program.model.listing.Program]: ...

    @property
    def currentProgram(self) -> ghidra.program.model.listing.Program: ...

    @currentProgram.setter
    def currentProgram(self, value: ghidra.program.model.listing.Program) -> None: ...

    @property
    def locked(self) -> bool: ...
