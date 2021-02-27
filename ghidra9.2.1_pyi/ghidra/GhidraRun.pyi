from typing import List
import ghidra
import java.lang


class GhidraRun(object, ghidra.GhidraLaunchable):
    """
    Main Ghidra application class. Creates
     the .ghidra folder that contains the user preferences and tools if it does
     not exist. Initializes JavaHelp and attempts to restore the last opened
     project.
      A list of classes for plugins, data types, and language providers is
     maintained so that a search of the classpath is not done every time
     Ghidra is run. The list is maintained in the GhidraClasses.xml file
     in the user's .ghidra folder. A search of the classpath is done if the
     (1) GhidraClasses.xml file is not found, (2) the classpath is different
     from when the last time Ghidra was run, (3) a class in the file was
     not found,  or (4) a modification date specified in the classes file for
     a jar file is older than the actual jar file's modification date.

     Note: The Plugin path is a user preference that
     indicates locations for where classes for plugins and data types should
     be searched; the Plugin path can include jar files just like a classpath.
     The Plugin path can be changed by using the Edit Plugin Path dialog,
     displayed from the Edit-Edit Plugin Path... menu option on the main
     Ghidra project window.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def launch(self, layout: ghidra.GhidraApplicationLayout, args: List[unicode]) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
