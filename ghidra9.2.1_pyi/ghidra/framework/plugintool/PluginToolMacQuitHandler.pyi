import ghidra.framework.plugintool
import java.lang


class PluginToolMacQuitHandler(object):
    """
    A plugin-level quit handler that serves as the callback from the Dock's 'Quit' popup action.

     This will also respond to the Command-Q callback.

     Note: there is a big assumption for this class that the 'front end tool', whatever that may
     be for your application, will be installed before all other tools.  Thus, when quit is called
     on your application, it will go through the main tool of your app, that knows about sub-tools
     and such.  Moreover, you would not want this handler installed on a subordinate tool; otherwise,
     the quit handler would try to close the wrong tool when the handler is activated.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def install(tool: ghidra.framework.plugintool.PluginTool) -> None:
        """
        Applies a quit handler which will close the given tool.
        @param tool The tool to close, which should result in the desired quit behavior.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
