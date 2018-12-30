Downy - Downloading Files in a Blink of the Eye
================================================

**downy** is an open source (MIT) collection of Python functions useful
in web downloads and parallel downloads.
It provides a simple and intuitive API and handles the threads accordingly.

View `source code`_ of downy!

.. _`source code`: https://github.com/downy/downy


Some of its awesome features are:

* Multiple Download Support
* Full utilisation of cores
* Intuitive API for downloads

And more to come!

downy is developed by an open community. Release
announcements and general discussion take place on our `mailing list`_
and `chat`_.

.. _`mailing list`: https://groups.io/g/downy-dev
.. _`chat`: https://riot.im/experimental/#/room/#rest:matrix.org

The `source code`_, `issue tracker`_ and `wiki`_ are hosted on GitHub, and all
contributions and feedback are more than welcome.

.. _`source code`: https://github.com/downy/downy
.. _`issue tracker`: https://github.com/downy/downy/issues
.. _`wiki`: https://github.com/downy/downy/wiki/

downy works on recent versions of Python and is released under
the MIT license, hence allowing commercial use of the library.

.. code-block:: python

    from downy.download import Download

    Download(url, filename).download()


.. note::
    The modules are currently under development and might be unstable at any point of time.
    Please help us by reporting any bugs you encounter while using downy.
