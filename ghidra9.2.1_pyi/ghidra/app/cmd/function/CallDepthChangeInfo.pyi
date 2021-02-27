import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class CallDepthChangeInfo(object):
    """
    Given a function in a program or the start of a function, record information
     about the change to a stack pointer from a subroutine call. The routine
     getCallChange() can be called with the address of a call instruction. If the
     stack could be tracked, the call instruction will return the change in the
     stack pointer that would result from a call to the function.

     The computation is based on a set of equations that are generated and solved.
     Each equation represents the stack change for a given basic flow block or
     call instruction within the function.
    """





    @overload
    def __init__(self, func: ghidra.program.model.listing.Function):
        """
        Construct a new CallDepthChangeInfo object.
        @param func function to examine
        """
        ...

    @overload
    def __init__(self, func: ghidra.program.model.listing.Function, monitor: ghidra.util.task.TaskMonitor):
        """
        Construct a new CallDepthChangeInfo object.
        @param func function to examine
        @param monitor monitor used to cancel the operation
        @throws CancelledException if the operation was canceled
        """
        ...

    @overload
    def __init__(self, function: ghidra.program.model.listing.Function, restrictSet: ghidra.program.model.address.AddressSetView, frameReg: ghidra.program.model.lang.Register, monitor: ghidra.util.task.TaskMonitor):
        """
        Construct a new CallDepthChangeInfo object.
        @param function function to examine
        @param restrictSet set of addresses to restrict flow flowing to.
        @param frameReg register that is to have it's depth(value) change tracked
        @param monitor monitor used to cancel the operation
        @throws CancelledException if the operation was canceled
        """
        ...

    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, addr: ghidra.program.model.address.Address, restrictSet: ghidra.program.model.address.AddressSetView, frameReg: ghidra.program.model.lang.Register, monitor: ghidra.util.task.TaskMonitor):
        """
        Construct a new CallDepthChangeInfo object.
        @param program program containing the function to examime
        @param addr address within the function to examine
        @param restrictSet set of addresses to restrict flow flowing to.
        @param frameReg register that is to have it's depth(value) change tracked
        @param monitor monitor used to cancel the operation
        @throws CancelledException if the operation was canceled
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getCallChange(self, addr: ghidra.program.model.address.Address) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getDepth(self, addr: ghidra.program.model.address.Address) -> int: ...

    def getInstructionStackDepthChange(self, instr: ghidra.program.model.listing.Instruction) -> int:
        """
        Inspect the instruction and return how it affects the stack depth. If the
         depth cannot be determined, then return that the stack depth change is
         unknown.
        @param instr instruction to analyze
        @return int change to stack depth if it can be determined,
                 Function.UNKNOWN_STACK_DEPTH_CHANGE otherwise.
        """
        ...

    def getRegDepth(self, addr: ghidra.program.model.address.Address, reg: ghidra.program.model.lang.Register) -> int:
        """
        @param addr the address to get the register depth at.
        @param reg the register to get the depth of.
        @return the depth of the register at the address.
        """
        ...

    def getRegValueRepresentation(self, addr: ghidra.program.model.address.Address, reg: ghidra.program.model.lang.Register) -> unicode:
        """
        @param addr the address of the register value to get the representation of.
        @param reg the register to get the representation of.
        @return the string representation of the register value.
        """
        ...

    def getSPDepth(self, addr: ghidra.program.model.address.Address) -> int:
        """
        @param addr the address to get the stack pointer depth at.
        @return the stack pointer depth at the address.
        """
        ...

    @staticmethod
    def getStackDepthChange(program: ghidra.program.model.listing.Program, address: ghidra.program.model.address.Address) -> int:
        """
        Gets the stack depth change value that has been set at the indicated address.
        @param program the program to be checked
        @param address the program address
        @return the stack depth change value or null if value has not been set
        """
        ...

    @staticmethod
    def getStackDepthChanges(program: ghidra.program.model.listing.Program, addressSet: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.AddressIterator:
        """
        Gets an iterator indicating all the addresses that have a stack depth change value specified
         within a program's indicated address set.
        @param program the program to be checked
        @param addressSet the set of addresses to check for a stack depth change value
        @return the address iterator indicating where stack depth change values have been set
        """
        ...

    def getStackOffset(self, cu: ghidra.program.model.listing.Instruction, opIndex: int) -> int: ...

    def getStackPurge(self) -> int: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def removeStackDepthChange(program: ghidra.program.model.listing.Program, address: ghidra.program.model.address.Address) -> bool:
        """
        Removes the value for the stack depth change at the indicated address.
        @param program the program where the value will be removed
        @param address the program address
        @return true if a stack depth change existed at the indicated at the address and it was removed.
        """
        ...

    @staticmethod
    def setStackDepthChange(program: ghidra.program.model.listing.Program, address: ghidra.program.model.address.Address, stackDepthChange: int) -> None:
        """
        Sets a new value for the stack depth change at the indicated address.
        @param program the program where the value will be set
        @param address the program address
        @param stackDepthChange the new stack depth change value
        @throws DuplicateNameException if the property name for stack depth changes conflicted
         with another property tha has the same name.
        """
        ...

    def smoothDepth(self, program1: ghidra.program.model.listing.Program, func: ghidra.program.model.listing.Function, monitor: ghidra.util.task.TaskMonitor) -> int:
        """
        Do a better job of tracking the stack by attempting to follow the data
         flow of the stack pointer as it moves in and out of other variables.
        @param program1 -
                    program containing the function to analyze
        @param func -
                    function to analyze stack pointer references
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
    def stackPurge(self) -> int: ...
