import ghidra.framework.model
import ghidra.framework.plugintool
import ghidra.util
import java.lang
import java.util


class AboutDomainObjectUtils(object):




    def __init__(self): ...



    @staticmethod
    def displayInformation(tool: ghidra.framework.plugintool.PluginTool, domainFile: ghidra.framework.model.DomainFile, metadata: java.util.Map, title: unicode, additionalInfo: unicode, helpLocation: ghidra.util.HelpLocation) -> None:
        """
        Displays an informational dialog about the specified domain object
        @param tool plugin tool
        @param domainFile domain file to display information about
        @param metadata the metadata for the domainFile
        @param title title to use for the dialog
        @param additionalInfo additional custom user information to append to
                               the bottom of the dialog
        @param helpLocation the help location
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
