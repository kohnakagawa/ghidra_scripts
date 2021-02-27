import docking.util.image
import ghidra.framework.model
import ghidra.framework.plugintool
import java.lang
import javax.swing
import org.jdom


class ToolTemplate(object):
    """
    Configuration of a tool that knows how to create tools.
    """

    TOOL_INSTANCE_NAME_XML_NAME: unicode = u'INSTANCE_NAME'
    TOOL_NAME_XML_NAME: unicode = u'TOOL_NAME'
    TOOL_XML_NAME: unicode = u'TOOL'







    def createTool(self, project: ghidra.framework.model.Project) -> ghidra.framework.plugintool.PluginTool:
        """
        Creates a tool like only this template knows how.
        @param project the project in which the tool will be living.
        @return a new tool for this template implementation.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getIcon(self) -> javax.swing.ImageIcon:
        """
        Get the icon for this tool template.  This is equivalent to calling
         <code>getIconURL().getIcon()</code>
        @return the icon for this tool template.
        """
        ...

    def getIconURL(self) -> docking.util.image.ToolIconURL:
        """
        Get the iconURL for this tool template
        @return the iconURL for this tool template
        """
        ...

    def getName(self) -> unicode:
        """
        Get the name for the tool.
        @return the name
        """
        ...

    def getPath(self) -> unicode:
        """
        Returns the path from whence this tool template came; may be null if the tool was not
         loaded from the filesystem
        @return the path
        """
        ...

    def getSupportedDataTypes(self) -> java.lang.Class:
        """
        Get the classes of the data types that this tool supports,
         i.e., what data types can be dropped onto this tool.
        @return list of supported data type classes.
        """
        ...

    def getToolElement(self) -> org.jdom.Element:
        """
        This returns the XML element that represents the tool part of the overall XML hierarchy.
        @return the XML element that represents the tool part of the overall XML hierarchy.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def restoreFromXml(self, root: org.jdom.Element) -> None:
        """
        Restore this object from a saved XML element.
        @param root element to restore this object into
        """
        ...

    def saveToXml(self) -> org.jdom.Element:
        """
        Save this object to an XML Element.
        @return the ToolConfig saved as an XML element
        """
        ...

    def setName(self, name: unicode) -> None:
        """
        Set the name for the tool template.
        @param name new tool template name
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
    def icon(self) -> javax.swing.ImageIcon: ...

    @property
    def iconURL(self) -> docking.util.image.ToolIconURL: ...

    @property
    def name(self) -> unicode: ...

    @name.setter
    def name(self, value: unicode) -> None: ...

    @property
    def path(self) -> unicode: ...

    @property
    def supportedDataTypes(self) -> List[java.lang.Class]: ...

    @property
    def toolElement(self) -> org.jdom.Element: ...
