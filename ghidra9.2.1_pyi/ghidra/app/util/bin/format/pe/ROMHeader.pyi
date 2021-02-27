import java.lang


class ROMHeader(object):
    """
    A class to represent the
     IMAGE_ROM_HEADERS
     struct as defined in
     winnt.h.


     typedef struct _IMAGE_ROM_HEADERS {
        IMAGE_FILE_HEADER FileHeader;
        IMAGE_ROM_OPTIONAL_HEADER OptionalHeader;
     } IMAGE_ROM_HEADERS, *PIMAGE_ROM_HEADERS;

    """





    def __init__(self): ...



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
