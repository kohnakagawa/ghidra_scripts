import ghidra.app.util.bin.format.pe
import ghidra.app.util.importer
import ghidra.program.model.listing
import java.lang


class ControlFlowGuard(object):
    """
    ControlFlowGuard is a platform security feature that was created to combat memory
     corruption vulnerabilities.

     ReturnFlowGuard was introduced as an addition to ControlFlowGuard in the Windows 10
     Creator's update.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def markup(lcd: ghidra.app.util.bin.format.pe.LoadConfigDirectory, program: ghidra.program.model.listing.Program, log: ghidra.app.util.importer.MessageLog, ntHeader: ghidra.app.util.bin.format.pe.NTHeader) -> None:
        """
        Perform markup on the supported ControlFlowGuard and ReturnFlowGuard functions and
         tables, if they exist.
        @param lcd The PE LoadConfigDirectory.
        @param program The program.
        @param log The log.
        @param ntHeader The PE NTHeader.
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
