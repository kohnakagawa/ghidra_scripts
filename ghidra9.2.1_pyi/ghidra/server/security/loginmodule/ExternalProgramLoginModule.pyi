import java.lang
import java.util
import javax.security.auth
import javax.security.auth.callback
import javax.security.auth.spi


class ExternalProgramLoginModule(object, javax.security.auth.spi.LoginModule):




    def __init__(self): ...



    def abort(self) -> bool: ...

    def commit(self) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def initialize(self, __a0: javax.security.auth.Subject, __a1: javax.security.auth.callback.CallbackHandler, __a2: java.util.Map, __a3: java.util.Map) -> None: ...

    def login(self) -> bool: ...

    def logout(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
