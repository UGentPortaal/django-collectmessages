class BaseMessageFinder(object):
    """Base finder for translated messages.

    Subclass this class to implement a custom message finder.
    """

    def find(self, language=None):
        """Return a sequence of translated messages.

        :param language: The language code
        :type language: string or None
        :rtype: sequence of ``POEntry`` objects
        """
        raise NotImplementedError
