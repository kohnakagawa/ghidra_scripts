import ghidra.app.util.bin
import ghidra.app.util.importer
import ghidra.program.database.mem
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.model.mem
import ghidra.util.task
import java.io
import java.lang


class MemoryBlockUtils(object):
    """
    Convenience methods for creating memory blocks.
    """





    def __init__(self): ...



    @staticmethod
    def adjustFragment(program: ghidra.program.model.listing.Program, address: ghidra.program.model.address.Address, name: unicode) -> None:
        """
        Adjusts the name of the fragment at the given address to the given name.
        @param program the program whose fragment is to be renamed.
        @param address the address of the fragment to be renamed.
        @param name the new name for the fragment.
        """
        ...

    @staticmethod
    def createBitMappedBlock(program: ghidra.program.model.listing.Program, name: unicode, start: ghidra.program.model.address.Address, base: ghidra.program.model.address.Address, length: int, comment: unicode, source: unicode, r: bool, w: bool, x: bool, overlay: bool, log: ghidra.app.util.importer.MessageLog) -> ghidra.program.model.mem.MemoryBlock:
        """
        Creates a new bit mapped memory block. (A bit mapped block is a block where each byte value
         is either 1 or 0 and the value is taken from a bit in a byte at some other address in memory)
        @param program the program in which to create the block.
        @param name the name of the new block.
        @param start the starting address of the new block.
        @param base the address of the region in memory to map to.
        @param length the length of the new block
        @param comment the comment text to associate with the new block.
        @param source the source of the block (This field is not well defined - currently another comment)
        @param r the read permission for the new block.
        @param w the write permission for the new block.
        @param x the execute permission for the new block.
        @param overlay create overlay block if true otherwise a normal mapped block will be created
        @param log a {@link StringBuffer} for appending error messages
        @return the new created block
        """
        ...

    @staticmethod
    def createByteMappedBlock(program: ghidra.program.model.listing.Program, name: unicode, start: ghidra.program.model.address.Address, base: ghidra.program.model.address.Address, length: int, comment: unicode, source: unicode, r: bool, w: bool, x: bool, overlay: bool, log: ghidra.app.util.importer.MessageLog) -> ghidra.program.model.mem.MemoryBlock:
        """
        Creates a new byte mapped memory block with a 1:1 byte mapping scheme.
         (A byte mapped block is a block where each byte value
         is taken from a byte at some other address in memory)
        @param program the program in which to create the block.
        @param name the name of the new block.
        @param start the starting address of the new block.
        @param base the address of the region in memory to map to.
        @param length the length of the new block
        @param comment the comment text to associate with the new block.
        @param source the source of the block (This field is not well defined - currently another comment)
        @param r the read permission for the new block.
        @param w the write permission for the new block.
        @param x the execute permission for the new block.
        @param overlay create overlay block if true otherwise a normal mapped block will be created
        @param log a {@link MessageLog} for appending error messages
        @return the new created block
        """
        ...

    @overload
    @staticmethod
    def createFileBytes(program: ghidra.program.model.listing.Program, provider: ghidra.app.util.bin.ByteProvider, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.database.mem.FileBytes:
        """
        Creates a new {@link FileBytes} object using all the bytes from a {@link ByteProvider}
        @param program the program in which to create a new FileBytes object
        @param provider the ByteProvider from which to get the bytes.
        @return the newly created FileBytes object.
        @param monitor the monitor for canceling this potentially long running operation.
        @throws IOException if an IOException occurred.
        """
        ...

    @overload
    @staticmethod
    def createFileBytes(program: ghidra.program.model.listing.Program, provider: ghidra.app.util.bin.ByteProvider, offset: long, length: long, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.database.mem.FileBytes:
        """
        Creates a new {@link FileBytes} object using a portion of the bytes from a {@link ByteProvider}
        @param program the program in which to create a new FileBytes object
        @param provider the ByteProvider from which to get the bytes.
        @param offset the offset into the ByteProvider from which to start loading bytes.
        @param length the number of bytes to load
        @param monitor the monitor for canceling this potentially long running operation.
        @return the newly created FileBytes object.
        @throws IOException if an IOException occurred.
        @throws CancelledException if the user cancelled the operation
        """
        ...

    @overload
    @staticmethod
    def createInitializedBlock(program: ghidra.program.model.listing.Program, isOverlay: bool, name: unicode, start: ghidra.program.model.address.Address, length: long, comment: unicode, source: unicode, r: bool, w: bool, x: bool, log: ghidra.app.util.importer.MessageLog) -> ghidra.program.model.mem.MemoryBlock:
        """
        Create a new initialized memory block.  Initialized to all zeros.
        @param program the program in which to create the block.
        @param isOverlay if true, the block will be created in a new overlay space for that block
        @param name the name of the new block.
        @param start the starting address of the new block.
        @param length the length of the new block
        @param comment the comment text to associate with the new block.
        @param source the source of the block (This field is not well defined - currently another comment)
        @param r the read permission for the new block.
        @param w the write permission for the new block.
        @param x the execute permission for the new block.
        @param log a {@link MessageLog} for appending error messages
        @return the newly created block or null if the operation failed.
        """
        ...

    @overload
    @staticmethod
    def createInitializedBlock(program: ghidra.program.model.listing.Program, isOverlay: bool, name: unicode, start: ghidra.program.model.address.Address, fileBytes: ghidra.program.database.mem.FileBytes, offset: long, length: long, comment: unicode, source: unicode, r: bool, w: bool, x: bool, log: ghidra.app.util.importer.MessageLog) -> ghidra.program.model.mem.MemoryBlock:
        """
        Creates a new initialized block in memory using the bytes from a {@link FileBytes} object.
         If there is a conflict when creating this block (some other block occupies at least some
         of the addresses that would be occupied by the new block), then an attempt will be made
         to create the new block in an overlay.
        @param program the program in which to create the block.
        @param isOverlay if true, the block will be created in a new overlay space for that block
        @param name the name of the new block.
        @param start the starting address of the new block.
        @param fileBytes the {@link FileBytes} object that supplies the bytes for this block.
        @param offset the offset into the {@link FileBytes} object where the bytes for this block reside.
        @param length the length of the new block
        @param comment the comment text to associate with the new block.
        @param source the source of the block (This field is not well defined - currently another comment)
        @param r the read permission for the new block.
        @param w the write permission for the new block.
        @param x the execute permission for the new block.
        @param log a {@link MessageLog} for appending error messages
        @return the new created block
        @throws AddressOverflowException if the address
        """
        ...

    @overload
    @staticmethod
    def createInitializedBlock(program: ghidra.program.model.listing.Program, isOverlay: bool, name: unicode, start: ghidra.program.model.address.Address, dataInput: java.io.InputStream, dataLength: long, comment: unicode, source: unicode, r: bool, w: bool, x: bool, log: ghidra.app.util.importer.MessageLog, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.mem.MemoryBlock:
        """
        Creates a new initialized block in memory using the bytes from the given input stream.
         If there is a conflict when creating this block (some other block occupies at least some
         of the addresses that would be occupied by the new block), then an attempt will be made
         to create the new block in an overlay.
        @param program the program in which to create the block.
        @param isOverlay if true, the block will be created in a new overlay space for that block
        @param name the name of the new block.
        @param start the starting address of the new block.
        @param dataInput the {@link InputStream} object that supplies the bytes for this block.
        @param dataLength the length of the new block
        @param comment the comment text to associate with the new block.
        @param source the source of the block (This field is not well defined - currently another comment)
        @param r the read permission for the new block.
        @param w the write permission for the new block.
        @param x the execute permission for the new block.
        @param log a {@link MessageLog} for appending error messages
        @param monitor the monitor for canceling this potentially long running operation.
        @return the new created block
        @throws AddressOverflowException if the address
        """
        ...

    @staticmethod
    def createUninitializedBlock(program: ghidra.program.model.listing.Program, isOverlay: bool, name: unicode, start: ghidra.program.model.address.Address, length: long, comment: unicode, source: unicode, r: bool, w: bool, x: bool, log: ghidra.app.util.importer.MessageLog) -> ghidra.program.model.mem.MemoryBlock:
        """
        Creates a new uninitialized memory block.
        @param program the program in which to create the block.
        @param isOverlay if true, the block will be created in a new overlay space for that block
        @param name the name of the new block.
        @param start the starting address of the new block.
        @param length the length of the new block
        @param comment the comment text to associate with the new block.
        @param source the source of the block (This field is not well defined - currently another comment)
        @param r the read permission for the new block.
        @param w the write permission for the new block.
        @param x the execute permission for the new block.
        @param log a {@link MessageLog} for appending error messages
        @return the newly created block or null if the operation failed.
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
