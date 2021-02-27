from typing import List
import ghidra.program.database
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class TreeManager(object, ghidra.program.database.ManagerDB):
    """
    Manage the set of trees in the program.
    """

    DEFAULT_TREE_NAME: unicode = u'Program Tree'



    def __init__(self, handle: db.DBHandle, errHandler: db.util.ErrorHandler, addrMap: ghidra.program.database.map.AddressMap, openMode: int, lock: ghidra.util.Lock, monitor: ghidra.util.task.TaskMonitor):
        """
        Construct a new TreeManager.
        @param handle database handle
        @param errHandler error handler
        @param addrMap map to convert addresses to longs and longs to addresses
        @param openMode the open mode for the program.
        @param lock the program synchronization lock
        @param monitor Task monitor for upgrading
        @throws IOException if a database io error occurs.
        @throws VersionException if the database version is different from the expected version
        """
        ...



    def addMemoryBlock(self, name: unicode, range: ghidra.program.model.address.AddressRange) -> None:
        """
        Add a memory block with the given range.
        """
        ...

    def createRootModule(self, treeName: unicode) -> ghidra.program.model.listing.ProgramModule:
        """
        Create a new tree with given name.
        @param treeName name of the tree (not the root module)
        @return root module for the new tree
        @throws DuplicateNameException if there is already tree named
         treeName
        """
        ...

    def deleteAddressRange(self, startAddr: ghidra.program.model.address.Address, endAddr: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Remove a memory block with the given range
        @throws CancelledException
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDefaultRootModule(self) -> ghidra.program.model.listing.ProgramModule:
        """
        Returns the root module for the default program tree. The default tree is the oldest tree.
        @return the root module for the default program tree. The default tree is the oldest tree.
        """
        ...

    @overload
    def getFragment(self, treeName: unicode, name: unicode) -> ghidra.program.model.listing.ProgramFragment:
        """
        Get the fragment with the given name that is in the tree identified
         by the treeName.
        @param treeName name of the tree
        @param name name of fragment to look for
        @return null if there is no fragment with the given name in the tree
        """
        ...

    @overload
    def getFragment(self, treeName: unicode, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.ProgramFragment:
        """
        Get the fragment that contains the given address within the tree
         identified by the treeName.
        @param treeName name of the tree
        @param addr address contained within some fragment
        @return fragment containing addr, or null if addr does not
         exist in memory
        """
        ...

    def getModule(self, treeName: unicode, name: unicode) -> ghidra.program.model.listing.ProgramModule:
        """
        Get the module with the given name that is in the tree identified
         by the treeName.
        @param treeName name of the tree
        @param name module name to look for
        @return null if there is no module with the given name in the tree
        """
        ...

    @overload
    def getRootModule(self, treeID: long) -> ghidra.program.model.listing.ProgramModule:
        """
        Get the root module for the tree that has the given ID.
        @param treeID ID of the tree
        @return root module
        """
        ...

    @overload
    def getRootModule(self, treeName: unicode) -> ghidra.program.model.listing.ProgramModule:
        """
        Get the root module of the tree with the given name.
        @return root module, or null if there is no tree with the
         given name
        """
        ...

    def getTreeNames(self) -> List[unicode]:
        """
        Get the names of all the trees in the program.
        @return sorted array of tree names
        """
        ...

    def hashCode(self) -> int: ...

    def imageBaseChanged(self, commit: bool) -> None: ...

    def invalidateCache(self, all: bool) -> None: ...

    def moveAddressRange(self, fromAddr: ghidra.program.model.address.Address, toAddr: ghidra.program.model.address.Address, length: long, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Move a memory block to new place.
        @param fromAddr old place
        @param toAddr new place
        @param length the length of the address range to move
        @param monitor the current task monitor
        @throws AddressOverflowException if an address overflow occurs.
        @throws CancelledException if the task is cancelled.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def programReady(self, openMode1: int, currentRevision: int, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        @see ghidra.program.database.ManagerDB#programReady(int, int, ghidra.util.task.TaskMonitor)
        """
        ...

    def removeTree(self, treeName: unicode) -> bool:
        """
        Remove the tree with the given name.
        @return true if the tree was removed
        """
        ...

    def renameTree(self, oldName: unicode, newName: unicode) -> None:
        """
        Rename the tree to the new name. This method has no effect on the
         name of the root module.
        @param oldName old name of root module
        @param newName new name for root module
        @throws DuplicateNameException if newName exists as the name
         for another root
        """
        ...

    def setProgram(self, program: ghidra.program.database.ProgramDB) -> None:
        """
        Set the program.
        """
        ...

    def setProgramName(self, oldName: unicode, newName: unicode) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def defaultRootModule(self) -> ghidra.program.model.listing.ProgramModule: ...

    @property
    def program(self) -> None: ...  # No getter available.

    @program.setter
    def program(self, value: ghidra.program.database.ProgramDB) -> None: ...

    @property
    def treeNames(self) -> List[unicode]: ...
