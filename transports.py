

class AbstractTransport:
    """
    Base interface for Transport implementations.
    """

    def dial(self, addr, **kwargs):
        """
        Returns an object that inherits from AbstractStream.
        """
        raise NotImplementedError
    
    def create_listener(self):
        """
        Returns an object that inherits from AbstractListener.
        """
        raise NotImplementedError


class AbstractListener:
    """
    Base interface for Listener implementations.
    """

    def listen(self, **kwargs):
        """
        Start accepting new connections.
        """
        raise NotImplementedError

    def close(self):
        raise NotImplementedError
