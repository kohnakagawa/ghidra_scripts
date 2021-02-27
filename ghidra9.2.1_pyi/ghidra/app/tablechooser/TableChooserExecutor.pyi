import ghidra.app.tablechooser
import java.lang


class TableChooserExecutor(object):








    def equals(self, __a0: object) -> bool: ...

    def execute(self, rowObject: ghidra.app.tablechooser.AddressableRowObject) -> bool:
        """
        Applies this executors action to the given rowObject.  Return true if the given object
         should be removed from the table.
        @param rowObject the AddressRowObject to be executed upon
        @return true if the rowObject should be removed from the table, false otherwise
        """
        ...

    def getButtonName(self) -> unicode:
        """
        A short name suitable for display in the "apply" button that indicates what the "apply"
         action does.
        @return A short name suitable for display in the "apply" button that indicates what the "apply"
         action does.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

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

    @property
    def buttonName(self) -> unicode: ...
