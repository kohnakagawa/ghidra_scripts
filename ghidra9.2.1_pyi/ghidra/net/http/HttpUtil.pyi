from typing import List
import java.io
import java.lang
import java.net
import java.util


class HttpUtil(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getContent(httpUrlString: unicode, httpRequestProperties: java.util.Properties, allowRedirect: bool) -> java.net.HttpURLConnection:
        """
        Execute an HTTP/HTTPS GET request and return the resulting HttpURLConnection.
        @param httpUrlString HTTP/HTTPS URL
        @param httpRequestProperties optional HTTP request header values to be included (may be null)
        @param allowRedirect allow site redirects to be handled if true
        @return HttpURLConnection which contains information about the URL
        @throws MalformedURLException bad httpUrlString specified
        @throws IOException if an error occurs while executing request
        """
        ...

    @staticmethod
    def getFile(httpUrlString: unicode, httpRequestProperties: java.util.Properties, allowRedirect: bool, destFile: java.io.File) -> unicode:
        """
        Download a file by executing an HTTP/HTTPS GET request.
        @param httpUrlString HTTP/HTTPS URL
        @param httpRequestProperties optional HTTP request header values to be included (may be null)
        @param allowRedirect allow site redirects to be handled if true
        @param destFile destination file
        @throws MalformedURLException bad httpUrlString specified
        @throws IOException if an error occurs while executing request
        @return String representing the content-type of the file, or null if the information is not available
        """
        ...

    def hashCode(self) -> int: ...

    @staticmethod
    def main(args: List[unicode]) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
