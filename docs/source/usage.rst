Usage
=====

Create custom message finders by subclassing ``BaseMessageFinder`` and
customizing method ``find()``:

.. code-block:: python

    from collectmessages.finders import BaseMessageFinder
    from polib import POEntry


    class MessageFinder(BaseMessageFinder):

        def find(self, language=None):
            ...

Method ``find()`` returns a sequence of ``POEntry`` objects with the
translated messages.  It takes one (optional) parameter ``language``.
If given, this parameter has the language code for the translated messages.
If not given, ``find()`` should return ``POEntry`` objects for a POT-file,
with an empty translated string.
