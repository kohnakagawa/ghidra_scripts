import docking.util.image
import ghidra.framework.model
import ghidra.framework.plugintool
import java.lang
import javax.swing
import org.jdom


class GhidraToolTemplate(object, ghidra.framework.model.ToolTemplate):
    """
    Implementation for a tool template that has the class names of the
     plugins that are part of the tool, and the tool's icon.
    """

    TEMPLATE_NAME: unicode
    TOOL_INSTANCE_NAME_XML_NAME: unicode = u'INSTANCE_NAME'
    TOOL_NAME_XML_NAME: unicode = u'TOOL_NAME'
    TOOL_XML_NAME: unicode = u'TOOL'



    @overload
    def __init__(self, root: org.jdom.Element, path: unicode):
        """
        Constructor.
        @param root XML element that contains the tool template data
        @param path the path of the template
        """
        ...

    @overload
    def __init__(self, __a0: docking.util.image.ToolIconURL, __a1: org.jdom.Element, __a2: List[java.lang.Class]): ...



    def createTool(self, project: ghidra.framework.model.Project) -> ghidra.framework.plugintool.PluginTool: ...

    def equals(self, obj: object) -> bool:
        """
        Indicates whether some other object is "equal to" this one.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getIcon(self) -> javax.swing.ImageIcon: ...

    def getIconURL(self) -> docking.util.image.ToolIconURL:
        """
        Get the icon URL.
        """
        ...

    def getName(self) -> unicode: ...

    def getPath(self) -> unicode: ...

    def getSupportedDataTypes(self) -> java.lang.Class: ...

    def getToolElement(self) -> org.jdom.Element: ...

    def hashCode(self) -> int:
        """
        Returns a hash code value for the object. This method is
         supported for the benefit of hashtables such as those provided by
         <code>java.util.Hashtable</code>.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def restoreFromXml(self, root: org.jdom.Element) -> None: ...

    def saveToXml(self) -> org.jdom.Element: ...

    def setIconURL(self, url: docking.util.image.ToolIconURL) -> None: ...

    def setName(self, name: unicode) -> None: ...

    def toString(self) -> unicode:
        """
        Returns a string representation of the object. In general, the
         <code>toString</code> method returns a string that
         "textually represents" this object. The result should
         be a concise but informative representation that is easy for a
         person to read.
        """
        ...

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

    @iconURL.setter
    def iconURL(self, value: docking.util.image.ToolIconURL) -> None: ...

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
