import ghidra.framework.plugintool
import java.lang
import java.net


class BrowserLoader(object):
    """
    BrowserLoader opens a web browser and displays the given url.
    """





    def __init__(self): ...



    @overload
    @staticmethod
    def display(url: java.net.URL) -> None:
        """
        Display the content specified by url in a web browser window.  This call will launch
         a new thread and then immediately return.
        @param url The URL to show.
        """
        ...

    @overload
    @staticmethod
    def display(url: java.net.URL, fileURL: java.net.URL, serviceProvider: ghidra.framework.plugintool.ServiceProvider) -> None:
        """
        Display the content specified by url in a web browser window.  This call will launch
         a new thread and then immediately return.
        @param url The web URL to show (e.g., http://localhost...).
        @param fileURL The file URL to show (e.g., file:///path/to/file).
        @param serviceProvider A service provider from which to get system resources.
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
