import ghidra.program.model.data
import ghidra.util.task
import ghidra.util.xml
import ghidra.xml
import java.lang


class DataTypesXmlMgr(object):
    """
    This manager is responsible for reading and writing datatypes in XML.
    """





    def __init__(self, dataManager: ghidra.program.model.data.DataTypeManager, log: ghidra.app.util.importer.MessageLog):
        """
        Constructs a new data types XML manager.
        @param dataManager the data type manager to read from or write to
        @param log the message log for recording datatype warnings
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def read(self, parser: ghidra.xml.XmlPullParser, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Reads the datatypes encoded in XML from the specified XML parser and recreates
         them in a datatype manager.
        @param parser the XML parser
        @param monitor the task monitor
        @throws SAXParseException if an XML parse error occurs
        @throws CancelledException if the user cancels the read operation
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def write(self, writer: ghidra.util.xml.XmlWriter, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Writes datatypes into XML using the specified XML writer.
        @param writer the XML writer
        @param monitor the task monitor
        @throws CancelledException if the user cancels the write operation
        """
        ...

    @staticmethod
    def writeAsXMLForDebug(dataManager: ghidra.program.model.data.DataTypeManager, outputFilename: unicode) -> None:
        """
        Output data types in XML format for debugging purposes.
         NOTE: There is no support for reading the XML produced by this
         method.
        @param outputFilename name of the output file
        @throws IOException if there was a problem writing to the file
        """
        ...
