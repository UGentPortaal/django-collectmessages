"""Use the command ``collect_messages`` to generate the translation files::

    $ python django-manage.py collect_messages

This command has the following options:

    -c, --compile   Compile the PO-files.
    -t, --pot-file  Create a POT-file.
    -v, --verbose   Show more information.
"""

import optparse
import os
import os.path

from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
try:
    # Django < 1.9
    from django.utils.importlib import import_module
except ImportError:
    # Django >= 1.9
    from importlib import import_module
from polib import POFile

from collectmessages.finders import BaseMessageFinder


class Command(BaseCommand):
    """Custom Django command ``collect_messages``.
    """
    args = ""
    help = "Collect translated messages from other applications."

    option_list = [o for o in BaseCommand.option_list
                   if "-v" not in o._short_opts] + [
        optparse.make_option(
            "-c", "--compile",
            action="store_true",
            dest="compile",
            default=False,
            help="Compile the PO-files."
        ),
        optparse.make_option(
            "-t", "--pot-file",
            action="store_true",
            dest="pot-file",
            default=False,
            help="Create a POT-file."
        ),
        optparse.make_option(
            "-s", "--verbose",
            action="store_true",
            dest="verbose",
            default=False,
            help="Show more information."
        ),
    ]

    def handle(self, *args, **options):
        """Run the command.
        """
        # Settings.
        locale_dir = settings.COLLECTMESSAGES_PATH
        languages = settings.COLLECTMESSAGES_LANGUAGES
        metadata = getattr(settings, "COLLECTMESSAGES_METADATA", {})

        # Generate a POT-file.
        if options["pot-file"]:

            # Verbose.
            if options["verbose"]:
                self.stdout.write(
                    "collect_messages: processing POT-file")

            # Create the output directory.
            if not os.path.exists(locale_dir):
                os.makedirs(locale_dir)

            # Build the POT-file.
            potfile = POFile()
            potfile.metadata = metadata
            for message in self._find_all(verbose=options["verbose"]):
                potfile.append(message)

            # Save the POT-file.
            potfile_path = os.path.join(locale_dir, "django.pot")
            potfile.save(potfile_path)

        # Generate PO-files for all languages.
        for language in languages:

            # Verbose.
            if options["verbose"]:
                self.stdout.write(
                    "collect_messages: processing language '%s'" % language)

            # Create the output directory.
            message_dir = os.path.join(locale_dir, language, "LC_MESSAGES")
            if not os.path.exists(message_dir):
                os.makedirs(message_dir)

            # Build a PO-file.
            pofile = POFile()
            pofile.metadata = metadata
            for message in self._find_all(language=language,
                                          verbose=options["verbose"]):
                pofile.append(message)

            # Save the PO-file.
            pofile_path = os.path.join(message_dir, "django.po")
            pofile.save(pofile_path)

            # Save the MO-file.
            if options["compile"]:
                mofile_path = os.path.join(message_dir, "django.mo")
                pofile.save_as_mofile(mofile_path)

    def _find_all(self, language=None, verbose=False):
        """Find all translated messages.
        """
        # Settings.
        finders = settings.COLLECTMESSAGES_FINDERS

        # Process all message finders.
        for finder in finders:

            # Verbose.
            if verbose:
                self.stdout.write(
                    "collect_messages: processing finder '%s'" % finder)

            # Import the message finder.
            try:
                module_name, class_name = finder.rsplit(".", 1)
                module = import_module(module_name)
                class_ = getattr(module, class_name)
            except:
                raise CommandError(
                    "Can't find message finder '%s'" % finder)

            # Validate the message finder.
            if not issubclass(class_, BaseMessageFinder):
                raise CommandError(
                    "Invalid message finder '%s'" % finder)

            # Find and yield the messages.
            messages = class_().find(language=language)
            for message in messages:
                yield message
