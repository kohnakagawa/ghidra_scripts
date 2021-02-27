from typing import List
import ghidra.program.model.data
import ghidra.util.task
import java.lang


class DataTypeWriter(object):
    """
    A class used to convert data types into ANSI-C.

     The ANSI-C code should compile on most platforms.
    """





    @overload
    def __init__(self, dtm: ghidra.program.model.data.DataTypeManager, writer: java.io.Writer):
        """
        Constructs a new instance of this class using the
         given writer. The default annotation handler is used.
        @param dtm data-type manager corresponding to target program or null
         for default
        @param writer the writer to use when writing data types
        @throws IOException
        """
        ...

    @overload
    def __init__(self, dtm: ghidra.program.model.data.DataTypeManager, writer: java.io.Writer, cppStyleComments: bool):
        """
        Constructs a new instance of this class using the
         given writer. The default annotation handler is used.
        @param dtm data-type manager corresponding to target program or null
         for default
        @param writer the writer to use when writing data types
        @param cppStyleComments whether to use C++ style comments
        @throws IOException
        """
        ...

    @overload
    def __init__(self, dtm: ghidra.program.model.data.DataTypeManager, writer: java.io.Writer, annotator: ghidra.program.model.data.AnnotationHandler):
        """
        Constructs a new instance of this class using the
         given writer and annotation handler
        @param dtm data-type manager corresponding to target program or null
         for default
        @param writer the writer to use when writing data types
        @param annotator the annotation handler to use to annotate the data types
        @throws IOException
        """
        ...

    @overload
    def __init__(self, dtm: ghidra.program.model.data.DataTypeManager, writer: java.io.Writer, annotator: ghidra.program.model.data.AnnotationHandler, cppStyleComments: bool):
        """
        Constructs a new instance of this class using the
         given writer and annotation handler
        @param dtm data-type manager corresponding to target program or null
         for default
        @param writer the writer to use when writing data types
        @param annotator the annotation handler to use to annotate the data types
        @param cppStyleComments whether to use C++ style comments
        @throws IOException
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

    @overload
    def write(self, dataTypes: List[ghidra.program.model.data.DataType], monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Converts all data types in the array into ANSI-C code.
        @param dataTypes the data types to write
        @param monitor the task monitor
        @throws IOException if an I/O error occurs when writing the data types to the specified writer
        @throws CancelledException
        """
        ...

    @overload
    def write(self, category: ghidra.program.model.data.Category, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Converts all data types in the category into ANSI-C code.
        @param category the category containing the datatypes to write
        @param monitor the task monitor
        @throws IOException if an I/O error occurs when writing the data types to the specified writer
        @throws CancelledException
        """
        ...

    @overload
    def write(self, dataTypeManager: ghidra.program.model.data.DataTypeManager, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Converts all data types in the data type manager into ANSI-C code.
        @param dataTypeManager the manager containing the data types to write
        @param monitor the task monitor
        @throws IOException if an I/O error occurs when writing the data types to the specified writer
        @throws CancelledException
        """
        ...

    @overload
    def write(self, __a0: List[object], __a1: ghidra.util.task.TaskMonitor) -> None: ...

    @overload
    def write(self, __a0: List[object], __a1: ghidra.util.task.TaskMonitor, __a2: bool) -> None: ...
