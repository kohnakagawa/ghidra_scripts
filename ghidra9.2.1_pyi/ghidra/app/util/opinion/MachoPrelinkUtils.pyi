from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format.macho
import ghidra.app.util.bin.format.macho.prelink
import ghidra.util.task
import java.lang
import org.apache.commons.collections4


class MachoPrelinkUtils(object):
    """
    Utilities methods for working with Mach-O PRELINK binaries.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def findPrelinkMachoHeaderOffsets(provider: ghidra.app.util.bin.ByteProvider, monitor: ghidra.util.task.TaskMonitor) -> List[long]:
        """
        Scans the provider looking for PRELINK Mach-O headers.
         <p>
         NOTE: The "System" Mach-O at offset 0 is not considered a PRELINK Mach-O.
         <p>
         NOTE: We used to scan on 0x1000, and then 0x10 byte boundaries.  Now iOS 12 seems to
         put them on 0x8-byte boundaries.
        @param provider The provider to scan.
        @param monitor A monitor.
        @return A list of provider offsets where PRELINK Mach-O headers start (not including the
           "System" Mach-O at offset 0).
        @throws IOException If there was an IO-related issue searching for PRELINK Mach-O headers.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getPrelinkStartAddr(header: ghidra.app.util.bin.format.macho.MachHeader) -> long:
        """
        Gets the start address of the PRELINK Mach-O's in memory.
         <p>
         NOTE: This method only works for pre iOS 12 binaries.  If called on an iOS 12 binary, it will
         fail and return 0 because the __PRELINK_TEXT segment has a size of 0.  In this case, some
         other means of computing the start address of the PRELINK Mach-O's must be used.
        @param header The Mach-O header.
        @return The start address of the PRELINK Mach-O's in memory, or 0 if it could not be found.
        """
        ...

    def hashCode(self) -> int: ...

    @staticmethod
    def matchPrelinkToMachoHeaderOffsets(__a0: ghidra.app.util.bin.ByteProvider, __a1: List[object], __a2: List[object], __a3: ghidra.util.task.TaskMonitor) -> org.apache.commons.collections4.BidiMap: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def parsePrelinkXml(provider: ghidra.app.util.bin.ByteProvider, monitor: ghidra.util.task.TaskMonitor) -> List[ghidra.app.util.bin.format.macho.prelink.PrelinkMap]:
        """
        Parses the provider looking for PRELINK XML.
        @param provider The provider to parse.
        @param monitor A monitor.
        @return A list of discovered {@link PrelinkMap}s.  An empty list indicates that the provider
           did not represent valid Mach-O PRELINK binary.
        @throws IOException if there was an IO-related issue.
        @throws JDOMException if there was a issue parsing the PRELINK XML.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
