class BaseMessageFinder(object):
    """Base finder for translated messages.
    """

    def find(self, language=None):
        """Return a sequence of translated messages.
        """
        raise NotImplementedError
