from typing import List
import ghidra.app.util.bin.format.ne
import java.lang


class EntryTableBundle(object):
    """
    A class to represent a new-executable entry table bundle.
    """

    CONSTANT: int = -2
    MOVEABLE: int = -1
    UNUSED: int = 0







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getCount(self) -> int:
        """
        Returns the number of entries in bundle.
        @return the number of entries in bundle
        """
        ...

    def getEntryPoints(self) -> List[ghidra.app.util.bin.format.ne.EntryPoint]:
        """
        Returns the array of entry points in this bundle.
        @return the array of entry points in this bundle
        """
        ...

    def getType(self) -> int:
        """
        Returns the type of the bundle. For example,
         MOVEABLE, CONSTANT, or segment index.
        @return the type of the bundle
        """
        ...

    def hashCode(self) -> int: ...

    def isConstant(self) -> bool:
        """
        Returns true if this bundle is constant.
        @return true if this bundle is constant
        """
        ...

    def isMoveable(self) -> bool:
        """
        Returns true if this bundle is moveable.
        @return true if this bundle is moveable
        """
        ...

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
    def constant(self) -> bool: ...

    @property
    def count(self) -> int: ...

    @property
    def entryPoints(self) -> List[ghidra.app.util.bin.format.ne.EntryPoint]: ...

    @property
    def moveable(self) -> bool: ...

    @property
    def type(self) -> int: ...
