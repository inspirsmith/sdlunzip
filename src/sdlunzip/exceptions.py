from .status_codes import Status


class SdlunzipException(Exception):
    MESSAGE = "Default error message"
    STATUS_CODE = Status.FAILURE

    def __init__(self):
        super().__init__(self.MESSAGE)
        self.status_code = self.STATUS_CODE


class InvalidZipFile(SdlunzipException):
    MESSAGE = "Specified zip file is not an instance of zipfile.ZipFile"
    STATUS_CODE = Status.BAD_ZIP


class NoPasswordError(SdlunzipException):
    MESSAGE = "No password: SDL_PASSWORD environment variable must be set to use this library"
    STATUS_CODE = Status.NO_PWD


class BadPasswordError(SdlunzipException):
    MESSAGE = "Bad password: password specified in SDL_PASSWORD environment variable incorrect"
    STATUS_CODE = Status.BAD_PWD


class LogFileNotFoundError(SdlunzipException):
    MESSAGE = "Specified log file not found in zip file"
    STATUS_CODE = Status.FILE_NOT_FOUND