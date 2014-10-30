Commands
========


``collect_messages``
--------------------

Use the custom command ``collect_messages`` to generate the translation files:

.. code-block:: bash

    python django-manage.py collect_messages

This command has the following options:

    -c, --compile   Compile the PO-files.
    -t, --pot-file  Create a POT-file.
    -v, --verbose   Show more information.
