import ghidra.framework.cmd
import ghidra.framework.model
import ghidra.program.disassemble
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.util.task
import java.lang


class DisassembleCommand(ghidra.framework.cmd.BackgroundCommand):
    """
    Command object for performing disassembly
    """





    @overload
    def __init__(self, startSet: ghidra.program.model.address.AddressSetView, restrictedSet: ghidra.program.model.address.AddressSetView):
        """
        Constructor for DisassembleCommand.
        @param startSet set of addresses to be the start of a disassembly.  The
         Command object will attempt to start a disassembly at each address in this set.
        @param restrictedSet addresses that can be disassembled.
         a null set implies no restrictions
        """
        ...

    @overload
    def __init__(self, start: ghidra.program.model.address.Address, restrictedSet: ghidra.program.model.address.AddressSetView, followFlow: bool):
        """
        Constructor for DisassembleCommand.
        @param start Address to start disassembly.
        @param restrictedSet addresses that can be disassembled.
         a null set implies no restrictions
        @param followFlow true means the disassembly should follow flow
        """
        ...

    @overload
    def __init__(self, startSet: ghidra.program.model.address.AddressSetView, restrictedSet: ghidra.program.model.address.AddressSetView, followFlow: bool):
        """
        Constructor for DisassembleCommand.
        @param startSet set of addresses to be the start of a disassembly.  The
         Command object will attempt to start a disassembly at each address in this set.
        @param restrictedSet addresses that can be disassembled.
         a null set implies no restrictions
        """
        ...



    @overload
    def applyTo(self, obj: ghidra.framework.model.DomainObject) -> bool: ...

    @overload
    def applyTo(self, obj: ghidra.framework.model.DomainObject, monitor: ghidra.util.task.TaskMonitor) -> bool: ...

    def canCancel(self) -> bool:
        """
        Check if the command can be canceled.
        @return true if this command can be canceled
        """
        ...

    def dispose(self) -> None:
        """
        Called when this command is going to be removed/canceled without
         running it.  This gives the command the opportunity to free any
         temporary resources it has hold of.
        """
        ...

    def enableCodeAnalysis(self, enable: bool) -> None:
        """
        Set code analysis enablement.  By default new instructions will be
         submitted for auto-analysis.
        @param enable
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDisassembledAddressSet(self) -> ghidra.program.model.address.AddressSet:
        """
        Returns an address set of all instructions that were disassembled.
        @return an address set of all instructions that were disassembled
        """
        ...

    def getName(self) -> unicode: ...

    def getStatusMsg(self) -> unicode: ...

    def hasProgress(self) -> bool:
        """
        Check if the command provides progress information.
        @return true if the command shows progress information
        """
        ...

    def hashCode(self) -> int: ...

    def isModal(self) -> bool:
        """
        Check if the command requires the monitor to be modal.  No other
         command should be allowed, and the GUI will be locked.
        @return true if no other operation should be going on while this
         command is in progress.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setInitialContext(self, initialContextValue: ghidra.program.model.lang.RegisterValue) -> None:
        """
        Allows a specified initial context to be used at all start points.  This value will take
         precedence when combined with any individual seed context values specified by the
         {@link #setSeedContext(DisassemblerContextImpl)} method.
         The defaultSeedContext should remain unchanged while disassembler command
         is actively running.
        @param initialContextValue the initial context value to set or null to clear it
        """
        ...

    def setSeedContext(self, seedContext: ghidra.program.disassemble.DisassemblerContextImpl) -> None:
        """
        Allows the disassembler context to be seeded for the various disassembly start
         points which may be encountered using the future flow state of the specified seedContext.
         Any initial context set via the {@link #setInitialContext(RegisterValue)} method will take
         precedence when combined with any seed values.
         The seedContext should remain unchanged while disassembler command is actively running.
        @param seedContext seed context or null
        """
        ...

    def taskCompleted(self) -> None:
        """
        Called when the task monitor is completely done with indicating progress.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def disassembledAddressSet(self) -> ghidra.program.model.address.AddressSet: ...

    @property
    def initialContext(self) -> None: ...  # No getter available.

    @initialContext.setter
    def initialContext(self, value: ghidra.program.model.lang.RegisterValue) -> None: ...

    @property
    def seedContext(self) -> None: ...  # No getter available.

    @seedContext.setter
    def seedContext(self, value: ghidra.program.disassemble.DisassemblerContextImpl) -> None: ...

    @property
    def statusMsg(self) -> unicode: ...
