import ghidra.program.model.address
import ghidra.util.task
import java.lang


class AddressCorrelation(object):
    """
    Interface representing the address mapping for any means of correlating addresses
     between a source program and a destination program.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getCorrelatedDestinationRange(self, sourceAddress: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.address.AddressRange:
        """
        Returns the AddressRange of a set of addresses in the destination
         program that correlates to corresponding range in the source program.
        @param sourceAddress the source program address
        @return the destination program address range, or null if the source program address maps
                 to one that is "deleted" in the destination program
        """
        ...

    def getName(self) -> unicode:
        """
        Returns the name of the correlating algorithm.
        @return the name of the correlating algorithm.
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

    @property
    def name(self) -> unicode: ...
