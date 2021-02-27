from typing import List
import ghidra.app.util
import ghidra.app.util.exporter
import ghidra.app.util.importer
import ghidra.framework.model
import ghidra.framework.plugintool
import ghidra.program.model.address
import ghidra.util
import ghidra.util.task
import java.io
import java.lang


class IntelHexExporter(ghidra.app.util.exporter.Exporter):
    """
    Exports the current program (or program selection) as bytes in Intel Hex format.

     The output defaults to lines of 16-bytes but this is configurable using the
     #recordSizeOption attribute. This allows users to select any record size
     up to the max of 0xFF. Users may also choose to Drop Extra Bytes, which will
     cause only lines that match the max record size to be printed; any other
     bytes will be dropped. If this option is not set, every byte will be represented in the output.
    """





    @overload
    def __init__(self):
        """
        Constructs a new Intel Hex exporter. This will use a record size of 16 (the default)
         and will export ALL bytes in the program or selection (even if the total length
         is not a multiple of 16.
        """
        ...

    @overload
    def __init__(self, recordSize: int, dropBytes: bool):
        """
        Constructs a new Intel Hex exporter with a custom record size.
        @param recordSize the record size to use when writing to the output file
        @param dropBytes if true, bytes at the end of the file that don't match the specified
         record size will be dropped
        """
        ...



    def canExportDomainObject(self, domainObjectClass: java.lang.Class) -> bool:
        """
        Returns true if this exporter knows how to export the given domain object.  For example,
         some exporters know how to export programs, other exporters can export project data type
         archives.
        @param domainObjectClass the class of the domain object to test for exporting.
        @return true if this exporter knows how to export the given domain object.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def export(self, file: java.io.File, domainObj: ghidra.framework.model.DomainObject, addrSet: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDefaultFileExtension(self) -> unicode:
        """
        Returns the default extension for this exporter.
         For example, .html for .xml.
        @return the default extension for this exporter
        """
        ...

    def getHelpLocation(self) -> ghidra.util.HelpLocation:
        """
        Returns the help location for this exporter.
         It should return null only if no help documentation exists.
        @return the help location for this exporter
        """
        ...

    def getMessageLog(self) -> ghidra.app.util.importer.MessageLog:
        """
        Returns the message log the may have been created during an export.
         The message log is used to log warnings and other non-critical messages.
        @return the message log
        """
        ...

    def getName(self) -> unicode:
        """
        Returns the display name of this exporter.
        @return the display name of this exporter
        """
        ...

    def getOptions(self, domainObjectService: ghidra.app.util.DomainObjectService) -> List[ghidra.app.util.Option]: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setExporterServiceProvider(self, provider: ghidra.framework.plugintool.ServiceProvider) -> None:
        """
        Sets the exporter service provider.
        @param provider the exporter service provider
        """
        ...

    def setOptions(self, __a0: List[object]) -> None: ...

    def supportsPartialExport(self) -> bool:
        """
        Returns true if this exporter can export less than the entire domain file.
        @return true if this exporter can export less than the entire domain file.
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
    def options(self) -> None: ...  # No getter available.

    @options.setter
    def options(self, value: List[object]) -> None: ...
