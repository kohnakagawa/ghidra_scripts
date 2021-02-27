import ghidra.util.classfinder
import java.lang


class ModuleInitializer(ghidra.util.classfinder.ExtensionPoint, java.lang.Runnable, object):
    """
    An ExtensionPoint that users can implement to perform work before the application
     is loaded.


    		To create a module initializer:

    		1) Implement ModuleInitializer.java
    		2) Have the name of your implementation end with the keyword 'Initializer'

    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode:
        """
        @return initializer name
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def run(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def name(self) -> unicode: ...
