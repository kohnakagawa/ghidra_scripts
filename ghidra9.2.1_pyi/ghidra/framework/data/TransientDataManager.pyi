from typing import List
import ghidra.framework.data
import java.lang


class TransientDataManager(object):
    """
    Simple static class to keep track of transient domain file/domain objects.
     When new domain objects are created, they may not have an associated DomainFile.
     In this case, a DomainFileProxy is created to contain it.  DomainFileProxy objects
     will add themselves to this Manager whenever a tool is using the associated
     DomainObject and will remove itself all the tools have released the domainObject.
    """









    @staticmethod
    def addTransient(domainFile: ghidra.framework.data.DomainFileProxy) -> None:
        """
        Adds the given transient domain file to the list.
        @param domainFile the transient domain file to add to the list
        """
        ...

    @staticmethod
    def clearAll() -> None:
        """
        Removes all transients from the list.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getTransients(__a0: List[object]) -> None: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def releaseFiles(consumer: object) -> None:
        """
        Releases all files for the given consumer.
        @param consumer the domain file consumer
        """
        ...

    @staticmethod
    def removeTransient(domainFile: ghidra.framework.data.DomainFileProxy) -> None:
        """
        Removes the given transient domain file from the list.
        @param domainFile the transient domain file to remove
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
