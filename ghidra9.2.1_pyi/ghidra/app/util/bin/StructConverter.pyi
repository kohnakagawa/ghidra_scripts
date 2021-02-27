import ghidra.program.model.data
import java.lang


class StructConverter(object):
    """
    Allows a class to create a structure
     datatype equivalent to its class members.
    """

    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    POINTER: ghidra.program.model.data.DataType = pointer
    QWORD: ghidra.program.model.data.DataType = qword
    STRING: ghidra.program.model.data.DataType = string
    UTF16: ghidra.program.model.data.DataType = unicode
    UTF8: ghidra.program.model.data.DataType = string-utf8
    VOID: ghidra.program.model.data.DataType = void
    WORD: ghidra.program.model.data.DataType = word







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toDataType(self) -> ghidra.program.model.data.DataType:
        """
        Returns a structure datatype representing the
         contents of the implementor of this interface.
         <p>
         For example, given:
         <pre>
         class A {
             int foo;
             double bar;
         }
         </pre>
         <p>
         The return value should be a structure data type with two
         data type components; an INT and a DOUBLE. The structure
         should contain field names and, if possible,
         field comments.
        @return returns a structure datatype representing
                 the implementor of this interface
        @throws DuplicateNameException when a datatype of the same name already exists
        @see ghidra.program.model.data.StructureDataType
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
