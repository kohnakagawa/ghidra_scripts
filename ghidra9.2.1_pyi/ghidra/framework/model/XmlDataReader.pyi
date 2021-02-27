import ghidra.framework.plugintool
import ghidra.util.task
import java.lang


class XmlDataReader(object):
    """
    Defines the method for creating an Object from an
     XML file in a JarInputStream.
    """









    def addXMLObject(self, tool: ghidra.framework.plugintool.PluginTool, basePath: unicode, relPathName: unicode, removeFile: bool, monitor: ghidra.util.task.TaskMonitor) -> bool:
        """
        Reads the XML file indicated by the base path and relative path name.
         It creates an object(s) from this, that is used by the project.
        @param basePath the prefix part of the path for the XML file
        @param relPathName a pathname for the file relative to the basePath.
        @param removeFile on success this should remove the original file.
        @param monitor a monitor for providing progress information to the user.
        @return true if an object associated with the file was added to the
         project. false if the file couldn't be processed.
        @throws SAXException if the XML file has a XML parsing error.
        @throws IOException if there is problem reading/removing the XML file
         or if there is a problem creating any resulting file.
        @throws NotFoundException if a required service can't be found in
         the service registry.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getSummary(self) -> unicode:
        """
        Returns a string summarizing the results of the XML data read
         or <code>null</code> if there was nothing to report.
        @return a string summarizing the results of the xml data read
                 or <code>null</code> if there was nothing to report
        """
        ...

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

    @property
    def summary(self) -> unicode: ...
