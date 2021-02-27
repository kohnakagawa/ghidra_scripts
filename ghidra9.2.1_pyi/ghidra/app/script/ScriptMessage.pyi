from typing import List
import java.lang
import org.apache.logging.log4j.message


class ScriptMessage(object, org.apache.logging.log4j.message.Message):
    """
    A simple Message implementation that allows us to use the filtering capability
     of log4j.  This class has a formatted and unformatted message.  log4j writes the the formatted
     message out.  Our formatted message is the original message given to us.   We use the
     unformatted message, in conjunction with a regex filter to allow for filtering such that
     the script log file only has script messages.

     See logj4-appender-rolling-file-scripts.xml
    """





    def __init__(self, message: unicode): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFormat(self) -> unicode: ...

    def getFormattedMessage(self) -> unicode: ...

    def getParameters(self) -> List[object]: ...

    def getThrowable(self) -> java.lang.Throwable: ...

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
    def format(self) -> unicode: ...

    @property
    def formattedMessage(self) -> unicode: ...

    @property
    def parameters(self) -> List[object]: ...

    @property
    def throwable(self) -> java.lang.Throwable: ...
