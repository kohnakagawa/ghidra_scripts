from typing import List
import java.lang


class KeyStorePasswordProvider(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getKeyStorePassword(self, keystorePath: unicode, passwordError: bool) -> List[int]:
        """
        Requests password for keystore file
        @param keystorePath keystore file path
        @param passwordError if true this is a repeated prompt due to a password use failure
        @return password or null, if not null caller will clear array
         when no longer needed.
        """
        ...

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
