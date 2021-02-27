from typing import List
import ghidra.program.model.listing
import ghidra.program.util
import java.io
import java.lang


class GroupPath(object, java.io.Serializable):
    """
    The GroupPath is a class to represent a unique path in a tree for a Group.
    """





    @overload
    def __init__(self, groupName: unicode):
        """
        Construct a new GroupPath that is only a single level.
        @param groupName name of group
        """
        ...

    @overload
    def __init__(self, groupNames: List[unicode]):
        """
        Construct a new GroupPath with the given names.
        @param groupNames group names. The first name is the oldest ancestor
         and the last name is the youngest descendant in the path.
        """
        ...



    def equals(self, obj: object) -> bool:
        """
        @see java.lang.Object#equals(Object)
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getGroup(self, program: ghidra.program.model.listing.Program, treeName: unicode) -> ghidra.program.model.listing.Group:
        """
        Get the Group for this group path object.
        @return null if there is no group with the name in this
         group path.
        """
        ...

    def getLastPathComponent(self) -> unicode:
        """
        Get the last name in the path.
        @return String
        """
        ...

    def getParentPath(self) -> ghidra.program.util.GroupPath:
        """
        Get the parent path for this group.
        """
        ...

    def getPath(self) -> List[unicode]:
        """
        Return the array of names that make up this group's path.
        """
        ...

    def getPathComponent(self, index: int) -> unicode:
        """
        Get the name at the given index into this group's path.
        @param index the index in the group path
        """
        ...

    def getPathCount(self) -> int:
        """
        Get the number of names (levels) that make up this path.
        """
        ...

    def hashCode(self) -> int:
        """
        @see java.lang.Object#hashCode()
        """
        ...

    def isDescendant(self, grpPath: ghidra.program.util.GroupPath) -> bool:
        """
        Return true if the indicated group path is a descendent of this group path.
        @param grpPath the group path
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def pathByAddingChild(self, child: unicode) -> ghidra.program.util.GroupPath:
        """
        Create a new GroupPath object by adding the given
         child name to this group path.
        @param child name of child to add to path
        """
        ...

    def toString(self) -> unicode:
        """
        Returns a string representation of this group path.
        """
        ...

    def updateGroupPath(self, oldname: unicode, newname: unicode) -> None:
        """
        Update this group path with the new group name wherever the old group name is found.
        @param oldname old name
        @param newname new name
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def lastPathComponent(self) -> unicode: ...

    @property
    def parentPath(self) -> ghidra.program.util.GroupPath: ...

    @property
    def path(self) -> List[unicode]: ...

    @property
    def pathCount(self) -> int: ...
