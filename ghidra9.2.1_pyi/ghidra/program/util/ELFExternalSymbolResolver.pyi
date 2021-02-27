import ghidra.app.util.importer
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class ELFExternalSymbolResolver(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def fixUnresolvedExternalSymbols(program: ghidra.program.model.listing.Program, saveIfModified: bool, messageLog: ghidra.app.util.importer.MessageLog, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Links unresolved symbols to the first symbol found in the (ordered) linked
         libraries (saved in the program's properties as "ELF Required Library [nn]").
         <p>
         The ordering and precedence logic is ELF specific though no ELF binary formats
         are parsed or required.
         <p>
         The program's external libraries need to already be populated with paths to
         already existing / imported libraries.
         <p>
        @param program ELF {@link Program} to fix.
        @param saveIfModified boolean flag, if true the program will be saved if there was a
         modification.
        @param messageLog {@link MessageLog} to write info message to.
        @param monitor {@link TaskMonitor} to watch for cancel and update with progress.
        @throws CancelledException if user cancels
        @throws IOException if error reading
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
