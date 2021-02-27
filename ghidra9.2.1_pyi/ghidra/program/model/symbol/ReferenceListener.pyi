import ghidra.program.model.symbol
import java.lang


class ReferenceListener(object):
    """
    Interface to define methods that are called when references are
     added or removed.
    """









    def equals(self, __a0: object) -> bool: ...

    def externalReferenceAdded(self, ref: ghidra.program.model.symbol.Reference) -> None:
        """
        Notification that the given external reference has been added.
        @param ref the external reference that was added.
        """
        ...

    def externalReferenceNameChanged(self, ref: ghidra.program.model.symbol.Reference) -> None:
        """
        Notification that the external program name in the reference
         has changed.
        @param ref the external reference with its new external name.
        """
        ...

    def externalReferenceRemoved(self, ref: ghidra.program.model.symbol.Reference) -> None:
        """
        Notification that the given external reference has been removed.
        @param ref the external reference that was removed.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def memReferenceAdded(self, ref: ghidra.program.model.symbol.Reference) -> None:
        """
        Notification that the given memory reference has been added.
        @param ref the reference that was added.
        """
        ...

    def memReferencePrimaryRemoved(self, ref: ghidra.program.model.symbol.Reference) -> None:
        """
        Notification that the given memory reference is no longer the primary
         reference.
        @param ref the reference that was primary but now is not.
        """
        ...

    def memReferencePrimarySet(self, ref: ghidra.program.model.symbol.Reference) -> None:
        """
        Notification that the given memory reference has been set as
         the primary reference.
        @param ref the reference that is now primary.
        """
        ...

    def memReferenceRemoved(self, ref: ghidra.program.model.symbol.Reference) -> None:
        """
        Notification that the given memory reference has bee removed.
        @param ref the reference that was removed.
        """
        ...

    def memReferenceTypeChanged(self, newRef: ghidra.program.model.symbol.Reference, oldRef: ghidra.program.model.symbol.Reference) -> None:
        """
        Notification that the reference type on the given memory reference
         has changed.
        @param newRef the reference with the new reference type.
        @param oldRef the reference with the old reference type.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def stackReferenceAdded(self, ref: ghidra.program.model.symbol.Reference) -> None:
        """
        Notification that the given stack reference has been added.
        @param ref the stack reference that was added.
        """
        ...

    def stackReferenceRemoved(self, ref: ghidra.program.model.symbol.Reference) -> None:
        """
        Notification tbat the given stack reference has been removed.
        @param ref The stack reference that was removed
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
