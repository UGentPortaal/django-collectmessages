Configuration
=============

1. Add the following options to ``settings.py``:

   ``COLLECTMESSAGES_PATH``
        The path of the locale directory where the generated translation
        files will be placed.  This option is required.

   ``COLLECTMESSAGES_LANGUAGES``
        A list of language codes.  Translation files will be generated for
        each code.  This option is required.

   ``COLLECTMESSAGES_FINDERS``
        A list of message finders.  Each message finder returns a sequence
        of translated messages for the translation files.  This option
        is required.

   ``COLLECTMESSAGES_METADATA``
        A dictionary with the metadata for the PO-files.  This setting
        is optional.

   Example:

   .. code-block:: python

        COLLECTMESSAGES_PATH = "collected/locale"
        COLLECTMESSAGES_LANGUAGES = ("en", "nl")
        COLLECTMESSAGES_FINDERS = (
            "firstexampleapp.messages.MessageFinder",
            "secondexampleapp.messages.MessageFinder",
        )
        COLLECTMESSAGES_METADATA = {
            "Project-Id-Version": "1.0",
            "Report-Msgid-Bugs-To": "john.doe@example.com",
            "POT-Creation-Date": "2007-10-18 14:00+0100",
            "PO-Revision-Date": "2007-10-18 14:00+0100",
            "Last-Translator": "John Doe <john.doe@example.com>",
            "Language-Team": "Translations <translations@example.com>",
            "MIME-Version": "1.0",
            "Content-Type": "text/plain; charset=utf-8",
            "Content-Transfer-Encoding": "8bit",
        }

2. Add ``COLLECTMESSAGES_PATH`` to ``LOCALE_PATHS`` in ``settings.py``, so
   Django can find the translations:

   .. code-block:: python

        LOCALE_PATHS = (
            ...

            "collected/locale",

            ...
        )
