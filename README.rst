django-collectmessages
======================

Collect translated messages from other applications.


USAGE
-----

1. Add application ``collectmessages`` to ``INSTALLED_APPS`` in
   ``settings.py``::

    INSTALLED_APPS = (
        ...

        'collectmessages',

        ...
    )

2. Add the following options to ``settings.py``:

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

   Example::

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

3. Add ``COLLECTMESSAGES_PATH`` to ``LOCALE_PATHS`` in ``settings.py``::

    LOCALE_PATHS = (
        ...

        "collected/locale",

        ...
    )

4. Use the custom command ``collect_messages`` to generate the translation
   files::

    $ python django-manage.py collect_messages

   This command has the following options:

    -c, --compile   Compile the PO-files.
    -t, --pot-file  Create a POT-file.
    -v, --verbose   Show more information.

5. Create custom message finders by subclassing ``BaseMessageFinder`` and
   customizing method ``find()``::

    from collectmessages.finders import BaseMessageFinder
    from polib import POEntry


    class MessageFinder(BaseMessageFinder):

        def find(self, language=None):
            ...

   Method ``find()`` returns a sequence of ``POEntry`` objects with the
   translated messages.  It takes one (optional) parameter ``language``.  If
   given, this parameter has the language code for the translated messages.
   If not given, ``find()`` should return ``POEntry`` objects for a POT-file,
   with an empty translated string.


CONTRIBUTORS
------------

- Bert Vanderbauwhede <bert.vanderbauwhede@ugent.be>, Author
