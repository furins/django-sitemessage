
class SiteMessageError(Exception):
    """Base class for sitemessage errors."""


class SiteMessageConfigurationError(SiteMessageError):
    """This error is raised on configuration errors."""


class UnknownMessageTypeError(SiteMessageError):
    """This error is raised when there's a try to access an unknown message type."""


class UnknownMessengerError(SiteMessageError):
    """This error is raised when there's a try to access an unknown messenger."""


class MessengerWarmupException(SiteMessageError):
    """This exception represents a delivery error due to a messenger warm up process failure."""
