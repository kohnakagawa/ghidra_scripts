from typing import List
import ghidra.pcode.memstate
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.pcode
import java.lang


class MemoryState(object):
    """
    All storage/state for a pcode emulator machine

     Every piece of information in a pcode emulator machine is representable as a triple
     (AddressSpace,offset,size).  This class allows getting and setting
     of all state information of this form.
    """





    def __init__(self, language: ghidra.program.model.lang.Language):
        """
        MemoryState constructor for a specified processor language
        @param language
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    @overload
    def getBigInteger(self, nm: unicode) -> long:
        """
        This is a convenience method for reading registers by name.
         any register name known to the language can be used as a read location.
         The associated address space, offset, and size is looked up and automatically
         passed to the main getValue routine.
        @param nm is the name of the register
        @return the unsigned value associated with that register
        """
        ...

    @overload
    def getBigInteger(self, reg: ghidra.program.model.lang.Register) -> long:
        """
        A convenience method for reading a value directly from a register rather
         than querying for the offset and space
        @param reg the register location to be read
        @return the unsigned value read from the register location
        """
        ...

    @overload
    def getBigInteger(self, vn: ghidra.program.model.pcode.Varnode, signed: bool) -> long:
        """
        A convenience method for reading a value directly from a varnode rather
         than querying for the offset and space
        @param vn the varnode location to be read
        @param signed true if signed value should be returned, false for unsigned value
        @return the unsigned value read from the varnode location
        """
        ...

    @overload
    def getBigInteger(self, spc: ghidra.program.model.address.AddressSpace, off: long, size: int, signed: bool) -> long:
        """
        This is the main interface for reading values from the MemoryState.
         If there is no registered MemoryBank for the desired address space, or
         if there is some other error, an exception is thrown.
        @param spc is the address space being queried
        @param off is the offset of the value being queried
        @param size is the number of bytes to query
        @param signed true if signed value should be returned, false for unsigned value
        @return the queried unsigned value
        """
        ...

    def getChunk(self, res: List[int], spc: ghidra.program.model.address.AddressSpace, off: long, size: int, stopOnUnintialized: bool) -> int:
        """
        This is the main interface for reading a range of bytes from the MemorySate.
         The MemoryBank associated with the address space of the query is looked up
         and the request is forwarded to the getChunk method on the MemoryBank. If there
         is no registered MemoryBank or some other error, an exception is thrown.
         All getLongValue methods utilize this method to read the bytes from the
         appropriate memory bank.
        @param res the result buffer for storing retrieved bytes
        @param spc the desired address space
        @param off the starting offset of the byte range being read
        @param size the number of bytes being read
        @param stopOnUnintialized if true a partial read is permitted and returned size may be
         smaller than size requested
        @return number of bytes actually read
        @throws LowlevelError if spc has not been mapped within this MemoryState or memory fault
         handler generated error
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getMemoryBank(self, spc: ghidra.program.model.address.AddressSpace) -> ghidra.pcode.memstate.MemoryBank:
        """
        Any MemoryBank that has been registered with this MemoryState can be retrieved via this
         method if the MemoryBank's associated address space is known.
        @param spc is the address space of the desired MemoryBank
        @return the MemoryBank or null if no bank is associated with spc.
        """
        ...

    @overload
    def getValue(self, nm: unicode) -> long:
        """
        This is a convenience method for reading registers by name.
         any register name known to the language can be used as a read location.
         The associated address space, offset, and size is looked up and automatically
         passed to the main getValue routine.
        @param nm is the name of the register
        @return the value associated with that register
        """
        ...

    @overload
    def getValue(self, reg: ghidra.program.model.lang.Register) -> long:
        """
        A convenience method for reading a value directly from a register rather
         than querying for the offset and space
        @param reg the register location to be read
        @return the value read from the register location
        """
        ...

    @overload
    def getValue(self, vn: ghidra.program.model.pcode.Varnode) -> long:
        """
        A convenience method for reading a value directly from a varnode rather
         than querying for the offset and space
        @param vn the varnode location to be read
        @return the value read from the varnode location
        """
        ...

    @overload
    def getValue(self, spc: ghidra.program.model.address.AddressSpace, off: long, size: int) -> long:
        """
        This is the main interface for reading values from the MemoryState.
         If there is no registered MemoryBank for the desired address space, or
         if there is some other error, an exception is thrown.
        @param spc is the address space being queried
        @param off is the offset of the value being queried
        @param size is the number of bytes to query
        @return the queried value
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setChunk(self, val: List[int], spc: ghidra.program.model.address.AddressSpace, off: long, size: int) -> None:
        """
        This is the main interface for setting values for a range of bytes in the MemoryState.
         The MemoryBank associated with the desired address space is looked up and the
         write is forwarded to the setChunk method on the MemoryBank. If there is no
         registered MemoryBank or some other error, an exception  is throw.
         All setValue methods utilize this method to read the bytes from the
         appropriate memory bank.
        @param val the byte values to be written into the MemoryState
        @param spc the address space being written
        @param off the starting offset of the range being written
        @param size the number of bytes to write
        @throws LowlevelError if spc has not been mapped within this MemoryState
        """
        ...

    def setInitialized(self, initialized: bool, spc: ghidra.program.model.address.AddressSpace, off: long, size: int) -> None:
        """
        This is the main interface for setting the initialization status for a range of bytes
         in the MemoryState.
         The MemoryBank associated with the desired address space is looked up and the
         write is forwarded to the setInitialized method on the MemoryBank. If there is no
         registered MemoryBank or some other error, an exception  is throw.
         All setValue methods utilize this method to read the bytes from the
         appropriate memory bank.
        @param initialized indicates if range should be marked as initialized or not
        @param spc the address space being written
        @param off the starting offset of the range being written
        @param size the number of bytes to write
        """
        ...

    def setMemoryBank(self, bank: ghidra.pcode.memstate.MemoryBank) -> None:
        """
        MemoryBanks associated with specific address spaces must be registers with this MemoryState
         via this method.  Each address space that will be used during emulation must be registered
         separately.  The MemoryState object does not assume responsibility for freeing the MemoryBank.
        @param bank is a pointer to the MemoryBank to be registered
        """
        ...

    @overload
    def setValue(self, nm: unicode, cval: long) -> None:
        """
        This is a convenience method for setting registers by name.
         Any register name known to the language can be used as a write location.
         The associated address space, offset, and size is looked up and automatically
         passed to the main setValue routine.
        @param nm is the name of the register
        @param cval is the value to write to the register
        """
        ...

    @overload
    def setValue(self, reg: ghidra.program.model.lang.Register, cval: long) -> None:
        """
        A convenience method for setting a value directly on a register rather than
         breaking out the components
        @param reg the register location to be written
        @param cval the value to write into the register location
        """
        ...

    @overload
    def setValue(self, vn: ghidra.program.model.pcode.Varnode, cval: long) -> None:
        """
        A convenience method for setting a value directly on a varnode rather than
         breaking out the components
        @param vn the varnode location to be written
        @param cval the value to write into the varnode location
        """
        ...

    @overload
    def setValue(self, nm: unicode, cval: long) -> None:
        """
        This is a convenience method for setting registers by name.
         Any register name known to the language can be used as a write location.
         The associated address space, offset, and size is looked up and automatically
         passed to the main setValue routine.
        @param nm is the name of the register
        @param cval is the value to write to the register
        """
        ...

    @overload
    def setValue(self, reg: ghidra.program.model.lang.Register, cval: long) -> None:
        """
        A convenience method for setting a value directly on a register rather than
         breaking out the components
        @param reg the register location to be written
        @param cval the value to write into the register location
        """
        ...

    @overload
    def setValue(self, vn: ghidra.program.model.pcode.Varnode, cval: long) -> None:
        """
        A convenience method for setting a value directly on a varnode rather than
         breaking out the components
        @param vn the varnode location to be written
        @param cval the value to write into the varnode location
        """
        ...

    @overload
    def setValue(self, spc: ghidra.program.model.address.AddressSpace, off: long, size: int, cval: long) -> None:
        """
        This is the main interface for writing values to the MemoryState.
         If there is no registered MemoryBank for the desired address space, or
         if there is some other error, an exception is thrown.
        @param spc is the address space to write to
        @param off is the offset where the value should be written
        @param size is the number of bytes to be written
        @param cval is the value to be written
        """
        ...

    @overload
    def setValue(self, spc: ghidra.program.model.address.AddressSpace, off: long, size: int, cval: long) -> None:
        """
        This is the main interface for writing values to the MemoryState.
         If there is no registered MemoryBank for the desired address space, or
         if there is some other error, an exception is thrown.
        @param spc is the address space to write to
        @param off is the offset where the value should be written
        @param size is the number of bytes to be written
        @param cval is the value to be written
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
    def memoryBank(self) -> None: ...  # No getter available.

    @memoryBank.setter
    def memoryBank(self, value: ghidra.pcode.memstate.MemoryBank) -> None: ...
