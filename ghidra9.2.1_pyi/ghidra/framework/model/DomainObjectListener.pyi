import ghidra.framework.model
import java.lang
import java.util


class DomainObjectListener(java.util.EventListener, object):
    """
    The interface an object must support to be registered with a Domain Object
     and thus be informed of changes to the object.

     NOTE: The DomainObjectChangeEvent is TRANSIENT: it is only valid during the
     life of calls to all the DomainObjectChangeListeners.
    """









    def domainObjectChanged(self, ev: ghidra.framework.model.DomainObjectChangedEvent) -> None:
        """
        Method called when a change is made to the domain object.
        @param ev event containing the change record and type of change that
         was made
        """
        ...

    def equals(self, __a0: object) -> bool: ...

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
