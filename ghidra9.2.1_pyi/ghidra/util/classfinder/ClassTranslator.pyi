import java.lang


class ClassTranslator(object):
    """
    ClassTranslator provides a way to map an old Ghidra class to
     a current Ghidra class. It can be used whenever a class is moved or renamed
     and Ghidra needs to know.
     Important: Any class that is indicated by the currentClassPath
     passed to the put method should implement ExtensionPoint.
     Whenever a class whose name gets stored in the data base is moved to
     another package or renamed, the map of the old class path name to the
     new one should get put into the ClassTranslator.
     Example:  The class ghidra.app.plugin.core.MyPlugin.MyInfo is in Ghidra version 1.
     In Ghidra version 2, it is moved and renamed to ghidra.app.plugin.core.RenamedPlugin.SubPackage.SaveInfo.
     Put the following static initializer in the version 2 SaveInfo class.

       static {
           ClassTranslator.put("ghidra.app.plugin.core.MyPlugin.MyInfo", SaveInfo.class.getName());
       }

     Warning: If the class gets moved or renamed again in a subsequent version
     of Ghidra, a new translation (put call) should get added to the static initializer block
     and any old translations should have their current path name changed to the new
     class path.
     Example: The class ghidra.app.plugin.core.MyPlugin.MyInfo is in Ghidra version 1.
     In Ghidra version 2, it is moved and renamed to ghidra.app.plugin.core.RenamedPlugin.SubPackage.SaveInfo.
     In Ghidra version 3, it is renamed to ghidra.app.plugin.core.RenamedPlugin.SubPackage.SaveInfo.
     Put the following static initializer in the version 3 SaveInfo class.

       static {
           ClassTranslator.put("ghidra.app.plugin.core.MyPlugin.MyInfo", SaveInfo.class.getName());
           ClassTranslator.put("ghidra.app.plugin.core.RenamedPlugin.SubPackage.SaveInfo", SaveInfo.class.getName());
       }

    """





    def __init__(self): ...



    @staticmethod
    def contains(oldClassPath: unicode) -> bool:
        """
        Returns true if this ClassTranslator has a mapping for the indicated old class path name.
        @param oldClassPath the old class path name of the class.
        @return true if the old class path is mapped to a new class path name in
         the current Ghidra version.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def get(oldClassPath: unicode) -> unicode:
        """
        Returns the current class path name that is mapped for the indicated old class path name.
        @param oldClassPath the old class path name of the class.
        @return the class path name of the current Ghidra version's class file. Otherwise, null if the old class path name isn't mapped.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def put(oldClassPath: unicode, currentClassPath: unicode) -> None:
        """
        Defines a mapping indicating the class path name of the current Ghidra class
         that is the same class as the indicated old class path name from a previous Ghidra version.
        @param oldClassPath the old class path name of the class.
        @param currentClassPath the current class path name of the class.
         <p><strong>Important</strong>: Any class that is indicated by the currentClassPath
         passed to the <code>put</code> method should implement <code>ExtensionPoint</code>.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
