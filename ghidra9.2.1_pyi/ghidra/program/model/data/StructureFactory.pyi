from typing import List
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.listing
import java.lang


class StructureFactory(object):
    """
    Creates and initializes Structure objects.
    """

    DEFAULT_STRUCTURE_NAME: unicode = u'struct'



    def __init__(self): ...



    @overload
    @staticmethod
    def createStructureDataType(program: ghidra.program.model.listing.Program, address: ghidra.program.model.address.Address, dataLength: int) -> ghidra.program.model.data.Structure:
        """
        Creates a {@link StructureDataType} instance based upon the information
         provided.  The instance will not be placed in memory.
         <p>
         This method is just a pass-through method for
         {@link #createStructureDataType(Program,Address,int,String,boolean)}
         equivalent to calling:
         <pre>
              Structure newStructure = StructureFactory.createStructureDataType(
                  program, address, dataLength, DEFAULT_STRUCTURE_NAME, true );
         </pre>
        @param program The program to which the structure will belong.
        @param address The address of the structure.
        @param dataLength The number of components to add to the structure.
        @return A new structure not yet added to memory.
        @throws IllegalArgumentException for the following conditions:
                 <ul>
                      <li>if <code>dataLength</code> is not greater than zero
                      <li>if the number of components to add exceeds the available
                          address space
                      <li>if there are any instructions in the provided
                          address space
                      <li>if there are no data components to add to the structure
                 </ul>
        """
        ...

    @overload
    @staticmethod
    def createStructureDataType(program: ghidra.program.model.listing.Program, address: ghidra.program.model.address.Address, dataLength: int, structureName: unicode, makeUniqueName: bool) -> ghidra.program.model.data.Structure:
        """
        Creates a {@link StructureDataType} instance based upon the information
         provided.  The instance will not be placed in memory.
        @param program The program to which the structure will belong.
        @param address The address of the structure.
        @param dataLength The number of components to add to the structure.
        @param structureName The name of the structure to create.
        @param makeUniqueName True indicates that the provided name should be
                 altered as necessary in order to make it unique in the program.
        @return A new structure not yet added to memory.
        @throws IllegalArgumentException for the following conditions:
                 <ul>
                      <li>if <code>structureName</code> is <code>null</code>
                      <li>if <code>dataLength</code> is not greater than zero
                      <li>if the number of components to add exceeds the available
                          address space
                      <li>if there are any instructions in the provided
                          address space
                      <li>if there are no data components to add to the structure
                 </ul>
        """
        ...

    @overload
    @staticmethod
    def createStructureDataTypeInStrucuture(program: ghidra.program.model.listing.Program, address: ghidra.program.model.address.Address, fromPath: List[int], toPath: List[int]) -> ghidra.program.model.data.Structure:
        """
        Creates a {@link StructureDataType} instance, which is inside of
         another structure, based upon the information provided.  The instance
         will not be placed in memory.
         <p>
         This method is just a pass-through method for
         {@link #createStructureDataTypeInStrucuture(Program,Address,int[],int[],String,boolean)}
         equivalent to calling:
         <pre>
              Structure newStructure = StructureFactory.createStructureDataTypeInStrucuture(
                  program, address, fromPath, toPath, DEFAULT_STRUCTURE_NAME, true );
         </pre>
        @param program The program to which the structure will belong.
        @param address The address of the structure.
        @param fromPath The path to the first element in the parent structure
                 that will be in the new structure.
        @param toPath The path to the last element in the parent structure
                 that will be in the new structure.
        @return A new structure not yet added to memory.
        @throws IllegalArgumentException for the following conditions:
                 <ul>
                      <li>if the component at <code>fromPath</code> or the component
                          at <code>toPath</code> are null
                      <li>if there is not data to add to the structure
                      <li>if the parent data type is not a structure
                 </ul>
        """
        ...

    @overload
    @staticmethod
    def createStructureDataTypeInStrucuture(program: ghidra.program.model.listing.Program, address: ghidra.program.model.address.Address, fromPath: List[int], toPath: List[int], structureName: unicode, makeUniqueName: bool) -> ghidra.program.model.data.Structure:
        """
        Creates a {@link StructureDataType} instance, which is inside of
         another structure, based upon the information provided.  The instance
         will not be placed in memory.
        @param program The program to which the structure will belong.
        @param address The address of the structure.
        @param fromPath The path to the first element in the parent structure
                 that will be in the new structure.
        @param toPath The path to the last element in the parent structure
                 that will be in the new structure.
        @param structureName the name of the structure to create
        @param makeUniqueName True indicates that the provided name should be
                 altered as necessary in order to make it unique in the program.
        @return A new structure not yet added to memory.
        @throws IllegalArgumentException for the following conditions:
                 <ul>
                      <li>if <code>structureName</code> is <code>null</code>
                      <li>if the component at <code>fromPath</code> or the component
                          at <code>toPath</code> are null
                      <li>if there is not data to add to the structure
                      <li>if the parent data type is not a structure
                 </ul>
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
