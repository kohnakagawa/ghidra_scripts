import ghidra.app.util.importer
import ghidra.app.util.xml
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class ProgramXmlMgr(object):
    """
    The manager responsible for reading and writing a program in XML.
    """





    @overload
    def __init__(self, bp: ghidra.app.util.bin.ByteProvider):
        """
        Constructs a new program XML manager using the specified {@link ByteProvider}.
         <p>
         If {@link ByteProvider} has a {@link FSRL} and it is a simple local filepath,
         convert that to a normal local java.io.File instance instead of using the
         {@link ByteProvider}'s File property which is probably located in the
         {@link FileSystemService} filecache directory, which will break the ability
         to find the *.bytes file associated with this .xml file.
         <p>
         This workaround will not help xml files that are truly embedded in a GFileSystem
         (ie. in a .zip file).
        @param bp
        """
        ...

    @overload
    def __init__(self, file: java.io.File):
        """
        Constructs a new program XML manager using the specified file.
         The file should be an XML file.
        @param file the XML file
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getProgramInfo(self) -> ghidra.app.util.xml.ProgramInfo:
        """
        Returns the program info from the underlying file. T``his method
         does not make sense to invoke if a write is being performed
         to a new file.
        @return the program info
        @throws SAXException if an XML error occurs
        @throws IOException if an I/O error occurs
        """
        ...

    @staticmethod
    def getStandardName(name: unicode) -> unicode:
        """
        Converts from a generic format name to standard Ghidra names;
        @param name the generic format name
        @return the equivalent Ghidra name
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def read(self, program: ghidra.program.model.listing.Program, monitor: ghidra.util.task.TaskMonitor, options: ghidra.app.util.xml.XmlProgramOptions) -> ghidra.app.util.importer.MessageLog:
        """
        Reads from the underlying XML file and populates the specified program.
        @param program the program to load the XML into
        @param monitor the task monitor
        @param options the XML options, which features to load and to ignore
        @return the message log containing any warning/error messages
        @throws SAXException if an XML error occurs
        @throws IOException if an I/O occurs
        @throws AddressFormatException if an invalid address is specified in the XML
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def write(self, program: ghidra.program.model.listing.Program, addrSet: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor, options: ghidra.app.util.xml.XmlProgramOptions) -> ghidra.app.util.importer.MessageLog:
        """
        Writes the specified program in XML into the underlying file.
        @param program the program to write into XML
        @param addrSet an address set to limit areas of program that written, or null for entire program
        @param monitor the task monitor
        @param options the XML options to limit what is and is not written out
        @return the message log containing any warning/error messages
        @throws IOException if an I/O occurs
        @throws CancelledException if the user cancels the read
        """
        ...

    @property
    def programInfo(self) -> ghidra.app.util.xml.ProgramInfo: ...
