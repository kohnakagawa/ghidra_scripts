import ghidra.framework.model
import ghidra.framework.task
import java.lang


class GTaskManagerFactory(object):
    """
    Factory class managing a single GTaskManager for an UndoableDomainObject.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getTaskManager(domainObject: ghidra.framework.model.UndoableDomainObject) -> ghidra.framework.task.GTaskManager:
        """
        Returns the one GTaskManager for the domainObject. A new GTaskManager will be created if
         one does not already exist for the domainObject.
        @param domainObject the domainObject for which to get a GTaskManager.
        @return the GTaskManager for the given domainObject.
        """
        ...

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
